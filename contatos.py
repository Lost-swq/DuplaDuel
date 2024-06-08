class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

class GerenciadorContatos:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
        print(f'Contato {contato.nome} adicionado com sucesso!')

    def listar_contatos(self):
        if self.contatos:
            print('Lista de Contatos:')
            for contato in self.contatos:
                print(f'Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}')
        else:
            print('Nenhum contato encontrado.')

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                print(f'Contato encontrado - Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}')
                return
        print('Contato não encontrado.')

# aqui vamos ter as info dos contatos, abaixo:
def obter_detalhes_contato():
    nome = input('Digite o nome do contato: ')
    telefone = input('Digite o número de telefone do contato: ')
    email = input('Digite o email do contato: ')
    return Contato(nome, telefone, email)

# Exemplo de uso
gerenciador = GerenciadorContatos()

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
