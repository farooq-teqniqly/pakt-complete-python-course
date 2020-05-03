import functools
import time
import logging


def timeit(logger=None):
    def _decorator(func):
        @functools.wraps(func)
        def _timeit(*args, **kwargs):
            start = time.perf_counter_ns()
            try:
                return func(*args, **kwargs)
            finally:
                end = time.perf_counter_ns()

                if logger:
                    logger.debug(
                        f"[{func.__name__}]Executed in {(end - start)/1000000}ms"
                    )

        return _timeit

    return _decorator


def configue_logger(name: str):
    logger = logging.getLogger(name)
    log_entry_format = (
        "%(asctime)s %(levelname)-8s %(name)s [%(filename)s:%(lineno)d] %(message)s"
    )
    logging.basicConfig(level=logging.DEBUG, format=log_entry_format)
    logging.Formatter.converter = time.gmtime

    return logger


logger = configue_logger("timeit_test")


@timeit(logger=logger)
def foo():
    time.sleep(3)


@timeit(logger=logger)
def bar():
    time.sleep(4)


class Qux:
    @timeit(logger=logger)
    def f(self):
        for i in range(1, 1000):
            pass

    @timeit(logger=logger)
    def x(self):
        raise ValueError("Oops!")


if __name__ == "__main__":
    foo()
    bar()
    Qux().f()
    Qux().x()
