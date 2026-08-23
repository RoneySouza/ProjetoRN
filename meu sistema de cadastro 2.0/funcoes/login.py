from banco.bd import *
from hashlib import sha256
from pwinput import pwinput


class Login:
    
    def __init__(self):
        self.__usuario = None
        self.__chave = None
    
    @property    
    def cadastrar_usuario(self):
        return self.__usuario,self.__chave
    
    @cadastrar_usuario.setter
    def cadastrar_usuario(self,dados):
        
        usu, chv = dados
        
        if isinstance(usu, str) and 8 <= len(usu) <= 10:  
            self.__usuario = usu
            print(f'Usuario Cadastrado')
            usuario_valido =  True   
        else:
            print (f'Digite um Usuario com 8 a 10 Characteres')
            usuario_valido = False    
        if isinstance(chv, str) and 8 <= len(chv) <= 10:
            chv = sha256(chv.encode('utf-8')).hexdigest()
            self.__chave = chv
            print(f'Senha Cadastrada')
            senha_valida = True
        else:
            print (f'Senha Fraca digite entre 8 a 10 Characters')
            senha_valida = False
        
        if usuario_valido and senha_valida:    
            try:
                con_bd = "INSERT INTO login(usuario, hash) VALUES(%s, %s)"
                cursor.execute(con_bd, (self.__usuario, self.__chave))
                conexao.commit()
                print('Usuário Cadastrado no Banco de Dados')
                return True
            except Exception as e:
                print(f'Erro ao cadastrar: {e}')
                return False
        else:
            print('Usuário não cadastrado')
            return False
            
            
    def verificar_login(self,usu,chv):
        
        chv = sha256(chv.encode('utf-8')).hexdigest()
        
        con_bd = ("SELECT * FROM login WHERE usuario = %s AND hash = %s ")
        cursor.execute(con_bd,(usu,chv))
        login = cursor.fetchone()
        
        
        if not isinstance(usu,str) and not isinstance(chv,str):
            print(f'tipo de valor nao aceito ')

        if login is None:
            print(f'Usuario {usu} nao existe\n')
        else:
            print(f'usuario {usu} encontrado Login Bem Sucedido\n')
            m =  Menu(usu)
            m.menu()
  
    def tela_login(self,title):
    
        print('-'*40)
        print(title.center(40))
        print('-'*40)
    
        print("""
            1 - LOGIN
            2 - CADASTRAR USUARIO
            3 - SAIR
            
            """)

        while True:
            
            sele = int(input('Opção: '))
    
            if sele == 1:
                print('-'*30)            
                print('LOGIN'.center(30))
                print('-'*30)
                
                while True:
                    try:
                        usu = str(input('Usuario: '))
                    except Exception(ValueError,TypeError):
                        return f'Esse Valor nao é valido'
                    try:
                        chv = str(pwinput('Senha: '))
                    except Exception(ValueError,TypeError):
                        return f"Esse valor nao é valido"
                    
                                
                    l = Login() 
                    l.verificar_login(usu,chv)
                    
                break    
            
            elif sele == 2:
                print('-'*30)
                print('CADASTRO'.center(30))
                print('-'*30)
                try:
                    usu = str(input('Usuario: '))
                except Exception(ValueError,TypeError):
                    return f'Esse valor nao é valido'
                try:    
                    chv = str(pwinput('Senha: '))
                except Exception(ValueError,TypeError):
                    return f'Esse valor nao é valido'
                
                l = Login()
                l.cadastrar_usuario = (usu,chv)
                
            
            
            elif sele == 3:
                print('-'*40)
                print (f'SITEMA ENCERRADO'.center(40))
                print('-'*40)
                break
            
            
            if sele not in range(1,3):
                print(f'Selecio a opção Correta')
                
      
      
      
class Menu:
    def __init__(self,usu):
        self.usuinfo = usu
    
    
            
    def menu(self):
    
        print('-'*40)
        print(f'BEM VINDO AO MENU'.center(40))
        print('-'*40)
        print(f'Usuario: {self.usuinfo}\n')
    
        print("""
            1 - PRODUTOS
            2 - CLIENTES
            3 - FORNECEDORES
            4 - VOLTAR
            \n
             """)
        
        while True:                
            sele = int(input('Opção: '))
            
            if isinstance(sele,int) or len(sele) <= 0:
                print('Digite um Valor Valido')
            
            match sele:
                
                case 1:
                    self.produtos()  
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case _:
                    print('opção invalida')
        
    def produtos(self):
        print('-'*40)
        print('MENU PRODUTOS'.center(40))
        print('-'*40)
        print(f'Usuario:{self.usuinfo}\n')
        
        print("""
              1 - LISTAR PRODUTOS
              2 - CADASTRAR PRODUTOS
              3 - EDITAR PRODUTOS
              4 - EXCLUIR PRODUTOS
              5 - VOLTAR
              \n
              """)
        
        cursor = conexao.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS produtos(id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(100) NOT NULL,preco DECIMAL(10,2) NOT NULL,quantidade int NOT NULL)")
        conexao.commit()
        
        while True:
            sele = int(int(input('Opção: ')))
            
            if not isinstance(sele,int) or sele < 0:
                print('Digite um Valor Valido')
            
            match sele:
                
                case 1:
                    self.Listar_produtos()
                case 2:
                    self.cadastrar_produtos()
                case 3:
                    self.editar_produtos()
                case 4:
                    self.excluir_produtos()
                case 5:
                    self.menu()       
                case _:
                    print('opção invalida')

    
                
    def Listar_produtos(self):
            print('-'*50)
            print('PRODUTOS CADASTRADOS'.center(50))
            print('-'*50)
            
            
            cursor.execute('SELECT * FROM produtos')
            produtos = cursor.fetchall()
            
            for c in produtos:
                print(f'ID: {c[0]} Nome {c[1]}', end=' ')
                print(f'Preço: {c[2]} Quantidade: {c[3]}')
                print()
                print('-'*50)
            
            
    def cadastrar_produtos(self):
            print('-'*50)
            print('CADASTRANDO PRODUTOS'.center(50))
            print('-'*50)
            
            while True:

                nome = str(input('Nome: ')).strip()
                
                if not isinstance(nome, str) and len(nome) == 0:
                    print('Digite um nome Valido')
                else:
                    print('preço inserido com sucesso')
                    break
            
            
            while True:
                
                try:
                    preco = int(input('Preço: '))
                except Exception(ValueError):
                    print('Digite um Valor Valido')
                    
                if not isinstance(preco, int) and len(preco) == 0:
                    print('Digite um nome Valido')
                else:
                    print(f'Preço Inserio com Sucesso')
                    break
                
            while True:
                
                try:
                    quantidade = int(input('Quantidade: '))
                except Exception(ValueError):
                    print('Digite um Valor Valido')
                    
                if not isinstance(quantidade, int):
                    print('Digite um valor valido')
                else:
                    print('Quantidade Inserido com sucesso')
                    break        
                            
            con_db = "INSERT INTO produtos(nome,preco,quantidade) VALUES(%s,%s,%s)"
            cursor.execute(con_db,(nome,preco,quantidade,))
            
            while True:
                confimar = str(input(f'COIFRMAR CADASTRO: S/N ')).strip()[0]
                
                if not isinstance(confimar, str) and len(confimar) == 0:
                    print('Escolha uma opção Valida!!!')
                if confimar in 'Ss':
                    print('PRODUTO CADASTRADO COM SUCESSO\n')
                    conexao.commit()
                    self.produtos()
                    break
                elif confimar in 'Nn':
                    print('PRODUTO NAO CADASTRADO\n')
                    self.produtos
                    break        
                

    def editar_produtos(self):
        print('-'*40)
        print('EDITAR PRODUTOS'.center(40))
        print('-'*40)
        
        cursor.execute('SELECT * FROM produtos')
        produtos =  cursor.fetchall()
        
        for c in produtos:
            print(f'ID: {c[0]} Nome {c[1]}', end=' ')
            print(f'Preço: {c[2]} Quantidade: {c[3]}')
            print()
            print('-'*50)
         
        try:
            pesq = int(input('Qual ID voce quer Editar: '))
        except ValueError:
            return f'Valor invalido'     

        con_db = ('SELECT * FROM produtos WHERE id = %s')
        cursor.execute(con_db,(pesq,))
        produtos = cursor.fetchone()
        
        if produtos is None:
            print('Esse Produto Nao Existe')
            self.editar_produtos()
            
            
        while True:    
            try:
                novonome = str(input('Novo Nome: '))    
            except ValueError:
                return f'Valor invalido'
            
            if not isinstance(novonome, str) or len(novonome) == 0:
                print('Digite um Nome Valido')
            else:
                print(f'Nome: {novonome} inserido com Sucesso')
                break
                       
        while True:    
            try:
                novopreco = int(input('Novo Preço: '))    
            except ValueError:
                return f'Valor invalido'
            
            if not isinstance(novopreco, int) or novopreco < 0:
                print('Digite um preço Valido')
            else:
                print(f'Preço R${novopreco:.2f} Inserido com Sucesso')
                break    
            
        while True:    
            try:
                novoquantidade = int(input('Nova Quantidade: '))    
            except ValueError:
                return f'Valor invalido'
            
            if not isinstance(novoquantidade, int) or novoquantidade < 0:
                print('Digite um Valor Valido')
            else:
                print(f'Quantidade {novoquantidade}kg Inserido Com Sucesso')    
                break
        while True:        
            try:
                att = str(input('Atualizar Produto: S/N ')).strip()[0]
            except ValueError:
                return f'Digite um valor valido'
            
            if not isinstance(att, int) or len(att) == 0:
                print('Escolha a opçao Valida')
            if att not in 'SsNn':
                print('Esta opção Nao é Valida')
            if att in 'Ss':
                con_produtos = ("UPDATE produtos SET nome = %s,preco = %s, quantidade = %s WHERE id = %s")
                valores = (novonome,novopreco,novoquantidade,pesq)
                cursor.execute(con_produtos,valores)
                conexao.commit()
                print(f'PRODUTO {novonome} ATUALIADO')
                self.produtos()
                break
                
            if att in 'Nn':
                print(f'PRODUTO {produtos[1]} NAO FOI ATUALIZADO')
                self.produtos()
                break            

    
    
    def excluir_produtos(self):
        print('-'*40)
        print('EXCLUIR PRODUTOS'.center(40))
        print('-'*40)
        
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        
        for c in produtos:
            print(f'ID: {c[0]} Nome {c[1]}', end=' ')
            print(f'Preço: {c[2]} Quantidade: {c[3]}')
            print()
            print('-'*50)
            
        while True: 
            try:    
                pesq  = int(input('Qual Produto Voce quer Excluir: '))
            except ValueError:
                print('Valor inserido Invalido')
            
            if not isinstance(pesq, int) or pesq < 0:
                print('Valor inserido é Invalido')
            
            # Buscar produto pelo ID
            con_db = "SELECT * FROM produtos WHERE id = %s"
            cursor.execute(con_db, (pesq,))
            produto = cursor.fetchone()
            
            if produto:
                print(f'Produto encontrado: {produto[1]}')
                break    
                    
            if produtos is None:
                print('Produto Não Econtrado')
        
                
        while True:               
            try:
                apagar = str(input('Deseja Realmente Apagar: S/N ')).strip()[0]
            except ValueError:
                return f'Valor inserido Invalido'
            if not isinstance(apagar, str) or len(apagar) == 0:
                print('Digite um valor Valido')  
            if apagar not in "SsNn":
                print('Escolha uma Opção Valida')
            if apagar in "Ss":
                print(f'PRODUTO {produto[1]} EXCLUIDO COM SUCESSO')
                del_db = ("DELETE FROM produtos WHERE id = %s")
                cursor.execute(del_db,(pesq,))
                conexao.commit()
                self.produtos()
                break
            if apagar in "Nn":
                print('Produto Não apagado')
                self.produtos()
                break    
    
class Clientes:
    
    def __init__(self):
        pass
    
    
class Fornecedores:
    def __init__(self):
        pass
    