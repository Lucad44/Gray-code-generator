def grayCode(n: int):
    if n == 1:
        return [0, 1], [0, 1]
    gray, reflected = ["0", "1"], ["1", "0"]
    for j in range(2, n + 1):
        bin = [i.zfill(j) for i in gray]
        bin += [i.rjust(j, "1") for i in reflected]
        gray, reflected = bin, reversed(bin)
    return bin, [int(i, 2) for i in bin]

def bin2gray(n: int):
    binary = list(bin(n))[2:]
    xor = binary[:-1]
    gray = [binary.pop(0)]
    gray += [str(int(b) ^ int(x)) for b, x in zip(binary, xor)]
    return ''.join(gray)
