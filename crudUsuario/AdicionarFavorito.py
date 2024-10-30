from bson.objectid import ObjectId

def AdicionarFavorito(db, redis_client, session_id):
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

    escolha_produto = int(input("Selecione o número do produto que deseja adicionar aos favoritos: ")) - 1
    if escolha_produto < 0 or escolha_produto >= len(lista_produtos):
        print("Seleção de produto inválida. Tente novamente.")
        return

    produto_selecionado = lista_produtos[escolha_produto]

    favorito_existente = next((f for f in usuario_logado.get('favoritos', []) if f['produto_id'] == str(produto_selecionado['_id'])), None)
    
    if favorito_existente:
        print("Produto já está nos favoritos.")
        return

    favorito = {
        "produto_id": str(produto_selecionado['_id']),
        "nome": produto_selecionado["nome"],
        "descricao": produto_selecionado.get("descricao", ""),
        "preco": produto_selecionado["preco"],
        "estoque": produto_selecionado["estoque"]
    }

    mycol_usuario.update_one(
        {"_id": ObjectId(usuario_logado["_id"])},
        {"$push": {"favoritos": favorito}}
    )

    print(f"O produto {produto_selecionado['nome']} foi adicionado aos favoritos.")
