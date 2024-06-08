import contato, contatos_manager

while True:
    print('\n1 - Adicionar Contato')
    print('2 - Listar Contatos')
    print('3 - Pesquisar Contato')
    print('4 - Sair')

    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        contato = obter_detalhes_contato()
        gerenciador.adicionar_contato(contato)
    elif escolha == '2':
        gerenciador.listar_contatos()
    elif escolha == '3':
        nome = input('Digite o nome do contato a ser pesquisado: ')
        gerenciador.buscar_contato(nome)
    elif escolha == '4':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')
