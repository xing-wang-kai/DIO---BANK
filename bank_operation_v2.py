# definindo schema de menu para sacar
import textwrap
from datetime import datetime

def main():
    
    saldo = 1
    LIMITE = 500
    extrato = []
    numero_de_saques = 0
    LIMITE_DE_SAQUE = 3
    contas = []
    usuarios = []
    AGENCIA = "BNC DO POVO"

    while True: 

        option = menu()

        if option == 'd':
            print("""
                
                Quanto você deseja Depositar?
                
                """)
            deposito = int(input("VALOR: "))
            saldo, extrato = depositar(
                                    saldo, 
                                    deposito, 
                                    extrato)

            continue

        if option == 's':
            print("""
                
                quanto você deseja sacar?
                
                """)
            saque = int(input("valor: "))

            saldo, extrato, numero_de_saques = sacar(
                saldo=saldo,
                valor=saque,
                extrato=extrato,
                limite_valor=LIMITE,
                numero_de_saques=numero_de_saques,
                quantidade_maxima_saque=LIMITE_DE_SAQUE
            )

            continue
    
        if option == 'e':
            saldo, extrato = print_extrato(saldo, extrato)

        if option == 'q':
            print("OBRIGADO PELA PREFERENCIA!")
            break
        
        if option == "nc":
            agencia = AGENCIA
            numero_conta = len(contas) + 1

            conta = criar_conta(agencia, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        if option == 'nu':
            usuarios = criar_usuario(usuarios)

        if option == 'lt':
            listar_contas(contas)
        continue

def depositar(saldo, valor, extrato, /):
    print(extrato)
    if valor <= 0:
        print("valor de depósito inválido, não é possivel depositar valores negativos")
                
    else:
        saldo += valor
        print(f"Deposito Realizado com sucesso no valor R$ {valor:.2f}, saldo atual R$ {saldo:.2f}")
        extrato.append(f"DATA: {datetime.now().strftime('%d-%m-%Y')}, Deposito no valor de R$ {valor:.2f} saldo atual R$ {saldo:.2f}")
        
    return saldo, extrato

def sacar(saldo, valor, extrato, limite_valor, numero_de_saques, quantidade_maxima_saque):
    if quantidade_maxima_saque <= numero_de_saques:
        print("limite diário ultrapassado")
        extrato.append(f"DATA: {datetime.now().strftime('%d-%m-%Y')}, tentativa de saque falha| numero de saque diário ultrapassado")

    elif valor > limite_valor:
        print(f"limite do saque é de R$ {limite_valor:.2f}")
        extrato.append(f"DATA: {datetime.now().strftime('%d-%m-%Y')}, tentativa de saque falha| ultrapssou limite diário")

    elif valor > saldo:
        print(f"Saldo insuficiente seu saldo é R$ {saldo:.2f}")
        extrato.append(f"DATA: {datetime.now().strftime('%d-%m-%Y')}, tentativa de saque falha| saldo insuficiente")

    else:
        saldo -= valor
        numero_de_saques += 1
        print("Saque realizado com sucesso.")
        extrato.append(f"DATA: {datetime.now().strftime('%d-%m-%Y')}, Saque no valor de {valor:.2f} saldo atual R$ {saldo:.2f}")
    return saldo, extrato, numero_de_saques

def print_extrato(saldo ,/, extrato):
    if saldo < 1.99:
        print("Saldo insufiente, valore do extrato R$ 1.99")
        
    else:
        saldo -= 1.99
        extrato.append(f"DATA: {datetime.now().strftime('%d-%m-%Y')}, imprimiu um extrato valor {1.99} saldo R$ {saldo:.2f}")
        print("""
            EXTRATO ATUAL
        """)
        for line in extrato:
            
            print(f"|--> {line}")
    return saldo, extrato

def menu():
    menu = """\033[31m
            DIGITE UMA OPÇÃO ABAIXO\033[0;0m
            |===========================|      
            |  \033[33m [ d ]\033[0;0m  \033[34m Depositar \033[0;0m      |
            |  \033[33m [ s ]\033[0;0m  \033[34m Saque \033[0;0m          |
            |  \033[33m [ e ]\033[0;0m  \033[34m Extrato \033[0;0m        |
            | --------------------------|
            |  \033[33m [ nc ]\033[0;0m \033[34m Nova conta \033[0;0m     |
            |  \033[33m [ lt ]\033[0;0m \033[34m Listar Conta \033[0;0m   |
            |  \033[33m [ nu ]\033[0;0m \033[34m novo usuário \033[0;0m   |
            |---------------------------| 
            |  \033[33m [ q ]\033[0;0m  \033[34m Sair \033[0;0m           |
            |===========================|


    """

    return input(textwrap.dedent(menu))

def criar_usuario(usuarios):

    cpf = input("insira o número do CPF (somente números):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("O usuário informado já existe!!!")
        return
    
    nome = input("agora informe o nome do novo usuário:")
    data_nascimento = input("agora informe a data de nascimento:")
    endereco = input("agora informe o endereço do usuário:")

    usuarios.append({'NOME': nome, "DATA_NASCIMENTO": data_nascimento, "ENDEREÇO": endereco, "CPF": cpf})
    print(f"USUARIO {nome} cadastrado com sucesso!!")
    return usuarios

def filtrar_usuario(cpf, usuarios):
    if len(usuarios) > 0:
        for usuario in usuarios:
            if usuario['CPF'] == cpf:
                return usuario

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("insira o número do CPF (somente números):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(" CONTA CRIADA COM SUCESSO!!")
        return {"AGENCIA":agencia, "NUMERO_CONTA": numero_conta, "USUARIO": usuario}
    
    print(f"CONTA NÃO CRIADA, não existe um usuário para o cpf {cpf}")

def listar_contas(contas):
    if len(contas) > 0:
        for conta in contas:
            print(f"""
                AGENCIA: {conta['AGENCIA']}
                NUMERO_DA_CONTA: {conta['NUMERO_CONTA']}
                USUARIO: {conta['USUARIO']}
                """
                )
   

if __name__ == "__main__":
    main()