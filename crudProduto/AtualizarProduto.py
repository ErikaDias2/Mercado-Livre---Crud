from bson.objectid import ObjectId

def AtualizarProduto(db):
    mycol_produto = db.produto
    total_produtos = mycol_produto.count_documents({})

    if total_produtos == 0:
        print("Nenhum produto cadastrado.")
        return

    produtos = mycol_produto.find().sort("nome", 1)

    print("-------- Produtos cadastrados ----------")
    lista_produtos = list(produtos)
    for i, produto in enumerate(lista_produtos):
        print(f"{i + 1}. Nome: {produto['nome']}")
        print(f"   ID: {produto['_id']}")
        print(f"   Preço: ${produto['preco']}")
        print(f"   Estoque: {produto['estoque']}")
        print("-" * 40)

    escolha = int(input("Selecione o número do produto que deseja atualizar: ")) - 1

    if 0 <= escolha < len(lista_produtos):
        produto = lista_produtos[escolha]
        print(f"As atualizações serão feitas no produto {produto['nome']}")

        novo_nome = produto['nome']
        nova_descricao = produto['descricao']
        novo_preco = produto['preco']
        novo_estoque = produto['estoque']

        atualizarNome = input("Atualizar nome? (S/N): ")
        if atualizarNome.lower() == "s":
            novo_nome = input("Novo nome: ")
        
        atualizarDescricao = input("Atualizar descrição? (S/N): ")
        if atualizarDescricao.lower() == "s":
            nova_descricao = input("Nova descrição: ")
        
        atualizarPreco = input("Atualizar preço? (S/N): ")
        if atualizarPreco.lower() == "s":
            novo_preco = float(input("Novo preço: "))
        
        atualizarEstoque = input("Atualizar estoque? (S/N): ")
        if atualizarEstoque.lower() == "s":
            novo_estoque = int(input("Novo estoque: "))

        updates = {}
        if novo_nome:
            updates['nome'] = novo_nome
        if nova_descricao:
            updates['descricao'] = nova_descricao
        if novo_preco:
            updates['preco'] = novo_preco
        if novo_estoque:
            updates['estoque'] = novo_estoque

        if updates:
            mycol_produto.update_one({"_id": ObjectId(produto['_id'])}, {"$set": updates})
            print("Produto atualizado com sucesso.")
        else:
            print("Nenhuma atualização foi feita.")
    else:
        print("Seleção inválida. Tente novamente.")
