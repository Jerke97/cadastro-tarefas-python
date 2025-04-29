tarefas = []

def exibir_menu():
    print("\n=== Menu ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append({"tarefa": tarefa, "concluida": False})
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    print("\n=== Tarefas ===")
    for i, t in enumerate(tarefas):
        status = "✔️" if t["concluida"] else "❌"
        print(f"{i + 1}. {t['tarefa']} - {status}")

def concluir_tarefa():
    listar_tarefas()
    i = int(input("Digite o número da tarefa para concluir: ")) - 1
    if 0 <= i < len(tarefas):
        tarefas[i]["concluida"] = True
        print("Tarefa marcada como concluída.")

def remover_tarefa():
    listar_tarefas()
    i = int(input("Digite o número da tarefa para remover: ")) - 1
    if 0 <= i < len(tarefas):
        tarefas.pop(i)
        print("Tarefa removida com sucesso.")

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        concluir_tarefa()
    elif opcao == "4":
        remover_tarefa()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")