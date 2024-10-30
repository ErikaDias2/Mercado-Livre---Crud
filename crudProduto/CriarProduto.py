def CriarProduto(db):
    mycol_produto = db.produto
    mycol_usuario = db.usuario


    vendedores = mycol_usuario.find({"vendas": True}).sort("nome", 1)
    total_vendedores = mycol_usuario.count_documents({"vendas": True})


    if total_vendedores == 0:
        print("Nenhum vendedor cadastrado.")
        return


    print("Vendedores cadastrados:")
    lista_vendedores = list(vendedores)
    for i, vendedor in enumerate(lista_vendedores):
        print(f"{i + 1}. Nome: {vendedor['nome']}")
        print(f"   CPF: {vendedor['cpf']}")
        print("-" * 40)


    escolha = int(input("Selecione o número do vendedor: ")) - 1

    if 0 <= escolha < len(lista_vendedores):
        vendedor = lista_vendedores[escolha]
        print(f"O produto será associado ao vendedor {vendedor['nome']}.")


        nome = input("Nome do produto: ")
        descricao = input("Descrição: ")
        preco = float(input("Preço: $"))
        estoque = int(input("Estoque: "))

        owner = {
            "id": str(vendedor["_id"]),
            "nome": vendedor["nome"]
        }


        produto = {
            "nome": nome,
            "descricao": descricao,
            "preco": preco,
            "estoque": estoque,
            "owner": owner
        }


        resultado = mycol_produto.insert_one(produto)
        print(f"Produto inserido com o ID: {resultado.inserted_id}")
    else:
        print("Seleção inválida. Tente novamente.")