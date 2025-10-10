
def print_formatted(number):
    """
        Takes an integer number and generates
        a table of numbers on base 10, 8, 16 and 2.
    """
    binary = ''
    num_bin = number
    while num_bin > 0:
        binary = str(num_bin%2) + '' + binary
        num_bin = num_bin//2
    length = len(binary)
    
    for i in range(1, number+1):
        binary = ''
        num_bin = i
        while num_bin > 0:
            binary = str(num_bin%2) + '' + binary
            num_bin = num_bin//2
        
        octal = ''
        num_octal = i
        while num_octal > 0:
            octal = str(num_octal%8) + '' + octal
            num_octal = num_octal//8
        
        hexadecimal = ''
        num_hexa = i
        transf = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
        while num_hexa > 0:
            if num_hexa%16<10:
                hexadecimal = str(num_hexa%16) + '' + hexadecimal
            else:
                hexadecimal = str(transf[num_hexa%16]) + '' + hexadecimal
            num_hexa = num_hexa//16
        
        print(str(i).rjust(length, ' '), end=' ')
        print(octal.rjust(length, ' '), end=' ')
        print(hexadecimal.rjust(length, ' '), end=' ')
        print(binary.rjust(length, ' '))
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)