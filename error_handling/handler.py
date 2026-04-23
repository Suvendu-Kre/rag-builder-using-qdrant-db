import time
import random

def retry(func, attempts=3, delay=1, backoff=2):
    """Retry a function with exponential backoff."""
    for i in range(attempts):
        try:
            return func()
        except Exception as e:
            print(f"Attempt {i+1} failed: {e}")
            if i == attempts - 1:
                raise  # Re-raise the exception after the last attempt
            sleep_time = delay * (backoff ** i) + random.uniform(0, 1)
            time.sleep(sleep_time)

# Placeholder for circuit breaker implementation.  In a real system,
# this would track failure rates and prevent calls to failing services.
def circuit_breaker(func):
    """A simple circuit breaker (not fully implemented)."""
    def wrapper(*args, **kwargs):
        # In a real implementation, check circuit state here
        return func(*args, **kwargs)
    return wrapper