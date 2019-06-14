# -*- coding: utf-8 -*- #


def safe_int(src):
    """
    转成int
    """
    if not src:
        return src
    else:
        return int(src)