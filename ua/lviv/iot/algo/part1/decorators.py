"""
Contains decorator realisations
"""
import time
from functools import wraps


def timer(func):
    def wrapper(*args):
        before = time.time()
        result = func(*args)
        print("Function took", time.time() - before, "seconds to execute")
        return result

    return wrapper


def iterator_to_tuple(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_iterator = func(*args, **kwargs)
        result = tuple(original_iterator)
        return result

    return wrapper
