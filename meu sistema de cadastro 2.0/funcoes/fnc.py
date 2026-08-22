from .login import *
from banco.bd import *
from pwinput import pwinput

def tela_login(title):
    
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
            usu = str(input('Usuario: '))
            chv = str(pwinput('Senha: '))
                        
            l = login() 
            l.verificar_login(usu,chv)    
        
        elif sele == 2:
            print('-'*30)
            print('CADASTRO'.center(30))
            print('-'*30)
            usu = str(input('Usuario: '))
            chv = str(pwinput('Senha: '))
            
            l = login()
            l.cadastrar_usuario = (usu,chv)
            
            
        else:
            print('Selecione a opção correta!!')
            
        
        