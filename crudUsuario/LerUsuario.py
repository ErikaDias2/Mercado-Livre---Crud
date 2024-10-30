def LerUsuario(db):
    mycol = db.usuario
    usuarios = mycol.find()

    if mycol.count_documents({}) == 0:
        print("Não há usuário cadastrado.")
        return

    for usuario in usuarios:
        usuario_id = str(usuario['_id'])
        nome = usuario['nome']
        cpf = usuario['cpf']
        email = usuario['email']
        senha = usuario['senha']
        vendas = usuario.get('vendas', [])
        enderecos = usuario['endereco']
        favoritos = usuario.get('favoritos', [])
        compras = usuario.get('compras', [])

        print("x" * 40)
        print("-------- Informações pessoais --------")
        print(f"Id: {usuario_id}")
        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
        print(f"Email: {email}")
        print(f"Senha: {senha}")
        print(f"Vendedor: {'Sim' if vendas else 'Não'}")

        print("------------- Endereço --------------")
        for endereco in enderecos:
            print(f"Rua: {endereco['rua']}")
            print(f"Número: {endereco['numero']}")
            print(f"Bairro: {endereco['bairro']}")
            print(f"Cidade: {endereco['cidade']}")
            print(f"Estado: {endereco['estado']}")
            print(f"CEP: {endereco['cep']}")    
            print("-" * 40)


        if favoritos:
            print("------------ Favoritos -------------")
            for favorito in favoritos:
                print(f"Produto ID: {favorito['produto_id']}")
                print(f"Nome: {favorito['nome']}")
                print(f"Descrição: {favorito.get('descricao', 'N/A')}")
                print(f"Preço: {favorito['preco']}")
                print(f"Estoque: {favorito['estoque']}")
        else:
            print("Favoritos: Nenhum produto favoritado.")


        if compras:
            print("------------ Compras -------------")
            for compra in compras:
                print(f"Produto ID: {compra['produto_id']}")
                print(f"Nome: {compra['nome']}")
                print(f"Descrição: {compra.get('descricao', 'N/A')}")
                print(f"Preço Unitário: {compra['preco']}")
                print(f"Quantidade: {compra['quantidade']}")
                print(f"Valor Total: {compra['preco'] * compra['quantidade']}")
        else:
            print("Compras: Nenhuma compra registrada.")
        
        print("x" * 40)
