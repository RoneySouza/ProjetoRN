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
                
def Pesquisar_Produtos(lista,lista_produtos=0):
    
    if lista == 3:
        print('PESQUISANDO PRODUTOS'.center(30))
        print('-'*30)
        while True:
            try:
                pesq = str(input('Digite o Nome do Produto q vc quer ver: ')).strip()
            except(ValueError,TypeError):
                print('digite uma opção valida')
                continue
            con_bd = ("SELECT * FROM produtos WHERE nome = %s ")
            cursor.execute(con_bd,(pesq,))
            produtos = cursor.fetchone()
                    
            if produtos is not None:
                print('~'*50)
                print(f'Nome: {produtos[1]} Preço: R${produtos[2]} Quantidade: {produtos[3]}kg')
                print('~'*50)
                break
            elif produtos == None:
                print('Esse Produto Nao existe')               
    
                
def editar_Produtos(editar,produto=0):
    
    
    
    if editar == 4:
        print('~~'*10)
        print('EDITAR UM PRODUTO'.center(10))
        print('~~'*10)
        try:
            pesq =  str(input('Qual ID Voce quer editar: ')).lower()
            print()
        except:
            print('Escolha uma Opção valida!')
            
        con_db = ("SELECT * FROM produtos WHERE id = %s ")
        cursor.execute(con_db,(pesq,))
        produtos = cursor.fetchone()
        
        if produtos is None:
            print('Produto Nao Econtrado')
            return
        
        print(f'Nome: {produtos[1]} Preço: {produtos[2]} Quantidade: {produtos[3]}')
        
        while True:
            
            while True:
                try:
                    novonome = str(input('Novo Nome: ')).strip().lower()  
                except:
                    print('Digite o Valor Correto')
                    continue
                if novonome.strip() == '':
                    print("Digite algum Nome")
                    continue    
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
                    print('Quantidade Alterada')
                    break
            try:    
                att = str(input('Atualizar Produto: S/N ')).strip()
            except:
                print('Dgite o Valor Correto')    
            if att not in "SsNn":
                print('Escolha a Opçao Correta')
            elif att in 'Ss':
                con_produtos = ("UPDATE produtos SET nome = %s, preco = %s, quantidade = %s WHERE id  = %s")
                valores = (novonome,novopreco,novaquantidade,pesq)
                cursor.execute(con_produtos,valores)
                conexao.commit()
                print('PRODUTO ATUALIZADO')
                break
                       
            elif att in 'Nn':
                print('PRODUTO NAO ATUALIZADO')
                break          
                
                
                
def excluir_Produtos(excluir,produto=0):
    
    if excluir == 5:
        print('-'*30)
        print('EXCLUIR PRODUTOS'.center(30))
        print('-'*30)
        try:                
            pesq = int(input('Qual Id do Produto Deseja Excluir: '))
            produtoencontrado = False
        except:
            print('Digite o Valor correto!!')
            
        pes_db = ("SELECT * FROM produtos WHERE id = %s ")
        cursor.execute(pes_db,(pesq,))
        produtos = cursor.fetchone()
        

        if produtos is None:
            print('PRODUTO NAO ENCONTRADO')
            return

        print('-'*50)
        print(f'Nome: {produtos[1]} Preço: R${produtos[2]} Quantidade: {produtos[3]}Kg')
        print('-'*50)
            
        while True:        
            try:
                apagar = str(input(f'Deseja Excluir Mesmo o {produtos[1]}: S/N '))
            except:
                print('Digite o Valor Correto')
                if apagar not in "SsNn":
                    print('Digite a opção Correta')        
            if apagar in "Ss":
                    del_db = ("DELETE FROM produtos WHERE id = %s")
                    cursor.execute(del_db,(pesq,))
                    conexao.commit()
                    
                    print(f'O Produto {produtos[1]} Foi Excluido')
                    break
            if apagar in 'Nn':
                    print(f'O produto {produtos[1]} nao foi Excluido')
                    break  
       
 
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