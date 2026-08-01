from modulos.cadastro import cadastrar_Produtos, Listar_Produtos,produtos,ficha,Pesquisar_Produtos  
  

print('-'*20)
print('IN NATURE'.center(20))
print('-'*20)

while True:
    
    print("""
    1 - Cadastrar Produtos
    2 - Listar Produtos
    3 - Pesquisar Produtos
    4 - Sair             
            """)
    while True:
        
        try:
           num  = int(input('Qual Sua Escolha: '))
        except:
            print('Digite a opção correta')
        else:
            break    
              
    cadastrar_Produtos(num)
    Listar_Produtos(num,produtos)
    Pesquisar_Produtos(num)
    
    if num == 4:
        print('Até Logo')
        break
    
