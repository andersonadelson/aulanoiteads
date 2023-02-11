from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = ano_atual - ano_nascimento

if idade >= 16:
    print("Você pode votar este ano. Sua idade é: ", idade)
else:
    print("Você não pode votar este ano. Sua idade é: ", idade)