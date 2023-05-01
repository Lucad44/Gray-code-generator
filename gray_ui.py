# Gray Encoding Generator console application
from tabulate import tabulate
from gray import grayCode, bin2gray
def mode_sel() -> int:
    # description
    print(
        "Welcome to the Gray Encoding Generator application.\nThis program can construct an n-bit Gray code,\nand convert a single decimal number to Gray code as well.\n")
    # set mode
    print("What do you wish to do?\n1) Generate an n-bit Gray code\n2) Convert a decimal number to Gray code")
    while True:
        n = input("Type 1 or 2: ")
        if n == '1' or n == '2':
            break
        print("Enter a valid option")
    return int(n)

def gray_txt(table):
    with open("gray_output.txt", "w") as f:
        f.write(tabulate(table, tablefmt='plain'))
    print("\nFile created successfully!")

def main():
    match mode_sel():
        # n-bit gray code
        case 1:
            while True:
                n = input("Enter the number of bits: ")
                if n.isdigit() and int(n) > 0:
                    break
                print("Enter a valid number")
            b, dec = grayCode(int(n))
            table = zip(b, dec)
            print("\nWould you like the output:\n1) To be printed here in the console\n2) To be printed in a 'gray_output.txt' file located in the same directory as the executable (Recommended for larger numbers of bits)")
            while True:
                m = input("Type 1 or 2: ")
                if m == '1' or m == '2':
                    break
                print("Enter a valid option")
            match int(m):
                case 1:
                    print(tabulate(table, headers=["Binary", "Decimal"], tablefmt='psql'))
                case 2:
                    gray_txt(table)
        # conversion
        case 2:
            while True:
                n = input("Enter the number you wish to convert: ")
                if n.isdigit() and int(n) >= 0:
                    break
                print("Enter a valid number")
            print(f"\nGray code of {n}d ({''.join(list(bin(int(n))))[2:]}b): {bin2gray(int(n))}")
    input("Press any key to exit...")

if __name__ == "__main__":
    main()
