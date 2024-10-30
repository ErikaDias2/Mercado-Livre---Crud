from bson.objectid import ObjectId
import json

def sincronizarCompras(db, redis_client, session_id):
    mycol_usuario = db.usuario

    usuario_logado = mycol_usuario.find_one({"_id": ObjectId(session_id)})
    
    if not usuario_logado:
        print("Usuário logado não encontrado no banco de dados.")
        return

    compras = usuario_logado.get('compras', [])
    if compras:
        chave_redis = f"compras:{usuario_logado['_id']}"
        redis_client.set(chave_redis, json.dumps(compras))
        print(f"Compras do usuário {usuario_logado['nome']} sincronizadas com o Redis.")
    else:
        print(f"O usuário {usuario_logado['nome']} não possui compras.")
