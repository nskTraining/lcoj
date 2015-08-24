# @param {integer} x
# @return {integer}


def reverse(self, x):
    '''
    Return reversed int or 0 if int become too long while reversed
    Arguments:
    x : the int to reverse
    '''

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
