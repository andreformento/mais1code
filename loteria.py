# docker run --rm -it \
#                 --entrypoint=python \
#                 python:2

def qtd_primos(sequencia):
	return 1 #todo calcular


def qtd_impar(sequencia):
	return 0 # todo calcular


# precisa usar a função str() para converter para string (texto)
# https://www.w3schools.com/python/ref_func_str.asp
# essa função deve ser utilizada para concatenar todos os métodos
# que você for criando para gerar a assinatura
def gera_assinatura(sequencia):
	return str(qtd_impar(sequencia)) + "i" + str(qtd_primos(sequencia)) + "p"


def main():
	numeros=[2,3,5,8,13]
	print(gera_assinatura(numeros))


# referencia https://realpython.com/python-main-function/
if __name__ == "__main__":
	main()

# exemplo da saida:
# 0i1p
