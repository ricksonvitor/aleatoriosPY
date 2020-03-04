import shelve

colecpes = shelve.open('cole_pes.db')
Pessoas = {'nome' : [], 'idade' : [], 'cpf' : [], 'endereco':[] }
numPessoas = 0

menu = '''

 ======================================
|      Cadastro de Pessoas             |
|======================================|
| Para adicionar pessoa :            1 |
| Para pesquisar pessoa :            2 |
| Para atualizar info do pessoa :    3 |
| Para ver a coleção   :             4 |
| para remover pessoa   :            5 |
| Para fechar programa :             6 |
|                                      |
 ======================================

 Escolha uma Opção válida: '''

#adcicionar 
def adicionarpes():
    numPessoas = 0 
    if numPessoas < 100:
        nome = str(input(' informe nome: ')).lower()
        idade = str(input('informe idade: '))
        cpf = str(input('informe cpf: '))
        endereco = str(input('informe endereco: '))
 
        Pessoas['nome'].append(nome)
        Pessoas['idade'].append(idade)
        Pessoas['cpf'].append(cpf)
        Pessoas['endereco'].append(endereco)

        numPessoas = len(Pessoas) + 1 
        print('\n PARABÉNS \n Pessoa adicionada com sucesso') 

    else:
        print('\n numero maximo de Pessoas atingido')


#pesquisar 
def pesquisarpes():
    pes = input('digite nome da pessoa: ').lower()
    buscar = pes in Pessoas['nome']

    if buscar == True:

        pos = Pessoas['nome'].index(pes)
        print('nome \t idade \t cpf \t endereco')
        print('{0} \t{1} \t{2} \t{3} ' .format(Pessoas['nome'][pos],Pessoas['idade'][pos],Pessoas['cpf'][pos],Pessoas['endereco'][pos]))

    else:
        print('*OPS* \nPOR FAVOR verifique nome digitado e tente novamente!')
        
#atualizar 
def atualizarpes():
    pes = input('digite nome da pessoa: ').lower()
    buscar = pes in Pessoas['nome']

    if buscar == True:
        newnome = input ("Informe o novo nome da pessoa: ")
        newidade = input("Informe o nova idade : ")
        newcpf = input("Informe o novo cpf : ")
        newendereco = str(input("Informe o novo endereco: "))

        pos = Pessoas['nome'].index(pes)
        
        Pessoas['nome'][pos] = newnome
        Pessoas['idade'][pos] = newidade
        Pessoas['cpf'][pos] = newcpf
        Pessoas['endereco'][pos] = newendereco
        print('\n Dados Atualizados com sucesso!!!')

    else:
        print('*OPS* \n POR FAVOR verifique nome digitado e tente novamente!')
def vercolecao():
    print('nome \t idade \t cpf \t endereco')
    print()

    for i in range(numPessoas):
        print('{0} \t {1} \t {2} \t {3}'.format(Pessoas['nome'][i],Pessoas['idade'][i],Pessoas['cpf'][i],Pessoas['endereco'][i]))
def removerpes():
    pes = input('digite nome da pessoa: ').lower()
    buscar = pes in Pessoas['nome']

    if buscar == True:
        pos = Pessoas['nome'].index(pes)
        Pessoas['nome'].pop(pos)
        Pessoas['idade'].pop(pos)
        Pessoas['cpf'].pop(pos)
        Pessoas['endereco'].pop(pos)

        numPessoas = len(Pessoas) - 1 
        print('Removido com sucesso')
        
    else:
        print('*OPS* \n POR FAVOR verifique nome digitado e tente novamente!') 


while True:
    try:
        op = int(input(menu))
    except:
        print("\n Entrada inválida.")
        continue

    if op == 1:
        adicionarpes()
    elif op == 2:
        pesquisarpes()
    elif op == 3:
        atualizarpes()
    elif op == 4:
        vercolecao()
    elif op == 5:
        removerpes()
    elif op == 6:
        print('\n\t Programa Finalizado!\n')
        break
    
    else:
        print("\n Opção inválida!")



colecar.close    
