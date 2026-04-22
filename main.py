from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents.main_agent import Agent
from observability.monitoring import process_request
from guardrails.safety import validate_input, validate_output
from error_handling.handler import retry
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
@process_request()
async def chat_endpoint(request: ChatRequest):
    try:
        user_message = validate_input(request.message)
        agent = Agent()
        agent_response = retry(agent.run)(user_message)
        validated_response = validate_output(agent_response)
        return ChatResponse(response=validated_response)
    except Exception as e:
        logging.exception("Error processing chat request")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn, os, socket
    def _port_free(p):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.3)
            return s.connect_ex(("127.0.0.1", p)) != 0
    port = int(os.environ.get("PORT", 8081))
    while not _port_free(port):
        print(f"Port {port} is already in use.")
        try:
            ans = input(f"Try port {port + 1} instead? [Y/n]: ").strip().lower()
        except EOFError:
            ans = "y"
        if ans in ("", "y", "yes"):
            port += 1
        else:
            print("Exiting. Free the port and try again.")
            raise SystemExit(1)
    print(f"Starting server on http://0.0.0.0:{port}")
    uvicorn.run(app, host="0.0.0.0", port=port)