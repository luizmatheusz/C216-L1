alunos = []
mat = 1 # variável global para matrícula sequencial
    
# Cadastro dos alunos
def cadastrar_aluno():
    global mat
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o e-mail do aluno: ")
    curso = input("Digite o curso do aluno: ")
    matricula = curso + str(mat)
    mat = mat + 1
    alunos.append({"nome": nome, "email": email, "curso": curso, "matricula": matricula})
    print(f"Aluno {nome} cadastrado com sucesso!")

# Listagem dos alunos
def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}, E-mail: {aluno['email']}, Curso: {aluno['curso']}, Matrícula: {aluno['matricula']}")

# Atualizar um aluno
def atualizar_aluno():
    global mat
    nome = input("Digite o nome do aluno a ser atualizado: ")
    for aluno in alunos:
        if aluno["nome"] == nome:
            aluno["email"] = input("Digite o novo e-mail: ")
            aluno["curso"] = input("Digite o novo curso: ")
            aluno["matricula"] = aluno["curso"] + str(mat)
            mat = mat + 1
            print("Aluno atualizado com sucesso!")
            return
    print("Aluno não encontrado.")

# Remover um aluno
def remover_aluno():
    nome = input("Digite o nome do aluno a ser removido: ")
    for aluno in alunos:
        if aluno["nome"] == nome:
            alunos.remove(aluno)
            print("Aluno removido com sucesso!")
            return
    print("Aluno não encontrado.")

# Execução
def main():
    while True:
        print("\nMenu de Opções:")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Atualizar aluno")
        print("4. Remover aluno")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            atualizar_aluno()
        elif opcao == '4':
            remover_aluno()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()