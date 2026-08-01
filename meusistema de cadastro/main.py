from modulos.cadastro import cadastrar_Produtos, Listar_Produtos,produtos,ficha,Pesquisar_Produtos,editar_Produtos  
  

print('-'*20)
print('SISTEMA IN NATURE'.center(20))
print('-'*20)

while True:
    
    print("""
    1 - Cadastrar Produtos
    2 - Listar Produtos
    3 - Pesquisar Produtos
    4 - Editar Produtos
    5 - sair             
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
    Pesquisar_Produtos(num,produtos)
    editar_Produtos(num,produtos)
    
    if num == 5:
        print('Até Logo')
        break
    
