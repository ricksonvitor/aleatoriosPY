import shelve

colecar = shelve.open('CadastroAluno.db')
Alunos = {'nome' : ["rickson"], 'nota1' : [100], 'nota2' : [100], 'idade':[22] }
numAlunos = 1
Cod = str(input("Digite seu Código: "))
Senha= str(input("Digite sua Senha: "))

while True:
    if Cod == '700596' and Senha == 'admin123':
        print("LOGADO")
        break
    elif Cod != '700596' and Senha != 'admin123':
        print("ERROR: LONGIN OU SENHA DIGITADOS INCORRETAMENTE!!! ")
        
        
    

menu = '''

 ======================================
|           SUAP BETA                  |
|======================================|
| Para adicionar Aluno :            1  |
| Buscar Aluno         :            2  |
| Situação do Aluno    :            3  |
| Para fechar programa :            5  |
|                                      |
 ======================================

 Escolha uma Opção válida: '''

#adcicionar Aluno
def adicionar_aluno():
        numAlunos = 1
        if numAlunos < 100:
            nome = str(input(' informe nome do Aluno: ')).lower()
            if len(nome) >3:
                Alunos['nome'].append(nome)
            else:
                print("ENTRADA DE DADOS INVÁLIDA!!")
                while True:
                     print ("1 - tentar de novo")
                     print ("2 - Sair")
                     opcao = int(input("escolhe ai: "))
                     if opcao == 1:
                         nome = str(input('informe nome do Aluno: ')).lower()
                         if len(nome) >3:
                            Alunos['nome'].append(nome)
                            break
                         else:
                            return menu
                     elif (opcao == 2):
                         return menu
                     else:
                         print ("Opcao invalida!")
                    
               
            nota1 = int(input('informe nota 1: '))
            nota2 = int(input('informe nota 2: '))
            idade = int(input('informe idade do Aluno: '))
            if idade >= 18:
                Alunos['idade'].append(idade)
            else: 
                print("ENTRADA DE DADOS INVÁLIDA!!")
                while True:
                     print ("1 - tentar de novo")
                     print ("2 - Sair")
                     opcao = int(input("escolhe ai: "))
                     if opcao == 1:
                         idade = int(input('informe idade do Aluno: '))
                         if idade >= 18:
                            Alunos['idade'].append(idade)
                            break
                         else:
                            return menu
                     elif (opcao == 2):
                         return menu
                     else:
                         print ("Opcao invalida!")
                    

            
                 
                
            Alunos['nota1'].append(nota1)
            Alunos['nota2'].append(nota2)
            

            numAlunos = numAlunos + 1 
            print('\n PARABÉNS \n ALUNO adicionado com sucesso') 

        else:
            print('\n ERROR')
def buscar_aluno():
        aluno = input('digite nome do aluno: ').lower()
        situacao_aluno = aluno in Alunos['nome']

        if situacao_aluno == True:

            pos = Alunos['nome'].index(aluno)
            print('nome \t nota1 \t nota2 \t idade ')
            print('{0} \t{1} \t{2} \t{3} ' .format(Alunos['nome'][pos],Alunos['nota1'][pos],Alunos['nota2'][pos],Alunos['idade'][pos]))

        else:
            print('*OPS* \nPOR FAVOR verifique nome digitado e tente novamente!')

def situacao_aluno():
        nota_1B = int(input("Digite a nota do primeito Bimestre: "))
        nota_2B = int(input("Digite a nota do segundo  Bimestre: "))
        media1 = (nota_1B + nota_2B)/2
        if media1 >= 60:
            print("O Aluno está APROVADO")
        elif media1 < 60 and media1 > 30 :
            print(media1)
            recu = int(input("Digite nota da recuperação: "))
            mediafinal = (recu + media1)/2
            if mediafinal >= 60:
                print(mediafinal)
                print("PARABÉNS VOCÊ ESTÁ APROVADO")
            else:
                print(mediafinal)
                print("SENTIMOS MUITO, ANO QUE VEM TEM MAIS OTARU KKKK")
        else:
            print("o aluno esta REPROVADO")
            
        
while True:
            try:
                op = int(input(menu))
            except:
                print("\n Entrada inválida.")
                continue

            if   op == 1:
                adicionar_aluno()
            elif op == 2:
                buscar_aluno()
            elif op == 3:
                situacao_aluno()
            elif op == 5:
                print('\n\t Programa Finalizado!\n')
                break
            
            else:
                print("\n Opção inválida!")

else:
        print("ERROR! Digite novamente.")
colecar.close

