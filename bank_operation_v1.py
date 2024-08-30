# definindo schema de menu para sacar

from datetime import datetime

menu = """\033[31m
        DIGITE UMA OPÇÃO ABAIXO\033[0;0m
        
    \033[33m [ d ]\033[0;0m \033[34m Depositar \033[0;0m
    \033[33m [ s ]\033[0;0m \033[34m Saque \033[0;0m
    \033[33m [ e ]\033[0;0m \033[34m Extrato \033[0;0m
    \033[33m [ q ]\033[0;0m \033[34m Sair \033[0;0m


"""


saldo = 1
LIMITE = 500
extrato = []
numero_de_saques = 0
LIMITE_DE_SAQUE = 3

while True: 

    print("""
            EXTRATO ATUAL
""")
    for line in extrato:
         
         print(line)

    option = input(menu)

    if option == 'd':
        print("""
              
              Quanto você deseja Depositar?
              
              """)
        deposito = int(input("VALOR: "))

        saldo += deposito
        print(f"Deposito Realizado com sucesso no valor {deposito}, saldo atual R$ {saldo:.2f}")
        extrato.append(f"DATA: {datetime.now().strftime('%d-%m-%Y')}, Deposito no valor de {deposito} saldo atual R$ {saldo:.2f}")
        continue

    if option == 's':
        print("""
              
              quanto você deseja sacar?
              
              """)
        saque = int(input("valor: "))

        if LIMITE_DE_SAQUE <= numero_de_saques:
            print("limite diário ultrapassado")
            extrato.append(f"DATA: {datetime.now().strftime('%d-%m-%Y')}, tentativa de saque falha| numero de saque diário ultrapassado")

            continue

        else:
            if saque > LIMITE:
                print(f"limite do saque é de {LIMITE}")
                extrato.append(f"DATA: {datetime.now().strftime('%d-%m-%Y')}, tentativa de saque falha| ultrapssou limite diário")
 
                continue

            if saque > saldo:
                print(f"Saldo insuficiente seu saldo é R$ {saldo:.2f}")
                extrato.append(f"DATA: {datetime.now().strftime('%d-%m-%Y')}, tentativa de saque falha| saldo insuficiente")
 
                continue
        
            else:
                saldo -= saque
                numero_de_saques += 1
                print("Saque realizado com sucesso.")
                extrato.append(f"DATA: {datetime.now().strftime('%d-%m-%Y')}, Saque no valor de {saque} saldo atual R$ {saldo:.2f}")

                continue
 
    if option == 'e':
        if saldo < 1.99:
            print("Saldo insufiente, valore do extrato R$ 1.99")
            continue
        else:
            saldo -= 1.99
            extrato.append(f"DATA: {datetime.now().strftime('%d-%m-%Y')}, imprimiu um extrato valor {1.99} saldo R$ {saldo:.2f}")
            print("""
                EXTRATO ATUAL
            """)
            for line in extrato:
                
                print(line)
            continue

    if option == 'q':
        print("OBRIGADO PELA PREFERENCIA!")
        break
    continue