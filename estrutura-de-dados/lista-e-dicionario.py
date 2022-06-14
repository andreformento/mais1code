competidores = ["Joao", "Carlos", "Patricia", "Caio", "Leticia"]

def esta_na_lista(nome_para_procurar):
    if nome_para_procurar in competidores:
        return "esta na lista"
    else:
        return "nao esta na lista"

print(f"Joao {esta_na_lista('Joao')}")
print(f"Pedro {esta_na_lista('Pedro')}")


dicionario = dict({
    "Joao": "Competicao",
    "Carlos": "Desenvolvimento",
    "Patricia": "Competicao",
    "Caio": "Competicao",
    "Leticia": "Gestao",
})

def imprime_equipe(nome_para_procurar):
    if nome_para_procurar in dicionario:
        return dicionario[nome_para_procurar]
    else:
        return "nome nao existe"


print(f"Equipe de Joao {imprime_equipe('Joao')}")
print(f"Equipe de Carlos {imprime_equipe('Carlos')}")
print(f"Equipe de Pedro {imprime_equipe('Pedro')}")
