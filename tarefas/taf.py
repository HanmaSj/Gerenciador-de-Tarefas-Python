# Desafio: Organizador de Tarefas
# Objetivo:
# Crie um programa em Python que permita ao usuário adicionar, visualizar, marcar como concluídas e excluir tarefas de uma lista.

# Requisitos:
# Menu interativo:

# O programa deve exibir opções numeradas para o usuário escolher:
def opcoes():
    print('1- Adicionar uma tarefa \n'
    '2- Exibir tarefas \n'
    '3- Marcar uma tarefa como concluída \n'
    '4- Excluir uma tarefa \n'
    '5- Sair\n')

# Adicionar tarefas
def add_tarefas():
    print("Adicione suas tarefas, separadas por vírgula:")
    tarefas_input = input("Digite as tarefas: ")
    novas_tarefas = [tarefa.strip() for tarefa in tarefas_input.split(',')]

    for tarefa in novas_tarefas:
        tarefas.append({'Tarefa': tarefa, 'concluida': False})

    print(f"{len(novas_tarefas)} tarefa(s) adicionada(s) com sucesso!\n")

# Exibir tarefas
def exibir_task():
    if not tarefas:
            print('Não à tarefas registradas.\n')
    else:
        print(f'Tarefas: ')
        for i, tarefa in enumerate(tarefas, start=1):
            status = '✔️' if tarefa['concluida'] else '❌'
            print(f'{i}. {tarefa['Tarefa']} [{status}]')
        print()

# Marcar tarefas como concluída
def task_feita():
    if not tarefas:  # Verifica se há tarefas antes de pedir para selecionar uma
        print('Não há tarefas para marcar como concluída.\n')
        return

    exibir_task()  # Exibe as tarefas, se houver

    try:
        feitas_input = input('Selecione os números das tarefas concluídas, separados por vírgula: ')
        feitas_indices = [int(i.strip()) for i in feitas_input.split(',')]

        concluidas = []
        for indice in feitas_indices:
            if 1 <= indice <= len(tarefas):
                tarefas[indice - 1]['concluida'] = True
                concluidas.append(indice)
            else:
                print(f'Número inválido: {indice}. Ignorando.\n')

        if concluidas:
            print(f"{len(concluidas)} tarefa(s) marcada(s) como concluída(s).")
        else:
            print('Nenhuma tarefa foi marcada como concluída.')

    except ValueError:
        print('Por favor, insira números válidos separados por vírgula.\n')

# Excluir tarefas
def excluir_task():
    if not tarefas:  # Verifica se há tarefas antes de tentar excluir
        print('Não há tarefas para excluir.\n')
        return

    exibir_task()  # Mostra a lista de tarefas para o usuário escolher

    try:
        excluir_input = input('Selecione os números das tarefas que deseja excluir, separados por vírgula: ')
        excluir_indices = [int(i.strip()) for i in excluir_input.split(',')]

        excluidas = []
        for indice in sorted(excluir_indices, reverse=True):
            if 1 <= indice <= len(tarefas):
                excluidas.append(tarefas.pop(indice - 1))
            else:
                print(f'Número inválido: {indice}. Ignorando.\n')

        if excluidas:
            print(f"{len(excluidas)} tarefa(s) excluída(s) com sucesso!")
        else:
            print('Nenhuma tarefa foi excluída.')

    except ValueError:
        print('Por favor, insira números válidos separados por vírgula.\n')




tarefas = []

try:
    while True:
        opcoes()
        menu = input('O que deseja fazer? \n')


        if menu == '1':
            add_tarefas()

        if menu == '2':
            exibir_task()

        if menu == '3':
            task_feita()

        if menu == '4':
            excluir_task()

        # Sair    
        if menu == '5':
            break
except:
    ...
