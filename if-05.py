print("Cadastro de Clientes")
print("0 - Fim")
print("1 - Inclui")
print("2 - Altera")
print("3 - Exclui")
print("4 - Consulta")

opcao = int(input("Escolha uma opção: "))

if opcao == 0:
    print("Fim do programa")
elif opcao == 1:
    print("Inclusão de cliente")
elif opcao == 2:
    print("Alteração de cliente")
elif opcao == 3:
    print("Exclusão de cliente")
elif opcao == 4:
    print("Consulta de cliente")
else:
    print("Opção inválida")
