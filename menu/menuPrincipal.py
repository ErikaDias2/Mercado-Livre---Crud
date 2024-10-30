from .menuCrudUsuario import MenuCrudUsuario
from .menuCrudProduto import MenuCrudProduto
from crudUsuario.AdicionarFavorito import AdicionarFavorito
from crudUsuario.RealizarCompra import RealizarCompra
from crudRedis.sincronizarFavoritos import sincronizarFavoritos
from crudRedis.AtualizarFavorito import AtualizarFavorito
from crudRedis.SincronizarCompra import sincronizarCompras
from crudRedis.AtualizarCompra import AtualizarCompra
from db.conexaoDb import db, redis_client
from .menuCrudUsuario import MenuCrudUsuario
from .menuCrudProduto import MenuCrudProduto

def MenuPrincipal(session_id):
    while True:
        print("*****************************")
        print("| 1 - CRUD Usuário          |")
        print("| 2 - CRUD Produto          |")
        print("| 3 - Comprar produto       |")
        print("| 4 - Favoritar produto     |")
        print("| 5 - Sincronizar favoritos |")
        print("| 6 - Atualizar favoritos   |")
        print("| 7 - Sincronizar compras   |")
        print("| 8 - Atualizar compras     |")
        print("| 0 - Logout                |")
        print("*****************************")

        key = input("Digite a opção desejada: ")
        if key == '1':
            MenuCrudUsuario()
        
        elif key == '2':
            MenuCrudProduto()
        
        elif key == '3':
            RealizarCompra(db, redis_client, session_id)
        
        elif key == '4':
            AdicionarFavorito(db, redis_client, session_id)
        
        elif key == '5':
            sincronizarFavoritos(db, redis_client, session_id)

        elif key == '6':
            AtualizarFavorito(db, redis_client, session_id)

        elif key == '7':
            sincronizarCompras(db, redis_client, session_id)

        elif key == '8':
            AtualizarCompra(db, redis_client, session_id)

        elif key == '0':
            redis_client.delete(session_id)
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida, por favor, tente novamente.")
