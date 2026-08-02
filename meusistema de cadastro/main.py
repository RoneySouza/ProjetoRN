from modulos.cadastro import menu  
 
print('~'*30)  
print('BEM VINDO'.center(30))
print('~'*30)

print('Para Abrir o Menu Aperte 0')

while True:
    try:
        abrir = int(input('Abrir Menu: '))
    except(TypeError,ValueError):
        print('Digite o Valor Correto')
        continue
        

    if abrir != 0:
        print('Essa opçao nao existe')
    else:
        break    
menu(abrir)    
           
 
                  


    

    
