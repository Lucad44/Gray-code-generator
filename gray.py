from tabulate import tabulate
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

def main():
    print("This program can generate the Gray encoding with n bits,\nand convert a single decimal number to Gray code as well.\n")
    while True:
        n = input("Enter the number of bits: ")
        if n.isdigit() and int(n) >= 1:
            break
        print("Enter a valid number")
    bina, dec = grayCode(int(n))
    table = zip(bina, dec)
    print(tabulate(table, headers=["Binary", "Decimal"], tablefmt='psql'))
    while True:
        n = input("Enter a base 10 number: ")
        if n.isdigit():
            break
        print("Enter a valid number")
    print(f"\nGray code of {n}d ({''.join(list(bin(int(n))))[2:]}b): {bin2gray(int(n))}")


if __name__ == "__main__":
    main()
