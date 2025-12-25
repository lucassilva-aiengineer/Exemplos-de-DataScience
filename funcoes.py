
import random 
# Funcao de geracao de id 

def gerar_id():

    id_ = ""
    quantidade_numeros_gerada, quantidade_numeros_gerar = 0, 4
    while quantidade_numeros_gerada <= quantidade_numeros_gerar:

        numero = random.randint(0, 9)
        id_ += str(numero)

        quantidade_numeros_gerada += 1

    return id_


