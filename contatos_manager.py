import contato

class GerenciadorContatos():
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
        return super().__init__(nome,telefone,email) 
