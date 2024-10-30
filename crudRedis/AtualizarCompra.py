from bson.objectid import ObjectId
from datetime import datetime
import json

def AtualizarCompra(db, redis_client, session_id):
    mycol_usuario = db.usuario

    usuario_logado_nome = redis_client.get(session_id)
    if not usuario_logado_nome:
        print("Nenhum usuário logado. Faça o login primeiro.")
        return

    compras_json = redis_client.get(f"compras:{session_id}")
    compras = json.loads(compras_json) if compras_json else []

    if not compras:
        print("Nenhuma compra encontrada.")
        return

    print("-------- Compras Disponíveis --------")
    for i, compra in enumerate(compras):
        print(f"{i + 1}. Nome: {compra['nome']}")
        print(f"   Preço: R${compra['preco']}")
        print(f"   Quantidade: {compra['quantidade']}")
        print(f"   Data: {compra['data']}")
        print("-" * 40)

    escolha_compra = int(input("Selecione o número da compra que deseja atualizar: ")) - 1
    if escolha_compra < 0 or escolha_compra >= len(compras):
        print("Seleção de compra inválida. Tente novamente.")
        return

    compra_selecionada = compras[escolha_compra]

    nova_quantidade = input(f"Informe a nova quantidade (atual: {compra_selecionada['quantidade']}): ")
    if nova_quantidade:
        nova_quantidade = int(nova_quantidade)
    else:
        nova_quantidade = compra_selecionada['quantidade']

    if nova_quantidade <= 0:
        print("Quantidade inválida.")
        return

    compra_selecionada['quantidade'] = nova_quantidade
    compra_selecionada['data'] = datetime.now().strftime("%Y-%m-%d")

    redis_client.set(f"compras:{session_id}", json.dumps(compras))

    print("A compra foi atualizada no Redis com sucesso!")

    mycol_usuario.update_one(
        {"_id": ObjectId(session_id)},
        {"$set": {"compras": compras}}
    )
    print("A compra foi sincronizada com o MongoDB.")