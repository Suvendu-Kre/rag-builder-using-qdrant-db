import time
import random
import logging
from typing import Callable, Any

def retry(func: Callable[..., Any], attempts: int = 3, delay: int = 1, exponential_backoff: bool = True) -> Callable[..., Any]:
    """
    Retry decorator with exponential backoff.
    """
    def wrapper(*args, **kwargs):
        attempt = 0
        while attempt < attempts:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                attempt += 1
                if attempt == attempts:
                    logging.error(f"Function {func.__name__} failed after {attempts} attempts: {e}")
                    raise
                sleep_time = delay * (2 ** (attempt - 1) if exponential_backoff else 1) + random.random()
                logging.warning(f"Retrying {func.__name__} in {sleep_time:.2f} seconds...")
                time.sleep(sleep_time)
    return wrapper

class CircuitBreaker:
    """
    Simple circuit breaker implementation.
    """
    def __init__(self, failure_threshold: int = 3, recovery_timeout: int = 30):
        self.failure_count = 0
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.last_failure_time = None

    def is_open(self) -> bool:
        if self.last_failure_time and time.time() - self.last_failure_time > self.recovery_timeout:
            self.failure_count = 0  # Reset if recovery timeout has passed
            return False
        return self.failure_count >= self.failure_threshold

    def record_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()

    def record_success(self):
        self.failure_count = 0
        self.last_failure_time = None

    def call(self, func: Callable[..., Any], *args, **kwargs):
        if self.is_open():
            raise Exception("Circuit breaker is open.")
        try:
            result = func(*args, **kwargs)
            self.record_success()
            return result
        except Exception as e:
            self.record_failure()
            raise