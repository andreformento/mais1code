def imprime_numeros_em_uma_linha(limite):
    todos_os_numeros = range(limite)
    linha = ""
    for numero_atual in todos_os_numeros:
        linha = f"{linha} {limite}"
    print(linha)

def imprime_linhas(limite):
    todos_os_numeros = range(limite+1)
    for numero_atual in todos_os_numeros:
        imprime_numeros_em_uma_linha(numero_atual)

print("primeiro exemplo")
imprime_numeros_em_uma_linha(3)

print("segundo exemplo")
imprime_linhas(5)
