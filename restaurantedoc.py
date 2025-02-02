import os


#restaurantes=['Forno Mágico', 'Óleos Divinos']
#inserir dicionario-em outras linguagens chave valor
restaurantes=[{'nome':'Forno Mágico','categoria':'Pizzas','ativo': True},
              {'nome':'Rota','categoria':'Rodízio','ativo': False},
              {'nome':'Óleos Divinos','categoria':'Pastel','ativo': True},] 

def mostrar_subtitulo(texto):
    '''Essa função é resonsável por exibir o subtítulo
    '''
    os.system('clear')
    linha='*'*(len(texto))
    print(linha)
    print (texto)
    print(linha)
    print()

#2 declarando a função finalizar_app
def finalizar_app():
    
    mostrar_subtitulo()

def chamar_nome_do_app():
    print (''' 

        𝕽𝖊𝖘𝖙𝖆𝖚𝖗𝖆𝖓𝖙𝖊 𝕰𝖝𝖕𝖗𝖊𝖘𝖘𝖔 𝕬𝖓𝖓𝖆 𝕷𝖚𝖈𝖎𝖆

    ''')

def voltar_ao_menu_principal():
     input('\nDigite uma tecla para voltar ao menu principal')
     main()

# 12 criando opção_invalida
def opcao_invalida():
    '''Essa função é responsável por uma opção inválida/não cadastrada
    '''
    print ('opção invalida\n')
    #input('Digite uma tecla para voltar ao menu principal:')
    #main()
    voltar_ao_menu_principal()
    
def exibir_opcoes():
    print ("1 Cadastrar Restaurante")
    print ("2 Listar Restaurante")
    print ("3 Ativar Restaurente")
    print ("4 Sair\n")


def cadatrar_novo_restaurante():
    '''Essa função é responsável por cadastrar  um novo restaurante
    '''
    os.system('clear')
    nome_do_restaurante= input('Digite o nome do novo restaurante:')
    categoria=input(f'Digite a categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante={'nome':nome_do_restaurante, 'categoria':categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante}, foi cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes cadastrados
    '''
    mostrar_subtitulo('Listando os restaurantes')
    print(f"\n"'Nome do restaurante'.ljust(22),"Categoria".ljust(20),'Ativo'"\n")
    for restaurante in restaurantes:
     
       nome_restaurante=restaurante['nome']
       categoria=restaurante['categoria']
       ativo="ativado" if restaurante ['ativo'] else "Desativado"
       print(f'-{nome_restaurante.ljust(20)}  {categoria.ljust(20)}  {ativo}')

    voltar_ao_menu_principal()


def alterar_estado_restaurante():
    '''Essa função é responsável por alterar o estado do restaurante
    '''
    mostrar_subtitulo('Alternando o estado do restaurante')
    nome_restaurante=input('Digite o nome do restaurante que desejas alternar o estado: ')
    restaurante_encontrado=False

    for restaurante in restaurantes:
        if nome_restaurante==restaurante['nome']:
            restaurante_encontrado=True
            restaurante['ativo']=not restaurante['ativo']
            mensagem=f'O restaurante {nome_restaurante} foi ativado com sucesso'if restaurante['ativo'] else f'Restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')        
    voltar_ao_menu_principal()


#8 declarando a função opcao_digitada1
def escolher_opcao():
    '''Essa função é responsável por escolher uma opção
    '''
    
    try:
        opcao_digitada = (int(input("Escolha uma opção:  ")))
        print ("Você selecionou:",opcao_digitada, "\n")
        if(opcao_digitada==1):
            print("Você escolheu Cadastrar Restaurante\n")
            cadatrar_novo_restaurante()
            finalizar_app()
        elif(opcao_digitada==2):
           # print("Você escolheu Listar Restaurante\n") 
           listar_restaurantes()
           finalizar_app()
        elif(opcao_digitada==3):
            #mostrar_subtitulo("Voce escolheu Ativar Restaurante")
            alterar_estado_restaurante()
            finalizar_app()
        elif(opcao_digitada==4):
            # print('Voce escolheu sair do programa') 
             finalizar_app()
        #3 chamando a função finalizar_app 
        else:
            opcao_invalida()
    except:
        opcao_invalida()         
  
  #5 escrever a funçaõ main
def main():
    #10 clear
    os.system('clear')
    #6 chamar o nome do app
    chamar_nome_do_app()
    #7 chamar a escolha de opções
    exibir_opcoes()
    '''Essa função exibe opções para o usuário escolher
    '''
    #9 chamar a opção digitada
    escolher_opcao()

#4 criando a entrada através da variável main
if(__name__=='__main__'):
    main()
    '''Essa função é responsável pelo ambiente principal onde se executa o código
    '''