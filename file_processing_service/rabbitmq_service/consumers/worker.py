from functools import wraps

workers_map = {}

def worker():
    def decorator(func):
        workers_map[func.__name__] = func
        @wraps(func)
        async def wrapper(*args, **kwargs):
            return await func(*args, **kwargs)
        return wrapper
    return decorator

@worker()
async def process_message(message: str) -> None:
    # Process the incoming message
    pass