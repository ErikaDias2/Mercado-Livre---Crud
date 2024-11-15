import hashlib

def login(db, redis_client):
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    mycol = db.usuario
    usuario = mycol.find_one({"email": email})

    if usuario:
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()

        if senha_hash == usuario["senha"]:
            print(f"Bem-vindo(a), {usuario['nome']}!")
            session_id = str(usuario["_id"])
            session_timeout = 20
            redis_client.setex(session_id, session_timeout, usuario['nome'])
            
            return session_id
        else:
            print("Senha incorreta.")
    else:
        print("Usuário não encontrado.")
    return None