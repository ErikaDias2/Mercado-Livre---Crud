from menu.menuLogin import MenuLogin
from menu.menuPrincipal import MenuPrincipal

def main():
    session_id = None
    while True:
        session_id = MenuLogin(session_id)
        if session_id is None:
            print("Login falhou, tentando novamente...")
        else:
            break

    MenuPrincipal(session_id)


if __name__ == "__main__": 
    main()