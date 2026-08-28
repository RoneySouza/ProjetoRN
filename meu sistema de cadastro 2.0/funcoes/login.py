from banco.bd import *
from hashlib import sha256
from pwinput import pwinput
from abc import ABC,abstractmethod


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
        # self.menu(usu)
        
        if not isinstance(usu,str) and not isinstance(chv,str):
            print(f'tipo de valor nao aceito ')

        if login is None:
            print(f'Usuario {usu} nao existe\n')
        else:
            print(f'usuario {usu} encontrado Login Bem Sucedido\n')
            self.menu(usu)
    
    def menu(self,usu):
        
            print('-'*40)
            print(f'BEM VINDO AO MENU'.center(40))
            print('-'*40)
            print(f'Usuario: {usu}\n')
        
            print("""
                1 - PRODUTOS
                2 - CLIENTES
                3 - FORNECEDORES
                4 - VOLTAR
                \n
                 """)
            
            while True:
                try:                
                    sele = int(input('Opção: '))
                except ValueError,TypeError:
                    print('Insira um valor valido')
                    continue
    
                if isinstance(sele,int) or len(sele) <= 0:
                    print('Digite um Valor Valido')
                
                match sele:
                    
                    case 1:
                        t = Produtos()
                        t.produtos()  
                    case 2:
                        t = Clientes()
                        t.menu_clientes()
                    case 3:
                        pass
                    case 4:
                        pass
                    case _:
                        print('opção invalida')
  
  
            
  
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
            try:
                sele = int(input('Opção: '))
            except ValueError:
                print('Digite Apenas Numeros')
                continue
                
            # if sele.isdigit():  # Verifica se só tem números
            #     sele = int(sele)
            #     # Processa a opção
            # else:
            #     print('❌ Digite apenas números!')
            #     continue  # Volta ao menu    
                
                
                 
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
                      
class Menu(ABC):
    def __init__(self,tabela):
        super().__init__()
        self.tabela = tabela
        self.usuinfo = None
        self.config = self.get_config()
        
    def get_config(self):
        """cada classe filha deve sobreescrever este metodo"""
        return{
            'campos': [],
            'tipos' : [],
            'validacoes': []
        }    
        
        
        

    @abstractmethod    
    def listar(self):
                print('-'*50)
                print(f'{self.tabela.upper()} CADASTRADOS'.center(50))
                print('-'*50)
                config = self.config
                
                cursor.execute(f'SELECT * FROM {self.tabela}')
                registros = cursor.fetchall()
                
                for c in registros:
                    print(f'ID: {c[0]}', end=' ')
                    for i,campo in enumerate(config['campos']):
                        print(f'{campo} : {c[i+1]}',end=' ')
                        print()
                        print('-'*50)
                        
                print()
        
        
    @abstractmethod
    def pesquisar(self):

        print('-'*50)
        print(f' PESQUISAR {self.tabela.upper()}'.center(50))
        print('-'*50)
        
        while True:
            try:
                pesq = input(f'Digite o nome do {self.tabela}: ').strip()
                
                # VALIDAÇÕES
                if not pesq:
                    print(' Digite um nome para pesquisar!')
                    continue
                
                if len(pesq) < 2:
                    print(' Digite pelo menos 2 caracteres!')
                    continue
                
                # Se passou nas validações, sai do loop
                break
                
            except (ValueError, TypeError):
                print(' Valor inválido!')
                continue
        
        # BUSCA NO BANCO
        try:
            con_db = f"SELECT * FROM {self.tabela} WHERE nome LIKE %s"
            cursor.execute(con_db, (f'%{pesq}%',))
            registros = cursor.fetchall()
            
            if not registros:
                print(f' Nenhum {self.tabela} encontrado com o nome "{pesq}"!')
                return
            
            # MOSTRA RESULTADOS
            print('\n' + '='*50)
            print(f' RESULTADOS DA PESQUISA'.center(50))
            print('='*50)
            
            for registro in registros:
                print(f'ID: {registro[0]}')
                # Mostra os campos dinamicamente
                for i, campo in enumerate(self.config['campos']):
                    if i + 1 < len(registro):
                        print(f'{campo.capitalize()}: {registro[i+1]}')
                print('-'*50)
                
            print(f' {len(registros)} registro(s) encontrado(s)!')
            
        except Exception as e:
            print(f' Erro ao pesquisar: {e}')
        

    @abstractmethod
    def editar(self):
        print('-'*40)
        print(f'EDITAR {self.tabela.upper()}'.center(40))
        print('-'*40)
        config = self.config
        
        cursor.execute(f'SELECT * FROM {self.tabela}')
        registros =  cursor.fetchall()
        
        if not registros:
            print(f'Nenhum {self.tabela} foi encontrado!')
            return
        
        for c in registros:
            print(f'ID: {c[0]}', end=' ')
            for i,campo in enumerate(config['campos']):
                print(f'{campo}: {c[i+1]}',end=' ')
                print()
                print('-'*50)
         
        try:
            pesq = int(input('Qual ID voce quer Editar: '))
        except ValueError:
            return f'Valor invalido'     

        con_db = (f'SELECT * FROM {self.tabela} WHERE id = %s')
        cursor.execute(con_db,(pesq,))
        registro = cursor.fetchone()
        
        if registro is None:
            print(f'Esse {self.tabela} Nao Existe')
          
        novos_dados = []
        for i,campo in enumerate(config['campos']):
            valor_atual = registro[i+1]
            tipo = config['tipos'][i]  
            
            while True:
                try:
                    if tipo == 'int':
                        valor = input(f'Novo {campo} (atual: {valor_atual}): ')
                        valor = int(valor) if valor else valor_atual
                        if valor < 0:
                            print('❌ Não pode ser negativo')
                            continue
                    elif tipo == 'float':
                        valor = input(f'Novo {campo} (atual: {valor_atual}): ')
                        valor = float(valor) if valor else valor_atual
                        if valor < 0:
                            print('❌ Não pode ser negativo')
                            continue
                    else:  # string
                        valor = input(f'Novo {campo} (atual: {valor_atual}): ')
                        valor = valor if valor else valor_atual
                        if len(str(valor).strip()) == 0:
                            print('❌ Não pode ser vazio')
                            continue
                    
                    novos_dados.append(valor)
                    break
                except ValueError:
                    print(f'❌ Tipo inválido para {campo}')
        
        # Confirma
        confirmar = input('🔄 Atualizar? (S/N): ').strip().upper()[0]
        if confirmar == 'S':
            campos_sql = ', '.join([f'{campo} = %s' for campo in config['campos']])
            query = f"UPDATE {self.tabela} SET {campos_sql} WHERE id = %s"
            cursor.execute(query, novos_dados + [pesq])
            conexao.commit()
            print(f'✅ {self.tabela} atualizado!')  
       
            
                       
    @abstractmethod            
    def excluir(self):
        print('-'*40)
        print(f'EXCLUIR {self.tabela.upper()}'.center(40))
        print('-'*40)
        config = self.config
        
        # CORREÇÃO 1: Verifica se config existe
        if not config or 'campos' not in config:
            print('❌ Configuração inválida!')
            return
        
        cursor.execute(f"SELECT * FROM {self.tabela}")
        registros = cursor.fetchall()
        
        # CORREÇÃO 2: Verifica se há registros
        if not registros:
            print(f'❌ Nenhum {self.tabela} cadastrado!')
            return
        
        # CORREÇÃO 3: Mostra registros corretamente
        for c in registros:
            print(f'ID: {c[0]}', end=' ')
            # CORREÇÃO: Usa config['campos'] em vez de config
            for i, campo in enumerate(config['campos']):
                if i + 1 < len(c):
                    print(f'{campo}: {c[i+1]}', end=' ')
            print()
            print('-'*50)
        
        # CORREÇÃO 4: Remove o loop desnecessário de coleta de dados
        # (não precisa de novosDados para excluir)
        
        # Seleciona ID para excluir
        while True: 
            try:    
                pesq = int(input('🔍 Qual ID deseja excluir: '))
                if pesq <= 0:
                    print('❌ ID deve ser positivo!')
                    continue
                break
            except ValueError:
                print('❌ Digite um número válido!')
                continue
        
        # Busca o registro
        con_db = f"SELECT * FROM {self.tabela} WHERE id = %s"
        cursor.execute(con_db, (pesq,))
        registro = cursor.fetchone()
        
        if not registro:
            print(f'❌ {self.tabela.capitalize()} não encontrado!')
            return
        
        # Mostra o registro
        print('\n📋 Registro encontrado:')
        print(f'ID: {registro[0]}')
        for i, campo in enumerate(config['campos']):
            if i + 1 < len(registro):
                print(f'{campo.capitalize()}: {registro[i+1]}')
        
        # Confirma exclusão
        while True:               
            try:
                apagar = input('❓ Deseja realmente apagar? (S/N): ').strip().upper()[0]
                if apagar == 'S':
                    del_db = f"DELETE FROM {self.tabela} WHERE id = %s"
                    cursor.execute(del_db, (pesq,))
                    conexao.commit()
                    print(f'✅ {self.tabela.capitalize()} excluído com sucesso!')
                    break
                elif apagar == 'N':
                    print('❌ Exclusão cancelada!')
                    break
                else:
                    print('❌ Digite S ou N')
            except (ValueError, IndexError):
                print('❌ Digite S ou N')
                continue


class Produtos(Menu):
    def __init__(self):
        super().__init__('produtos')
        self.config = {
            'campos': ['nome', 'preco', 'quantidade'],
            'tipos': ['str', 'float', 'int']
        }
        

         
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
              5 - PESQUISAR PRODUTOS
              6 - VOLTAR
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
                    produtos = self.produtos
                    self.listar(produtos)
                case 2:
                    self.cadastrar_produtos()
                case 3:
                   produtos = self.produtos
                   self.editar(produtos)
                case 4:
                    produtos = self.produtos
                    self.excluir(produtos)
                case 5:
                    produtos = self.produtos
                    self.pesquisar(produtos)
                case 6:
                    self.menu()   
                           
                case _:
                    print('opção invalida')
     
                                             
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

    def pesquisar(self,produtos):
        return super().pesquisar()
    
    def listar(self,produtos):
        return super().listar()
        
    def editar(self,produtos):
        return super().editar()
    def excluir(self,produtos):
        return super().excluir()
    
class Clientes(Menu):
    
    def __init__(self):
        super().__init__('clientes')
        self.config = {
            'campos': ['nome', 'cpf', 'telefone', 'endereco'],
            'tipos': ['str', 'str', 'str', 'str']
        }
        # ... resto do código
        
    
        cursor = conexao.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS clientes(id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(100) NOT NULL,cpf VARCHAR(30) NOT NULL,telefone VARCHAR(30) NOT NULL, endereco VARCHAR(200))")
        conexao.commit()


    
    def menu_clientes(self):
        print('-'*40)
        print('CLIENTES'.center(40))
        print('-'*40)
        
        print("""
              1 - LISTA DE CLIENTES
              2 - CADASTRO DE CLIENTES
              3 - PESQUISAR CLIENTES
              4 - EDITAR CLIENTE
              5 - EXCLUIR CLIENTE
              6 - VOLTAR    
              """)
        
        while True:    
            try:
                opcao =  int(input('Opção: '))
            except ValueError:
                print('Valor inserido invalido')
                continue
            
            if opcao not in range(1,5):
                print('Escolha uma opção Valida')
            
            if not isinstance(opcao, int):
                print('Digite um Valor valido')
            
            match opcao:
                
                case 1:
                    clientes = self.menu_clientes
                    self.listar(clientes)
                case 2:
                    self.cadastrar_clientes()
                case 3:
                    clientes = self.menu_clientes
                    self.pesquisar(clientes)
                case 4:
                    clientes = self.menu_clientes
                    self.editar(clientes)
                case 5:
                    clientes = self.menu_clientes
                    self.excluir(clientes)
                case 6:
                    self.menu_clientes    
                    
                case _:
                    print('Escolha uma opção Valida')             
            
            
    def cadastrar_clientes(self):
        print('-'*50)
        print('CADASTRO DE CLIENTES'.center(50))
        print('-'*50)
        
        while True:
            try:
                nome = str(input('Nome Completo: '))
            except ValueError:
                print('Error digite o Valor correto')
                continue    
            
            if isinstance(nome, str) and 8 <= len(nome) <= 12:
                print('Nome Inserido Com sucesso!')
                break
            else:
                print('Nome invalido')
             
             
        while True:
            cpf = input('CPF (apenas números ou xxx.xxx.xxx-xx): ').strip()
            
            # Remove formatação
            cpf_limpo = cpf.replace('.', '').replace('-', '')
            
            # Verificações básicas
            if not cpf_limpo.isdigit():
                print('Erro: CPF deve conter apenas números')
                continue
            
            if len(cpf_limpo) != 11:
                print('Erro: CPF deve ter 11 dígitos')
                continue
            else:
            # Formata automaticamente
                cpf_formatado = f'{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}'
                print(f'CPF válido: {cpf_formatado}')
                break
         
        while True:
            
            try:
                tel = input('TEl: ')
            except(ValueError,TypeError):
                print(' Error:Valor digitado Incorreto')    
                continue
            
            if not tel.isdigit():
                print('Erro: Numero de telefone deve conter apenas numeros')
                
            if len(tel) != 11:
                print('Erro: Coloque o DD junto com o numero')
                                                         
            else:
                print('Telefone inserido com Sucesso')
                break
                
                
        while True:
            try:
                end = str(input('Cidade: '))
            except ValueError:
                print('Error digite o Valor correto')
                continue    
                    
            if isinstance(end, str) and 5 <= len(end) <= 20:
                print('Cidade Inserido Com sucesso!')
                break
            else:
                print('Nome invalido')
                
        while True:
            try:
                p = str(input('Cadastrar Cliente? S/N')).strip()[0] 
            except ValueError:
                print('Error valor digitado invalido')
                
            if p not in 'SsNn':
                print('Digite sim ou nao')
            if p in 'Ss':
                con_db = "INSERT INTO clientes(nome,cpf,telefone,endereco) VALUES(%s,%s,%s,%s)"
                cursor.execute(con_db,(nome,cpf,tel,end,))
            
                print(f'Cliente {nome} Cadastrado com Sucesso ')
                break
            if p in 'Nn':
                print('Cadastro Cancelado')    
                break    
                
    def listar(self,clientes):
        return super().listar()
    
    def pesquisar(self,clientes):
        return super().pesquisar()
    
    def editar(self,clientes):
        return super().editar()
    
    def excluir(self,clientes):
        return super().excluir()     
    
class Fornecedores(Menu):
    def __init__(self):
        super().__init__('fornecedores')
        self.config = {
            'campos': ['nome', 'cnpj', 'telefone', 'email', 'endereco'],
            'tipos': ['str', 'str', 'str', 'str', 'str']
        }
        
        
        
    