contatos = []

def adicionarcontato(nome, telefone, email):
    contato = {'nome': nome, 'telefone': telefone, 'email': email}
    contatos.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")

def listarcontatos():
    if not contatos:
        print("Nenhum contato encontrado.")
        return
    for i, contato in enumerate(contatos):
        print(f"{i+1}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")

def removercontato(indice):
    try:
        contato = contatos.pop(indice - 1)
        print(f"Contato {contato['nome']} removido com sucesso!")
    except IndexError:
        print("Índice inválido. Tente novamente.")

def main():
    continuar = True
    while continuar:
        print("\nEscolha uma opção:")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Remover contato")
        print("4. Sair")
        opcao = input("Opção: ")

        if opcao == '1':
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            email = input("Digite o email: ")
            adicionarcontato(nome, telefone, email)
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            listar_contatos()
            try:
                indice = int(input("Digite o índice do contato a remover: "))
                remover_contato(indice)
            except ValueError:
                print("Índice inválido. Tente novamente.")
        elif opcao == '4':
            print("Saindo...")
            continuar = False
        else:
            print("Opção inválida. Tente novamente.")

if __name == "__main":
    main()