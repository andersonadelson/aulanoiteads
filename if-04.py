nome_aluno = input("Digite o nome do aluno(a): ")
nota_aluno = float(input("Digite a nota do aluno(a): "))

print("\nALUNO(A)       NOTA")
print("=========      =====")
print("{:<12}   {:<6.1f}".format(nome_aluno, nota_aluno))