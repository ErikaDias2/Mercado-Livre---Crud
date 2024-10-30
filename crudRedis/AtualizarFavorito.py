from bson.objectid import ObjectId
import json

def AtualizarFavorito(db, redis_client, session_id):
    mycol_usuario = db.usuario

    usuario_logado_nome = redis_client.get(session_id)
    if not usuario_logado_nome:
        print("Nenhum usuário logado. Faça o login primeiro.")
        return

    favoritos_json = redis_client.get(f"favoritos:{session_id}")
    favoritos = json.loads(favoritos_json) if favoritos_json else []

    if not favoritos:
        print("Nenhum favorito encontrado.")
        return

    print("-------- Favoritos Disponíveis --------")
    for i, favorito in enumerate(favoritos):
        print(f"{i + 1}. Nome: {favorito['nome']}")
        print(f"   Preço: R${favorito['preco']}")
        print(f"   ID: {favorito['produto_id']}")
        print("-" * 40)

    escolha_favorito = int(input("Selecione o número do favorito que deseja atualizar: ")) - 1
    if escolha_favorito < 0 or escolha_favorito >= len(favoritos):
        print("Seleção de favorito inválida. Tente novamente.")
        return

    favorito_selecionado = favoritos[escolha_favorito]

    novo_nome = input(f"Informe o novo nome (atual: {favorito_selecionado['nome']}): ") or favorito_selecionado['nome']
    nova_descricao = input(f"Informe a nova descrição (atual: {favorito_selecionado['descricao']}): ") or favorito_selecionado['descricao']
    novo_preco = input(f"Informe o novo preço (atual: R${favorito_selecionado['preco']}): ") or favorito_selecionado['preco']

    favorito_selecionado['nome'] = novo_nome
    favorito_selecionado['descricao'] = nova_descricao
    favorito_selecionado['preco'] = float(novo_preco)

    redis_client.set(f"favoritos:{session_id}", json.dumps(favoritos))

    print("O favorito foi atualizado no Redis com sucesso!")

    mycol_usuario.update_one(
        {"_id": ObjectId(session_id)},
        {"$set": {"favoritos": favoritos}}
    )
    print("O favorito foi sincronizado com o MongoDB.")