def pipeline(*funcs):
    def helper(arg):
        for f in funcs:
            arg = f(arg)
        return arg
    return helper

fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3)) #should print 5.0