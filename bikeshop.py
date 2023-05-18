# Início das variáveis globais
lista_peca = []
codigo_peca = 0
# Fim das variáveis globais

# Início do cadastro de peças
def cadastrarPeca(codigo):
    print('Boas-vindas ao menu de cadastrar peças.')
    print('Código da peça: {}' .format(codigo))
    nome = input('Digite o nome da peça: ')
    fabricante = input('Digite o fabricante da peça: ')
    preco = float(input('Digite o preço da peça: R$ '))
    dicionario_peca = {'codigo'     : codigo,
                       'nome'       : nome,
                       'fabricante' : fabricante,
                       'preco'      : preco}
    lista_peca.append(dicionario_peca.copy())
# Fim do cadastro de peças

# Início da consulta de peças
def consultarPeca():
    print('Boas-vindas ao menu de consultar peças.')
    while True:
        opcao_consultar = input('\n\033[7mEscolha a opção desejada:\033[m\n' +
                                '1 - Consultar todas as peças\n' +
                                '2 - Consultar peça por código\n' +
                                '3 - Consultar peça por fabricante\n' +
                                '4 - Retornar\n' +
                                '\nDigite o código escolhido \n\033[7m>>\033[m ')
        if opcao_consultar == '1':
            print('Você escolheu a opção para consultar todos os produtos')
            for peca in lista_peca:
                print('-------------------------')
                for key, value in peca.items(): # varrer todos os conjuntos de chave e valor do dicionário de peças
                    print('{}: {}' .format(key,value))
                print('-------------------------')
        elif opcao_consultar == '2':
            print('Você escolheu a opção para consultar peça por código')
            valor_desejado = int(input('Digite o código desejado: '))
            for peca in lista_peca:
                if peca['codigo'] == valor_desejado: # o valor do campo código desse dicionário é igual ao valor desejado
                   print('-------------------------')
                   for key, value in peca.items():  # varrer todos os conjuntos de chave e valor do dicionário de peças
                        print('{}: {}'.format(key, value))
                   print('-------------------------')
        elif opcao_consultar == '3':
            print('Você escolheu a opção para consultar peça por fabricante')
            valor_desejado = input('Digite o fabricante desejado: ')
            for peca in lista_peca:
                if peca['fabricante'] == valor_desejado:  # o valor do campo código desse dicionário é igual ao valor desejado
                    print('-------------------------')
                    for key, value in peca.items():  # varrer todos os conjuntos de chave e valor do dicionário de peças
                        print('{}: {}'.format(key, value))
                    print('-------------------------')
        elif opcao_consultar == '4':
            return # volta ao Main
        else:
            print('Opção inválida. Tente novamente.')
            continue  # volta para o início do laço
# Fim da consulta de peças

# Início da opção de remover peças
def removerPeca():
    print('Boas-vindas ao menu de remover peça.')
    valor_desejado = int(input('Digite o código do produto que deseja remover: '))
    for peca in lista_peca:
        if peca['codigo'] == valor_desejado:  # o valor do campo código desse dicionário é igual ao valor desejado
            lista_peca.remove(peca)
            print('Produto removido com sucesso.')
# Fim da opção de remover peças

# Início do Main
print('\n\033[7mBoas-vindas ao Controle de Estoque da Bicicletaria de Carolina Cozer Bacca\033[m')
print('-=' * 37)
while True:
    opcao_principal = input('\n\033[7mEscolha a opção desejada:\033[m\n'+
                            '1 - Cadastrar Peça\n'+
                            '2 - Consultar Peça\n'+
                            '3 - Remover Peça\n'+
                            '4 - Sair\n'+
                            '\nDigite o código escolhido \n\033[7m>>\033[m ')
    if opcao_principal == '1':
        codigo_peca = codigo_peca + 1
        cadastrarPeca(codigo_peca)
    elif opcao_principal == '2':
        consultarPeca()
    elif opcao_principal == '3':
        removerPeca()
    elif opcao_principal == '4':
        print('Programa finalizado. Até a próxima!')
        break # encerra o laço principal e o programa acaba
    else:
        print('Opção inválida. Tente novamente.')
        continue # volta para o início do Main
# Fim do Main