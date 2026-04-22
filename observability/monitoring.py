import logging
from functools import wraps
from typing import Callable, Any

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_request():
    """
    Decorator for logging request information.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            logging.info(f"Request received for: {func.__name__}")
            try:
                result = await func(*args, **kwargs)
                logging.info(f"Request completed for: {func.__name__}")
                return result
            except Exception as e:
                logging.error(f"Error in {func.__name__}: {e}")
                raise
        return wrapper
    return decorator