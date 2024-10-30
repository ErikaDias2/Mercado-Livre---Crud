def DeletarUsuario(db):
    mycol = db.usuario
    total_usuarios = mycol.count_documents({})

    if total_usuarios == 0:
        print("Nenhum usuário cadastrado.")
        return
    usuarios = mycol.find().sort("nome", 1)

    print("-------- Usuários cadastrados ----------")
    lista_usuarios = list(usuarios)
    for i, usuario in enumerate(lista_usuarios):
        print(f"{i + 1}. Nome: {usuario['nome']}")
        print(f"   CPF: {usuario['cpf']}")
        print(f"   Email: {usuario['email']}")
        print("-" * 40)

    escolha = int(input("Selecione o número do usuário que deseja deletar: ")) - 1

    if 0 <= escolha < len(lista_usuarios):
        usuario = lista_usuarios[escolha]
        print(f"O usuário {usuario['nome']} será deletado.")

        confirmar = input("Tem certeza que deseja deletar este usuário? (S/N): ")
        if confirmar.lower() == "s":
            mycol.delete_one({"cpf": usuario['cpf']})
            print("Usuário deletado com sucesso.")
        else:
            print("Operação cancelada.")
    else:
        print("Seleção inválida. Tente novamente.")