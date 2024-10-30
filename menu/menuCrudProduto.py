from crudProduto.CriarProduto import CriarProduto
from crudProduto.LerProduto import LerProduto
from crudProduto.AtualizarProduto import AtualizarProduto
from crudProduto.DeletarProduto import DeletarProduto
from db.conexaoDb import db

def MenuCrudProduto():
    print("| ----- Menu do Produto ----- |")     
    print("| 1 - Criar produto           |")
    print("| 2 - Listar produto          |")
    print("| 3 - Atualizar produto       |")
    print("| 4 - Deletar produto         |")
    sub = input("Digite a opção desejada? (V para voltar) ")

    if sub == '1':
        CriarProduto(db)

    elif sub == '2':
        LerProduto(db)

    elif sub == '3':
        AtualizarProduto(db)
    
    elif sub == '4':
        DeletarProduto(db)