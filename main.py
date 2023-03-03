Thaibase_CHARS = "๐๑๒๓๔๕๖๗๘๙กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ!#$%&()*+,-./:;<=>?@[]^_`{|}~฿"

def thaibase_encode(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    elif not isinstance(data, bytes):
        raise TypeError("Got fucked")

    result = ''
    value = 0
    bits = 0
    for b in data:
        value = (value << 8) | b
        bits += 8
        while bits >= 6:
            bits -= 6
            index = (value >> bits) & 0x3f
            result += Thaibase_CHARS[index]
    if bits > 0:
        index = (value << (6 - bits)) & 0x3f
        result += Thaibase_CHARS[index]
    
    return result

def thaibase_decode(data):
    if isinstance(data, bytes):
        data = data.decode('utf-8')
    elif not isinstance(data, str):
        raise TypeError("dammit!")
    result = bytearray()
    value = 0
    bits = 0
    for c in data:
        index = Thaibase_CHARS.find(c)
        if index < 0:
            raise ValueError("sussy chars error")
        value = (value << 6) | index
        bits += 6
        if bits >= 8:
            bits -= 8
            result.append((value >> bits) & 0xff)
    
    return result.decode('utf-8')
    
th = thaibase_encode("hello, สวัสดี")

print(f"encode: {th}")
print(f"decode: {thaibase_decode(th)}")
