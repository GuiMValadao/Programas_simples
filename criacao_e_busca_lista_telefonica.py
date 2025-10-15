if __name__ == '__main__':
    print("""
        Bem vindo à lista telefônica. Para usá-la siga os seguintes passos:
          1 - Forneça o número de entradas desejado'
          2 - Forneça Nome e Telefone, separados por um espaço, com número total igual ao informado em 1'
          3 - Forneça os nomes a serem procurados na lista.
          4 - Após terminar a entrada dos nomes, digite 'end';
""")
    n = int(input('Digite o número de valores para a lista: '))
    phonebook = {}
    searching, search = [], ' '
    for entry in range(n):
        name, phone = input('Digite Nome e Telefone separados por um espaço: ').split(' ')
        phonebook[name] = phone
    search = input()
    while True:
        searching.append(search)        
        search = input()
        if search == 'end':
            break

for individual in searching:
    if individual in phonebook.keys():
        print(f"{individual}={phonebook[individual]}")
    else:
        print('Not found')