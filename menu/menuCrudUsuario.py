from crudUsuario.CriarUsuario import CriarUsuario
from crudUsuario.LerUsuario import LerUsuario  
from crudUsuario.AtualizarUsuario import AtualizarUsuario
from crudUsuario.DeletarUsuario import DeletarUsuario
from db.conexaoDb import db

def MenuCrudUsuario():
    while True:
        print("| ----- Menu do Usuário ----- |")
        print("| 1 - Criar usuário           |")
        print("| 2 - Listar usuário          |")
        print("| 3 - Atualizar usuário       |")
        print("| 4 - Deletar usuário         |")
        print("| 0 - Voltar                  |")
        key = input("Digite a opção desejada: ")

        if key == '1':
            CriarUsuario(db)
        
        elif key == '2':
            LerUsuario(db)
        
        elif key == '3':
            AtualizarUsuario(db)

        elif key == '4':
            DeletarUsuario(db)

        elif key == '0':
            print("Voltando ao menu anterior...")
            return

        else:
            print("Opção inválida, por favor, tente novamente.")
