# @param {integer} x
# @return {integer}


def reverse(self, x):
    res = 0
    if x >= 0:
        res = int(str(x)[::-1])
        if res > 2147483647:
            return 0
        else:
            return res
    else:
        res = int('-' + str(x)[::-1][:-1])
        if res < -2147483647:
            return 0
        else:
            return res
