from datetime import datetime


# https://www.cnblogs.com/Neroi/p/11514984.html

def fdt(x):
    """
    Format DateTime -- fdt
    :param x:
    :return:
    """
    f = '%Y%m%d'
    return datetime.strptime(x, f)


print(fdt('20200520'))
