def main():
    apresentacao()
    loop_menu()


def loop_menu():
    
    imprimi_menu()
    print("Qual opção deseja? ")
    menu = input("-> ")
    tratamento_menu(menu)
            
def tratamento_menu(menu):
    str_aceitas = ["0","1","2", "3", "4", "5","6", "7"]
    if menu in str_aceitas:
        menu = int(menu)

    elif menu not in str_aceitas:
        print("Só aceita número de 0 à 7 no programa!")
        numero_invalido()
    
    if menu >=1 and menu<=7:
        condicoes(menu)


    else:
        numero_invalido()

def numero_invalido():
    print("Insira um número válido!")
    menu = input("-> ")
    tratamento_menu(menu)


def condicoes(menu):
    if menu == 1:
        opcao_01()
        
    elif menu == 2:
        opcao_02()
        
    elif menu == 3:
        opcao_03()
        
    elif menu == 4:
        opcao_04()
        
    elif menu == 5:
        opcao_05()
        
    elif menu == 6:
        opcao_01()  

    elif menu == 7:
        opcao_07()
        
           
    
def apresentacao():
    print("----------------------  ") 
    print("-----Bem vindo!!------  ")
    print("----------------------\n")     

def imprimi_menu():
    print("----------------------")
    print("---------Menu!!-------")
    print("----------------------")
    print("(1)     Opção 01      ")
    print("(2)     Opção 02      ")
    print("(3)     Opção 03      ")
    print("(4)     Opção 04      ")
    print("(5)     Opção 05      ")
    print("(6)     Opção 06      ")
    print("(7) Sair do programa\n")

def retorno_menu():
    print("Deseja voltar ao menu? (S) (N)")
    voltar = input("-> ")
    if voltar == "s" or voltar == "S":
        loop_menu()
    else:
        encerramento()
        
    
def opcao_01():
    print("Testando opção 1")
    retorno_menu()

def opcao_02():
    print("Testando opção 2")
    retorno_menu()

def opcao_03():
    print("Testando opção 3")
    retorno_menu()

def opcao_04():
    print("Testando opção 4")
    retorno_menu()

def opcao_05():
    print("Testando opção 5")
    retorno_menu()

def opcao_06():
    print("Testando opção 6")
    retorno_menu()

def opcao_07():
    encerramento()

def encerramento():
    print("----------------------")
    print("Encerrando programa...")
    print("----------------------")


if __name__ == "__main__":
    main()


