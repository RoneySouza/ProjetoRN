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
            print('-'*30)
            print('CADASTRO FINALIZADO'.center(30))
            print('-'*30)
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
            
                
def Pesquisar_Produtos(lista,lista_produtos):
    
    if lista == 3:
        print('PESQUISANDO PRODUTOS'.center(30))
        print('-'*30)
        try:
            pesq = int(input('Digite o Codigo do Produto q vc quer ver: '))
        except:
            print('digite uma opção valida')
            
        if 0 <= pesq < len(lista_produtos):
            produto = lista_produtos[pesq]
            print('~'*50)
            print(f'Nome: {produto["nome"]} Preço: R${produto["preco"]} Quantidade: {produto["Quantidade"]}kg')
            print('~'*50)
        else:
            print('Digite o Cod Correto')               
                
def editar_Produtos(editar,produtos):
    
    
    
    if editar == 4:
        print('~~'*10)
        print('EDITAR UM PRODUTO'.center(10))
        print('~~'*10)
        try:
            pesq =  str(input('Qual Produto Voce quer editar: ')).lower()
            produto_encontrado = False
        except:
            print('Escolha uma Opção valida!')
        
        for i in produtos:
            
            if pesq.lower() == i['nome'].lower():
                produto_encontrado = True
                print('-'*30)
                print(f'Editar o Prduto {i["nome"]}'.center(30))
                print('-'*30)
                
                print(f'Nome: {i["nome"]} Preço: {i["preco"]} Quantidade: {i["Quantidade"]}')
                
                try:
                    novonome = str(input('Novo Nome: ')).strip().lower()  
                except:
                    print('Digite o Valor Correto')
                try:        
                    novopreco = float(input('Novo Preço: '))   
                except:
                    print('Digite o Valor correto')
                try:        
                    novaquantidade = int(input('Nova Quantidade: '))  
                except:
                    print('Digite o Valor Correto')
                    
                try:    
                    att = str(input('Atualizar Produto: S/N ')).strip()
                except:
                    print('Dgite o Valor Correto')    
                if att not in "SsNn":
                    print('Escolha a Opçao Correta')
                elif att in 'Ss':
                    i["nome"] = novonome
                    i["preco"] = novopreco
                    i["Quantidade"] = novaquantidade
                    print('PRODUTO ATUALIZADO')
                    break
                       
                elif att in 'Nn':
                    print('PRODUTO NAO ATUALIZADO')
                    break          
                          
        if not produto_encontrado:
            print('PRODUTO NAO ECONTRADO')
                
                
                




    
                 
                 