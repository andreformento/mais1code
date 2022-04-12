# docker run --rm \
#            -v $(pwd)/loteria.py:/app/loteria.py \
#            --entrypoint=python \
#            python:2 \
#            /app/loteria.py


def eh_primo(numero):
    if numero==2 or numero==3:
        return True
    for i in range(3, int(numero**0.5)+1, 2):
        print(int(numero**0.5)+1)
        if numero%i==0:
            return False
    return True


def qtd_primos(sequencia):
    primos = 0
    for numero in sequencia:
        if eh_primo(numero):
            primos+=1
    return primos

def qtd_impar(sequencia):
    impares=0
    for numero in sequencia:
        if numero%2 != 0:
            impares+=1
    return impares

# precisa usar a funcao str() para converter para string (texto)
# https://www.w3schools.com/python/ref_func_str.asp
# essa funcao deve ser utilizada para concatenar todos os metodos
# que voce for criando para gerar a assinatura
def gera_assinatura(sequencia):
    return str(qtd_impar(sequencia)) + "i" + str(qtd_primos(sequencia)) + "p"


def main():
    print("2" + str(eh_primo(2)))
    print("3" + str(eh_primo(3)))
    print("4" + str(eh_primo(4)))
    print("5" + str(eh_primo(5)))

    numeros=[2,3,5,8,13]
    print(gera_assinatura(numeros))


# referencia https://realpython.com/python-main-function/
if __name__ == "__main__":
    main()

# exemplo da saida:
# 0i1p
