class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Digite o nome do contato: ")
        phone_number = input("Digite o número de telefone do contato: ")
        contact = {'name': name, 'phone_number': phone_number}
        self.contacts.append(contact)
        print(f"Contato {name} adicionado com sucesso.")

    def list_contacts(self):
        if self.contacts:
            print("Lista de contatos:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. Nome: {contact['name']}, Telefone: {contact['phone_number']}")
        else:
            print("Nenhum contato encontrado.")

    def remove_contact(self):
        name = input("Digite o nome do contato que deseja remover: ")
        for contact in self.contacts:
            if contact['name'] == name:
                self.contacts.remove(contact)
                print(f"Contato {name} removido com sucesso.")
                return
        print(f"Contato {name} não encontrado.")

if __name__ == "__main__":
    contact_manager = ContactManager()
    while True:
        print("\n1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Remover Contato")
        print("4. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            contact_manager.add_contact()
        elif choice == '2':
            contact_manager.list_contacts()
        elif choice == '3':
            contact_manager.remove_contact()
        elif choice == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
