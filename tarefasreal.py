tarefas = []
proximo_id = 1

def adicionar_tarefa(descricao):
    global proximo_id
    tarefas.append({
        "id": proximo_id,
        "descricao": descricao,
        "concluida": False
    })
    proximo_id += 1
    print(f"✓ Tarefa adicionada.")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa.")
        return
    print("─── Tarefas ───")
    for i, t in enumerate(tarefas, 1):
        status = "✓" if t["concluida"] else "○"
        print(f"  {i}. [{status}] {t['descricao']}")
    print()

def concluir_tarefa(numero):
    if 1 <= numero <= len(tarefas):
        tarefas[numero - 1]["concluida"] = True
        print("Tarefa concluída!")
    else:
        print("Número inválido.")

def remover_tarefa(numero):
    if 1 <= numero <= len(tarefas):
        removida = tarefas.pop(numero - 1)
        print(f"Removida: {removida['descricao']}")
    else:
        print("Número inválido.")

# Loop principal
print("=== Lista de Tarefas ===")
while True:
    print("[1] Adicionar  [2] Listar  [3] Concluir  [4] Remover  [0] Sair")
    opcao = input("→ ").strip()

    if opcao == "0":
        print("Até logo!")
        break
    elif opcao == "1":
        desc = input("Descrição: ").strip()
        if desc:
            adicionar_tarefa(desc)
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        listar_tarefas()
        n = input("Número: ")
        if n.isdigit():
            concluir_tarefa(int(n))
    elif opcao == "4":
        listar_tarefas()
        n = input("Número: ")
        if n.isdigit():
            remover_tarefa(int(n))
    else:
        print("Opção inválida.")