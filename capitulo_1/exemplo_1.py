# Motivação impotética - Lista de amigos de pares de amizade na rede social datascientister

# Nós temos uma rede social e uma lista contendo dicionários com usuários, os seus nomes e ids. 
# E temos uma lista contendo tuplas que indicam pares de amizade. 


# Lista de usuários da datascientister. 

lista_usuarios = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"}, 
    {"id": 4, "name": "Thomas"},
    {"id": 5, "name": "Clive"}, 
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Davin"}, 
    {"id": 8, "name": "Kate"}, 
    {"id": 9, "name": "Klein"}
]


friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), 
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Tuplas são estruturas de dados imutáveis. 

# O objetivo é encontrar todos os amigos de cada um dos usuários da DataScientister 

# dicionario_amigos = {}

# for par in friendship_pairs:

#     if not par[0] in dicionario_amigos: 

#         dicionario_amigos[par[0]] = []

#         # dicionario_amigos[par[0]].append(par[1])

def amigos_users():

    dicionario_amigos = {}

    for par in friendship_pairs:


        if not str(par[0]) in dicionario_amigos: 

            dicionario_amigos[str(par[0])] = []

        dicionario_amigos[str(par[0])].append(par[1])


    return dicionario_amigos


def relatorio_amigos():
    dicionario_amigos = amigos_users()

    for user in dicionario_amigos: 

        print(f"Amigos do user: {user}: ")
        for item in dicionario_amigos[user]:

            print(item)


# Resposta do livro: 

# amizades = 
# def lista_amigos(lista_users):

dicionario_amigos = {}
for usuario in lista_usuarios:

    dicionario_amigos[usuario["id"]] = []

print(dicionario_amigos)

# Minha versão 

# for tupla in friendship_pairs:

#     for id_ in dicionario_amigos:

#         if tupla[0] == id_: 

#             dicionario_amigos[id_].append(tupla[1])


# Versão do livro: 
# i é o índice 0 da tupla o j é o índice 1 da tupla. 

# Esta é a alternativa correta. 

for i, j in friendship_pairs: 

    dicionario_amigos[i].append(j)
    dicionario_amigos[j].append(i)



print(dicionario_amigos) 

# Definindo o número total de cone

# Lembre -se 