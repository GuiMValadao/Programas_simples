def print_formatted(number):
    """
        Takes an integer number and generates
        a table of numbers on base 10, 8, 16 and 2
        using python built-in methods.
    """
    length = len(str(bin(number)).replace('0b', ''))
    for i in range(1, number+1):
        print(str(i).rjust(length, ' '), 
              oct(i).replace('0o', '').rjust(length, ' '),
              hex(i).replace('0x', '').upper().rjust(length, ' '), 
              bin(i).replace('0b', '').rjust(length, ' '))

if __name__ == '__main__':
    n = int(input('Digite o número máximo para a tabela'))
    print_formatted(n)