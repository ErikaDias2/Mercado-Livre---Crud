import hashlib

def CriarUsuario(db):
    mycol = db.usuario

    print("--------- Informações pessoais -----------")
    nome = input("Nome: ")
    email = input("Email: ")
    if mycol.find_one({"email": email}):
        print("Erro: Email já cadastrado!")
        return
    
    cpf = input("CPF: ")
    if mycol.find_one({"cpf": cpf}):
        print("Erro: CPF já cadastrado!")
        return
    
    senha = hashlib.sha256(input("Digite a senha: ").encode()).hexdigest()
    vendedor = input("É vendedor? (S/N)").lower() == "s"


    print("-------------- Endereço -----------------")
    enderecos = []
    key = "S"

    while key.upper() == "S":
        rua = input("Rua: ")
        numero = input("Número: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")

        endereco = {
            "rua": rua,
            "numero": numero,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        enderecos.append(endereco)
        key = input("Deseja cadastrar um novo endereço? (S/N): ")


    usuario = {
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "senha": senha,
        "vendas": vendedor,
        "endereco": enderecos,
        "favoritos": [],
        "compras": []
    }


    resultado = mycol.insert_one(usuario)
    print(f"Usuário inserido com o ID: {resultado.inserted_id}")
