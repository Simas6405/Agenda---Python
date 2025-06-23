agenda = []
contato = []

contatos = 0

print('Menu:')
print('1: Inserir Contato na Agenda.')
print('2: Exibir Agenda.')
print('3: Consultar Contato na Agenda.')
print('4: Atualizar Dados do Contato na Agenda.')
print('5: Deletar Contato da Agenda.')
print('0: Sair.')

while True:
    try:

        opcao = int(input('Insira a opção desejada: '))

        if(opcao == 0):
            print('Finalizando Programa.')
            break

        elif(opcao == 1):
            nome = input('Insira o nome do Contato: ')
            email = input('Insira o Email do Contato: ')
            whatsapp = input('Insira o número de Whatsapp do Contato: ')

            contato = [nome, email, whatsapp]
            agenda.append(contato)
            contatos += 1

        elif(opcao == 2):
            if len(agenda) == 0:
                print('Nenhum contato na agenda.')
            else:
                print('Contatos da Agenda:')
                for contato in agenda:
                    print(f'Nome: {contato[0]}')
                    print(f'Email: {contato[1]}')
                    print(f'Número do Whatsapp: {contato[2]}')

        elif(opcao == 3):
            listaNome = [contato[0] for contato in agenda]
            nomePesquisa = input('Insira o Contato a ser pesquisado: ')
            indexPesquisaNome = listaNome.index(nomePesquisa)

            print(f'Pesquisando contato de: {nomePesquisa}')
            print(f'Nome: {agenda[indexPesquisaNome][0]}')
            print(f'Email: {agenda[indexPesquisaNome][1]}')
            print(f'Número do Whatsapp: {agenda[indexPesquisaNome][2]}')

        elif(opcao == 4):
            listaEmail = [contato[1] for contato in agenda]
            emailPesquisa = input('Insira o Email a ser pesquisado: ')
            indexPesquisaEmail = listaEmail.index(emailPesquisa)

            print(f'Modificando o Whatsapp do contato: {agenda[indexPesquisaEmail][0]}')
            whatsappNovo = input('Insira o novo Whatsapp: ')
            agenda[indexPesquisaEmail][2] = whatsappNovo

        elif(opcao == 5):
            print('Deletando Contato pelo Nome.')
            nomeDelete = input('Insira o nome do Contato a ser Deletado: ')
            indexPesquisaDel = listaNome.index(nomeDelete)

            agenda.remove(agenda[indexPesquisaDel])

            print('Contato deletado com êxito.')

        else:
            print('Erro na Entrada: Por Favor insira uma das Opções apresentadas!')


    except:
        print('Erro Entrada de Dados: Por Favor Tente novamente seguindo as instruções corretamente!')