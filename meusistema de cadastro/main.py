from modulos.cadastro import cadastrar_Produtos, Listar_Produtos,produtos  
  

print('-'*20)
print('IN NATURE'.center(20))
print('-'*20)

while True:
    
    print("""
    1 - Cadastrar Produtos
    2 - Listar Produtos
    3 - Sair             
            """)
    num  = int(input('Qual Sua Escolha: '))
    
    cadastrar_Produtos(num)
    Listar_Produtos(num,produtos)
    
    if num == 3:
        print('Até Logo')
        break
    
