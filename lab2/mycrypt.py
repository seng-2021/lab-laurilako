import codecs

def encode(s):
    if not isinstance(s, str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    else:
        s = s.rjust(1000, 'x')
    for c in s:
        if c.isalpha() and c not in ['ä', 'ö', 'å']:
            if c.islower():
                c=c.upper()
            else:
                c=c.lower()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
            crypted+=digitmapping[c]
        else:
            raise ValueError
    crypted = crypted[(1000-origlen):]
    return crypted

def decode(s):
    return encode(s)