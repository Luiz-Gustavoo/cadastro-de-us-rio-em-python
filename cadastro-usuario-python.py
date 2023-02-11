print('Olá, bem vindo ao nosso site')
print('-' * 30)

criar_conta = input('Para ver o conteúdo, é preciso criar uma conta. Deseja criar uma conta?(s/n): ')
if criar_conta == 's':
    print('Vamos precisar das seguintes informações:')

    nome_formatado = False
    while nome_formatado == False:
        nome = input('digite o seu nome: ')

        if type(nome) != str:
            print('digite apenas letras')
        elif type(nome) == str:
            nome_formatado = True

    senha_formatada = False
    while senha_formatada == False:
        senha = input('digite sua senha:')
        senha_int = int(senha)

        if type(senha_int) != int:
            print('digite apenas números')
        elif type(senha_int) == int:
            senha_formatada = True

    print('vamos checar suas informações agora...')        
    print(f'seu nome é: {nome}')
    print(f'sua senha é: {senha}')
    

              


elif criar_conta == 'n':
    print('Caso mudar de ideia estaremos aqui')

else:
    print('Nenhuma opção válida foi escolhida')

