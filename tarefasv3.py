# Lista que guarda todas as tarefas (cada tarefa é um dicionário)
tarefas = []
# Contador para gerar um id único para cada nova tarefa
proximo_id = 1


def adicionar(descricao):
    # 'global' permite alterar a variável proximo_id, que está fora da função
    global proximo_id
    # Cria um dicionário com os dados da tarefa e adiciona na lista
    tarefas.append({
        'id': proximo_id,
        'descricao': descricao,
        'concluida': False  # toda tarefa começa como não concluída
    })
    proximo_id += 1  # prepara o id da próxima tarefa

    # ANTES: print(f'Tarefa adicionada.')
    # AGORA: print('Tarefa adicionada.')
    # POR QUÊ: o 'f' serve para inserir variáveis dentro do texto com {}.
    # Como não há nenhuma variável aqui, o 'f' não fazia nada. Não dava erro,
    # mas era desnecessário e podia confundir quem lê.
    print('Tarefa adicionada.')


# FUNÇÃO NOVA: buscar
# POR QUÊ: antes, o código nunca usava o 'id' que guardava em cada tarefa.
# Esta função procura uma tarefa pelo id, e é ela que faz o id ter utilidade.
def buscar(id_tarefa):
    # Percorre a lista procurando a tarefa com o id informado
    for t in tarefas:
        if t['id'] == id_tarefa:
            return t  # achou: devolve o dicionário da tarefa
    return None  # não achou: devolve None (valor 'vazio')


def listar():
    # Lista vazia é considerada 'falsa', então entra aqui se não houver tarefas
    if not tarefas:
        print('Nenhuma tarefa.')
        return  # encerra a função sem continuar
    print('---- Tarefas ----')

    # ANTES: for i, t in enumerate(tarefas, 1):
    #            status = 'X' if t['concluida'] else 'O'
    #            print(f' {i}. [{status}] {t['descricao']}')
    # AGORA: percorre as tarefas direto e mostra o id real.
    # POR QUÊ (1): o enumerate gerava um número pela posição (1, 2, 3...).
    # Se você removesse a tarefa 1, a antiga 2 virava 1 e os números mudavam.
    # Com o id, cada tarefa mantém o mesmo número para sempre.
    # POR QUÊ (2): t['descricao'] com aspas simples dentro de uma f-string
    # também feita com aspas simples só funciona no Python 3.12+. Nas versões
    # anteriores dava SyntaxError. Para continuar usando só aspas simples e
    # funcionar em qualquer versão, guardo os valores em variáveis antes e
    # uso só o nome delas dentro da f-string.
    for t in tarefas:
        # 'X' se concluída, 'O' se pendente
        status = 'X' if t['concluida'] else 'O'
        numero = t['id']
        descricao = t['descricao']
        print(f' {numero}. [{status}] {descricao}')
    print()  # linha em branco para separar visualmente


def concluir(id_tarefa):
    # ANTES: concluir(numero)
    #            if 1 <= numero <= len(tarefas):
    #                tarefas[numero - 1]['concluida'] = True
    #                print('Tarefa concluída!')
    #            else:
    #                print('Número inválido.')
    # AGORA: busca a tarefa pelo id.
    # POR QUÊ: antes ele usava a posição na lista (numero - 1), então o 'id'
    # guardado em cada tarefa não servia para nada. Agora o número que o
    # usuário digita é o id que aparece na listagem.
    t = buscar(id_tarefa)  # procura a tarefa pelo id
    if t:  # se encontrou (None é considerado falso)
        t['concluida'] = True
        print('Tarefa concluída!')
    else:
        print('Número inválido.')


def remover(id_tarefa):
    # ANTES: remover(numero)
    #            if 1 <= numero <= len(tarefas):
    #                removida = tarefas.pop(numero - 1)
    #                print(f'Removida: {removida['descricao']}')
    #            else:
    #                print('Número inválido.')
    # AGORA: busca pelo id e remove o dicionário encontrado.
    # POR QUÊ: mesmo motivo do concluir (usar o id em vez da posição) e
    # também o mesmo cuidado com as aspas na f-string: o valor vai para uma
    # variável antes de ser usado.
    t = buscar(id_tarefa)  # procura a tarefa pelo id
    if t:
        descricao = t['descricao']
        tarefas.remove(t)  # remove o dicionário encontrado da lista
        print(f'Removida: {descricao}')
    else:
        print('Número inválido.')


print('---- Lista de tarefas ----')
# Loop infinito: o programa roda até o usuário escolher sair
while True:
    # Mostra o menu de opções
    print('[1] Adicionar [2] Listar [3] Concluir [4] Remover [0] Sair')
    # input lê o que o usuário digita; strip() remove espaços das pontas
    opcao = input('> ').strip()

    if opcao == '0':
        print('Até logo!')
        break  # sai do while e encerra o programa

    # ANTES: if opcao == '1':
    # AGORA: elif opcao == '1':
    # POR QUÊ: o 'if' começava uma segunda cadeia de condições, separada da
    # primeira (a do '0'). Funcionava porque o '0' já dá break, mas o certo
    # é deixar tudo numa cadeia só (if / elif / elif / else), para ficar claro
    # que só uma opção será executada.
    elif opcao == '1':
        desc = input('Descrição: ').strip()
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
            concluir(int(n))  # converte o texto para inteiro
    elif opcao == '4':
        listar()  # mostra a lista para o usuário escolher qual remover
        n = input('Número: ')
        if n.isdigit():
            remover(int(n))
    else:
        # Qualquer outra entrada cai aqui
        print('Opção inválida.')