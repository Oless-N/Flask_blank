import functools


def post_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pass
