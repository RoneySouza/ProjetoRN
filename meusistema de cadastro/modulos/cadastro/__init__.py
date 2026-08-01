produtos = []
ficha = {}    
def cadastrar_Produtos(text):
    
    while True:
        
        if text != 1:
            return        
          
        if text == 1:
            print('CADASTRANDO PRODUTOS'.center(30))
            print('-'*30)
            ficha['nome'] = str(input('Nome: '))
            
            while True:
                try :
                    ficha['preco'] = float(input('Preço R$: ')) 
                except(ValueError,TypeError):
                    print('Digite o valor correto')
                
                except(KeyboardInterrupt):
                    print('termine de digitar o valor correto')
                else:
                     break
                  
            while True:
                
                try:
                    ficha['Quantidade'] = int(input('Quantidade kg: '))
                except:
                    print('Digite o valor correto')
                else:
                    break      
            
            produtos.append(ficha.copy())
            
            while True:
                pergunta = str(input('Quer Cadastrar mais Produtos: S/N ')).strip()
                if pergunta not in 'SsNn':          
                        print('Escolha a Opçao correta')
                else:
                    break
        if pergunta in 'Nn':
            print('cadastro finalizado')
            break
       
            
def Listar_Produtos(text,listado):
    
    if text != 2:
        return
   
    if text == 2:
        print('PRODUTOS CADASTRADOS'.center(30))
        print('-'*30)   
        for pos,c in enumerate(listado):
            print(f'{pos} Nome: {c['nome']}', end=' ')
            print(f'Preço: R${c['preco']:.2f}', end=' ')
            print(f'Peso: {c['Quantidade']}kg', end=' ')
            print()
            print('-'*30)
            
                
def Pesquisar_Produtos(lista):
    
    if lista == 3:
        print('PESQUISANDO PRODUTOS'.center(30))
        print('-'*30)
        pesq = int(input('Digite o Codigo do Produto q vc quer ver: '))
        for p,c in enumerate(produtos):
            if pesq == p:
                print('~'*50)
                print(f'Nome: {c['nome']} Preço: R${c['preco']} Quantidade: {c['Quantidade']}kg')
                print('~'*50)
            else:
                print('Digite o Cod Correto')               
                
