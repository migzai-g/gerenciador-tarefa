tarefas = []
proximo_id = 1

def adicionar(descricao):
    global proximo_id
    tarefas.append({
        "id": proximo_id,
        "descricao": descricao,
        "concluida": False
    })
    proximo_id += 1
    print(f'Tarefa adicionada.')

def listar():
    if not tarefas:
        print("Nenhuma tarefa.")
        return
    print('---- Tarefas ----')
    for i, t in enumerate(tarefas, 1):
        status = 'X' if t['concluida'] else 'O'
        print(f' {i}. [{status}] {t['descricao']}')
    print()

def concluir(numero):
    if 1 <= numero <= len(tarefas):
        tarefas[numero - 1]['concluida'] = True 
        print('Tarefa concluída!')
    else:
        print('Número inválido.')

def remover(numero):
    if 1 <= numero <= len(tarefas):
        removida = tarefas.pop(numero - 1)
        print(f'Removida: {removida['descricao']}')
    else:
        print("Número inválido.")

print('---- Lista de tarefas ----')
while True:
    print('[1] Adicionar [2] Listar [3] Concluir [4] Remover [0] Sair')
    opcao = input("> ").strip()

    if opcao == '0':
        print("Até logo!")
        break
    if opcao == '1':
        desc = input("Descrição: ").strip()
        if desc:
            adicionar(desc)
    elif opcao == '2':
        listar()
    elif opcao == '3':
        listar()
        n = input('Número: ')
        if n.isdigit():
            concluir(int(n))
    elif opcao == '4':
        listar()
        n = input('Número: ')
        if n.isdigit():
            remover(int(n))
    else:
        print('Opção inválida.')
