import logging
from functools import wraps
from typing import Callable, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_request(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator for logging request information.  This version supports async functions.
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        logging.info(f"Request received for: {func.__name__} with args: {args} and kwargs: {kwargs}")
        try:
            result = await func(*args, **kwargs)
            logging.info(f"Request completed for: {func.__name__}")
            return result
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {e}")
            raise
    return wrapper