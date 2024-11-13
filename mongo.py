def parse(mongo):
    byte = bytes.fromhex(mongo)

    t = byte[0:4]
    p = byte [4:9]
    c = byte[9:12]

    timestamp = int.from_bytes(t, "big")
    process = p
    counter = int.from_bytes(c, "big")
    return timestamp, process, counter

def build(timestamp, process, counter):
    t = timestamp.to_bytes(4, "big")
    p = process
    c = counter.to_bytes(3, "big")
    return (t+p+c).hex()