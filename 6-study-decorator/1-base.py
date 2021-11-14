# @Time    : 2021/2/15 22:11
# @Author  : Lizo
# @File    : producer.py


def printer(func):
    def wrapper(*args):
        print("in the wrapper param=%s" % args)
        return func(args)
    return wrapper


def target(param):
    print("in the target param=%s" % param)


a = printer(target)(1)
