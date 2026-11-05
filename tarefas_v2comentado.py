# Lista que guarda todas as tarefas (cada tarefa é um dicionário)
tarefas = []
# Contador para gerar um id único para cada nova tarefa
proximo_id = 1

def adicionar(descricao):
    # "global" permite alterar a variável proximo_id, que está fora da função
    global proximo_id
    # Cria um dicionário com os dados da tarefa e adiciona na lista
    tarefas.append({
        "id": proximo_id,
        "descricao": descricao,
        "concluida": False # toda tarefa começa como não concluída
    })
    proximo_id += 1 # prepara o id da próxima tarefa
    print(f'Tarefa adicionada.')

def listar():
    # Lista vazia é considerada "falsa", então entra aqui se não houver tarefas
    if not tarefas:
        print("Nenhuma tarefa.")
        return      # encerra a função sem continuar
    print('---- Tarefas ----')
    # enumerate numera os itens começando em 1 (em vez de 0)
    for i, t in enumerate(tarefas, 1):
        # 'X' se concluída, 'O' se pendente
        status = 'X' if t['concluida'] else 'O'
        print(f' {i}. [{status}] {t['descricao']}')
    print()         # linha em branco para separar visualmente

def concluir(numero):
    # Verifica se o número está dentro do intervalo válido da lista
    if 1 <= numero <= len(tarefas):
        # Subtrai 1 porque o usuário vê a contagem a partir de 1, mas a lista começa em 0
        tarefas[numero - 1]['concluida'] = True 
        print('Tarefa concluída!')
    else:
        print('Número inválido.')

def remover(numero):
    # Mesma validação de intervalo da função concluir
    if 1 <= numero <= len(tarefas):
        # pop remove o item da posição e devolve o item removido
        removida = tarefas.pop(numero - 1)
        print(f'Removida: {removida['descricao']}')
    else:
        print("Número inválido.")

print('---- Lista de tarefas ----')
# Loop infinito: o programa roda até o usuário escolher sair
while True:
    # Mostra o menu de opções
    print('[1] Adicionar [2] Listar [3] Concluir [4] Remover [0] Sair')
    # input lê o que o usuário digita; strip() remove espaços das pontas
    opcao = input("> ").strip()

    if opcao == '0':
        print("Até logo!")
        break       # sai do while e encerra o programa
    if opcao == '1':
        desc = input("Descrição: ").strip()
        # Só adiciona se a descrição não estiver vazia
        if desc:
            adicionar(desc)
    elif opcao == '2':
        listar()
    elif opcao == '3':
        listar()  # mostra a lista para o usuário escolher qual concluir
        n = input('Número: ')
        # isdigit() garante que só tem dígitos, evitando erro no int()
        if n.isdigit():
            concluir(int(n)) # converte o texto para inteiro
    elif opcao == '4':
        listar() # mostra a lista para o usuário escolher qual remover
        n = input('Número: ')
        if n.isdigit():
            remover(int(n))
    else:
        # Qualquer outra entrada cai aqui
        print('Opção inválida.')
