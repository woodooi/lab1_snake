"""
Contains decorator realisations
"""
import logging
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


def logged(custom_exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except custom_exception as ex:
                if mode == "console":
                    logging.basicConfig(format="%(asctime)s - %(message)s)")
                    logging.error(str(ex))
                elif mode == "file":
                    logging.basicConfig(filename="log.log", filemode="w", format="%(asctime)s - %(message)s")
                    logging.error(str(ex))
                else:
                    raise ValueError("Incorrect mode value: mode can be \"console\" or \"file\"")
        return wrapper
    return decorator
