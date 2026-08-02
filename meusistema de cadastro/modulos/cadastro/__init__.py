from modulos.bancodedados.bd import cursor,conexao

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
                    ficha['quantidade'] = int(input('Quantidade kg: '))
                except:
                    print('Digite o valor correto')
                else:
                    break      
            
            con_bd = "INSERT INTO produtos(nome,quantidade,preco) VALUES(%s,%s,%s)"
            cursor.execute(con_bd,(ficha['nome'],ficha['preco'],ficha['quantidade'],))
            
            
            while True:
                try:
                    per_cad = str(input('CONFIRMAR CADASTRO: S/N '))
                except:
                    print('Digite uma opção valida')
                if per_cad not in "SsNn":
                    print('Digite a opção correta')
                if per_cad in 'Ss':
                    print('PRODUTO CADASTRADO COM SUCESSO')
                    conexao.commit()
                    # produtos.append(ficha.copy()) sem necessidade no momento
                    break 
                elif per_cad in 'Nn':
                    print('PRODUTO NAO CADASTRADO')
                    break        
            
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
       
            
def Listar_Produtos(text,listado=0):
    
    if text != 2:
        return
   
    if text == 2:
        print('PRODUTOS CADASTRADOS'.center(30))
        print('-'*30)
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        
        for c in produtos:
            print(f'ID {c[0]} Nome: {c[1]}', end=' ')
            print(f'Preço: R${c[2]:.2f}', end=' ')
            print(f'Peso: {c[3]}kg', end=' ')
            print()
            print('-'*30)           
                
def Pesquisar_Produtos(lista,lista_produtos):
    
    if lista == 3:
        print('PESQUISANDO PRODUTOS'.center(30))
        print('-'*30)
        while True:
            try:
                pesq = int(input('Digite o Codigo do Produto q vc quer ver: '))
            except(ValueError,TypeError):
                print('digite uma opção valida')
                continue
   
            if 0 <= pesq < len(lista_produtos):
                produto = lista_produtos[pesq]
                print('~'*50)
                print(f'Nome: {produto["nome"]} Preço: R${produto["preco"]} Quantidade: {produto["quantidade"]}kg')
                print('~'*50)
                break
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
                print(f'Editar o Produto {i["nome"]}'.center(30))
                print('-'*30)
                
                print(f'Nome: {i["nome"]} Preço: {i["preco"]} Quantidade: {i["quantidade"]}')
                while True:
                    try:
                        novonome = str(input('Novo Nome: ')).strip().lower()  
                    except:
                        print('Digite o Valor Correto')
                        continue
                    if novonome.strip() == '':
                        print("Digite algum Nome")
                    
                    else:
                        print('Nome Alterado')
                        break
                    
                while True:    
                    try:        
                        novopreco = float(input('Novo Preço: '))   
                    except(TypeError,ValueError):
                        print('Digite o Valor correto')
                        continue
                    else:
                        print('Preço Alterado')
                        break
                while True:    
                    try:        
                        novaquantidade = int(input('Nova Quantidade: '))  
                    except(TypeError,ValueError):
                        print('Digite o Valor Correto')
                        continue
                    else:
                        print('Quantidade Alterado')
                        break
                try:    
                    att = str(input('Atualizar Produto: S/N ')).strip()
                except:
                    print('Dgite o Valor Correto')    
                if att not in "SsNn":
                    print('Escolha a Opçao Correta')
                elif att in 'Ss':
                    i["nome"] = novonome
                    i["preco"] = novopreco
                    i["quantidade"] = novaquantidade
                    print('PRODUTO ATUALIZADO')
                    break
                       
                elif att in 'Nn':
                    print('PRODUTO NAO ATUALIZADO')
                    break          
                          
        if not produto_encontrado:
            print('PRODUTO NAO ECONTRADO')
                
                
def excluir_Produtos(excluir,produtos):
    
    if excluir == 5:
        print('-'*30)
        print('EXCLUIR PRODUTOS'.center(30))
        print('-'*30)
        try:                
            pesq = str(input('Qual Produto Voce Deseja Excluir: ')).lower().strip()
            produtoencontrado = False
        except:
            print('Digite o Valor correto!!')
            
        for pos,i in enumerate(produtos):

            if pesq.lower() == i['nome'].lower():
                produtoencontrado = True
                print('-'*50)
                print(f'Nome: {i["nome"]} Preço: R${i["preco"]} Quantidade: {i["quantidade"]}Kg')
                print('-'*50)
                
                try:
                    apagar = str(input(f'Deseja Excluir Mesmo o {i['nome']}: S/N '))
                except:
                    print('Digite o Valor Correto')
                if apagar not in "SsNn":
                    print('Digite a opção Correta')        
                if apagar in "Ss":
                    print(f'O Produto {i["nome"]} Foi Excluido')
                    produtos.remove(i)
                    break
                if apagar in 'Nn':
                    print(f'O produto {i['nome']} nao foi Excluido')
                    break  
        if not  produtoencontrado:
            print('PRODUTO NAO ENCONTRADO')
            return             
 
 
def menu(abrir):
    
    if abrir == 0:   
        print('~'*30)
        print('SISTEMA IN NATURE'.center(30))
        print('~'*30)
        while True:
            
            print("""
            MENU
        1 - CADASTRAR PRODUTOS
        2 - LISTA DE PRODUTOS
        3 - PESQUISAR PRODUTOS
        4 - EDITAR PRODUTOS
        5 - EXCLUIR PRODUTOS
        6 - SAIR
                """)
                
            try:
                num  = int(input('Qual Sua Escolha: '))
            except(ValueError,TypeError):
                print('Digite a opção correta')
            
            if num == 6:
                print('Até Logo')
                break
            if num not in range(1,7):
                print('Essa opçao nao Existe')
                continue
                    
            cadastrar_Produtos(num)
            Listar_Produtos(num,produtos)
            Pesquisar_Produtos(num,produtos)
            editar_Produtos(num,produtos)
            excluir_Produtos(num,produtos)                                   