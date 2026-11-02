def adicionar_tarefa(tarefas, descricao):
    nova = {'descricao': descricao, 'concluida': False}
    tarefas.append(nova)

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa.")
    for pos, tarefa in enumerate(tarefas):
        if tarefa['concluida']:
            status = '[X]'
        else:
            status = '[ ]'
        print(f'{pos + 1} - {status} {tarefa['descricao']}')

def concluir_tarefa(tarefas, numero):
    posicao = numero -1
    tarefa = tarefas[posicao]
    tarefa['concluida'] = True 

def remover_tarefa(tarefas, numero):
    posicao = numero -1
    tarefas.pop(posicao)


tarefas = []

while True:
    opcao = input('[1] Adicionar  [2] Listar  [3] Concluir  [4] Remover  [5] Sair\n')
    if opcao == '1':
        texto = input('Digite a Tarefa: ')
        adicionar_tarefa(tarefas, texto)
    elif opcao == '2':
        listar_tarefas(tarefas)
    elif opcao == '3':
        num = int(input('Tarefa completa: '))
        concluir_tarefa(tarefas, num)
    elif opcao == '4':
        num = int(input('Tarefa a remover: '))
        remover_tarefa(tarefas, num)
    elif opcao == '5':
        break
    else:
        print("Opção inválida.")