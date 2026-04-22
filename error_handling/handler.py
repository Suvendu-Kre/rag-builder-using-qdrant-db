import time
import random

def retry(func, attempts=3, delay=1, exponential_backoff=True):
    """Retry a function with exponential backoff."""
    def wrapper(*args, **kwargs):
        attempt = 0
        while attempt < attempts:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                attempt += 1
                if attempt == attempts:
                    raise
                sleep_time = delay * (2 ** (attempt - 1) if exponential_backoff else 1) + random.random()
                print(f"Attempt {attempt} failed. Retrying in {sleep_time:.2f} seconds...")
                time.sleep(sleep_time)
    return wrapper

# Placeholder for circuit breaker implementation
def circuit_breaker(func, failure_threshold=5, recovery_timeout=30):
    """A simple circuit breaker."""
    # In a real implementation, you'd track failures and open/close the circuit
    return func