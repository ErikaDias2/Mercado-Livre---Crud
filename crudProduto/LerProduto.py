def LerProduto(db):
    mycol_produto = db.produto
    produtos = mycol_produto.find()

    for produto in produtos:
        produto_id = str(produto['_id'])
        nome = produto['nome']
        descricao = produto['descricao']
        preco = produto['preco']
        estoque = produto['estoque']
        owner = produto['owner']
        
        print(f"Id: {produto_id}")
        print(f"Nome: {nome}")
        print(f"Descrição: {descricao}")
        print(f"Preço: ${preco}")
        print(f"Estoque: {estoque}")
        print(f"Vendedor: {owner['nome']} (Id: {owner['id']})")
        print("-" * 40)