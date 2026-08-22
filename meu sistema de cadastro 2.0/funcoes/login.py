from banco.bd import *
from hashlib import sha256
from pwinput import pwinput


class login:
    
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
            print(f'Usuario {usu} nao existe')
        else:
            print(f'usuario {usu} encontrado Login Bem Sucedido')    
        
            
        
        
