import time
import logging
from functools import wraps
from typing import Callable, Any

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def process_request(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator for logging request information.  Supports async functions.
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            response = await func(*args, **kwargs) if hasattr(func, "__call__") and hasattr(func, "__code__") and func.__code__.co_flags & 0x20 else func(*args, **kwargs)
            end_time = time.time()
            logging.info(f"Request to {func.__name__} took {end_time - start_time:.4f} seconds")
            return response
        except Exception as e:
            end_time = time.time()
            logging.error(f"Request to {func.__name__} failed after {end_time - start_time:.4f} seconds: {e}")
            raise
    return wrapper

setup_logging()