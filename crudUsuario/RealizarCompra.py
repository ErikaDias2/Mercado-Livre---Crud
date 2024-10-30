from bson.objectid import ObjectId
from datetime import datetime

def RealizarCompra(db, redis_client, session_id):
    mycol_produto = db.produto
    mycol_usuario = db.usuario

    usuario_logado_nome = redis_client.get(session_id)
    if not usuario_logado_nome:
        print("Nenhum usuário logado. Faça o login primeiro.")
        return

    usuario_logado = mycol_usuario.find_one({"_id": ObjectId(session_id)})
    if not usuario_logado:
        print("Usuário logado não encontrado no banco de dados.")
        return

    print(f"Bem-vindo, {usuario_logado['nome']}!")

    total_produtos = mycol_produto.count_documents({})
    if total_produtos == 0:
        print("Nenhum produto cadastrado.")
        return

    print("-------- Produtos Disponíveis --------")
    produtos = mycol_produto.find().sort("nome", 1)
    lista_produtos = list(produtos)
    for i, produto in enumerate(lista_produtos):
        print(f"{i + 1}. Nome: {produto['nome']}")
        print(f"   Preço: R${produto['preco']}")
        print(f"   Estoque: {produto['estoque']}")
        print(f"   ID: {produto['_id']}")
        print("-" * 40)

    escolha_produto = int(input("Selecione o número do produto que deseja comprar: ")) - 1
    if escolha_produto < 0 or escolha_produto >= len(lista_produtos):
        print("Seleção de produto inválida. Tente novamente.")
        return

    produto_selecionado = lista_produtos[escolha_produto]

    quantidade = int(input(f"Informe a quantidade que deseja comprar do produto {produto_selecionado['nome']}: "))

    if quantidade <= 0:
        print("Quantidade inválida.")
        return

    if produto_selecionado['estoque'] < quantidade:
        print("Estoque insuficiente.")
        return

    mycol_produto.update_one(
        {"_id": ObjectId(produto_selecionado['_id'])},
        {"$inc": {"estoque": -quantidade}}
    )

    compra = {
        "produto_id": str(produto_selecionado['_id']),
        "nome": produto_selecionado["nome"],
        "descricao": produto_selecionado.get("descricao", ""),
        "preco": produto_selecionado["preco"],
        "quantidade": quantidade,
        "data": datetime.now().strftime("%Y-%m-%d")
    }

    mycol_usuario.update_one(
        {"_id": ObjectId(usuario_logado["_id"])},
        {"$push": {"compras": compra}}
    )

    print(f"Compra realizada com sucesso!")
    print(f"Produto: {produto_selecionado['nome']}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço total: R${produto_selecionado['preco'] * quantidade}")
