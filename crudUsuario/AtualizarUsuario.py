import hashlib

def AtualizarUsuario(db):
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

    escolha = int(input("Selecione o número do usuário que deseja atualizar: ")) - 1

    if 0 <= escolha < len(lista_usuarios):
        usuario = lista_usuarios[escolha]
        print(f"As atualizações serão feitas no usuário {usuario['nome']}")
        novo_nome = usuario['nome']
        novo_email = usuario['email']
        nova_senha = usuario['senha']
        novo_endereco = usuario['endereco']

        atualizarNome = input("Atualizar nome? (S/N): ")
        if atualizarNome.lower() == "s":
            novo_nome = input("Novo nome: ")
        
        atualizarEmail = input("Atualizar email? (S/N): ")
        if atualizarEmail.lower() == "s":
            novo_email = input("Novo email: ")
        
        atualizarSenha = input("Atualizar senha? (S/N): ")
        if atualizarSenha.lower() == "s":
            nova_senha = hashlib.sha256(input("Nova senha: ").encode()).hexdigest()
        
        atualizarEndereco = input("Atualizar endereço? (S/N): ")
        if atualizarEndereco.lower() == "s":
            novo_endereco = []
            rua = input("Nova rua: ")
            numero = input("Novo número: ")
            bairro = input("Novo bairro: ")
            cidade = input("Nova cidade: ")
            estado = input("Novo estado: ")
            cep = input("Novo CEP: ")

            endereco = {
                "rua": rua,
                "numero": numero,
                "bairro": bairro,
                "cidade": cidade,
                "estado": estado,
                "cep": cep
            }
            novo_endereco.append(endereco)


        mycol.update_one(
            {"cpf": usuario['cpf']},
            {"$set": {"nome": novo_nome, "senha": nova_senha, "email": novo_email, "endereco": novo_endereco}}
        )
        print("Usuário atualizado com sucesso.")
    else:
        print("Seleção inválida. Tente novamente.")


