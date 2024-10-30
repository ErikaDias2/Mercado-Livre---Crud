from bson.objectid import ObjectId

def DeletarProduto(db):
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
        print(f"   Descrição: {produto.get('descricao', 'N/A')}")
        print(f"   Preço: {produto.get('preco', 'N/A')}")
        print(f"   Estoque: {produto.get('estoque', 'N/A')}")
        print("-" * 40)

    escolha = int(input("Selecione o número do produto que deseja deletar: ")) - 1

    if 0 <= escolha < len(lista_produtos):
        produto = lista_produtos[escolha]
        print(f"O produto {produto['nome']} será deletado.")

        confirmar = input("Tem certeza que deseja deletar este produto? (S/N): ")
        if confirmar.lower() == "s":
            resultado = mycol_produto.delete_one({"_id": ObjectId(produto['_id'])})
            if resultado.deleted_count > 0:
                print("Produto deletado com sucesso.")
            else:
                print("Erro ao deletar o produto.")
        else:
            print("Operação cancelada.")
    else:
        print("Seleção inválida. Tente novamente.")