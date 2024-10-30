from bson.objectid import ObjectId

def sincronizarFavoritos(db, redis_client, session_id):
    mycol_usuario = db.usuario

    usuario_logado = mycol_usuario.find_one({"_id": ObjectId(session_id)})
    
    if not usuario_logado:
        print("Usuário logado não encontrado no banco de dados.")
        return

    favoritos = usuario_logado.get('favoritos', [])
    
    if favoritos:
        chave_redis = f"favoritos:{usuario_logado['_id']}"
        redis_client.set(chave_redis, str(favoritos))
        print(f"Favoritos do usuário {usuario_logado['nome']} sincronizados com o Redis.")
    else:
        print(f"O usuário {usuario_logado['nome']} não possui favoritos.")
