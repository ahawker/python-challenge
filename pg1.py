__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'

def pg1():
    """
    Alphabet chars need to shift forward by two with circular wrap.
    NEXT: http://www.pythonchallenge.com/pc/def/ocr.html
    """
    s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.\
     bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.\
      sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    a, z = ord('a'), ord('z')
    def _transform(c):
        if not a <= c <= z:
            return c
        c = (c+ 2) % (z + 1)
        return (c + a) if c < a else c
    return ''.join(map(chr, map(_transform, map(ord, s))))
