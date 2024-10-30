from login import login
from db.conexaoDb import redis_client, db

def MenuLogin(session_id):
    print("------------------------------------")
    print("| Seja bem vindo ao mercado livre! |")
    print("------------------------------------")
    print("************************************")
    print("| 1 - Login                        |")
    print("| 0 - Sair                         |")
    print("************************************")
    key = input("Digite a opção desejada: ")

    if key == '1':
        session_id = login(db, redis_client)
        return session_id
    elif key == '0':
        print("Saindo do sistema...")
        return None

    return session_id