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

# Lembre - se Ciência de dados se trata estrair conhecimento de dados desorgânizado. 



# Agora vamos criar funções que repondem algumas perguntas. 

# Qual a quantidade de amigos que 1 id_ específico possui. 

# 1)

# Esta função conta o número de amigos que cada id possui 
def quantidade_amigos(usuario_dict):

    user_id = usuario_dict["id"]
    id_amigos = dicionario_amigos[user_id]

    return (user_id, len(id_amigos))


# dicionarios_users = [{"id": 1}]
# for dicionario in dicionarios_users:
#     print(dicionario["id"])

# Imprimindo a quantidade de amigos que o primeiro usuário possui. 
def quantidade_amigos_a():
    quantidade_amigos_indice_1 = quantidade_amigos(lista_usuarios[8])

    print(quantidade_amigos_indice_1)

# Agora eu vou somar a quantidade de conexões que  rede possui. 
# total_conexoes = sum((quantidade_amigos(usuario) for usuario in lista_usuarios)) 

# print("Possuimos um total de:",total_conexoes, "conexões.")


# Descobrindo o número de conexões de uma forma mais simples. 

def quantidade_conexoes():
    quantidade_conexoes = 0 

    for usuario in lista_usuarios:
        quantidade__amigos_usuario = quantidade_amigos(usuario)

        quantidade_conexoes += quantidade__amigos_usuario

    print(f"Quantidade de conexões que a nossa rede social possui: {quantidade_conexoes} conexões.")

    # 2) Quantidade média de conexões que cada usuário possui. 
    # Vamos descobrir outra informação interessante.

    # A quantidade total de conexões dividida pela quantidade de usuários. 

def quantidade_media_conexoes(): 

    pessoas = ["Mateus", "João"]
    quantidade_pessoas = len(pessoas)
    print("A quantidade de pessoas é: " + str(quantidade_pessoas))

    numero_usuarios = len(lista_usuarios)
    media_conexoes = quantidade_conexoes  / numero_usuarios 

    print("A quantidade média de conexões que cada usuário possui em nossa rede social é: " + str(media_conexoes)+ "conexões / usuários")

# Objetivo, extrair essas informações que extraimos da base de dados maior, treinar com um conjunto maior de dados, mais usuários isso é muito interessante. 


# Próximo desafio identificar o usuário que possui o maior número de amigos, depois tentar identificar o usuário que possui menos amigos. 

# Criando uma função que cria um ranking com as pessoas mais influentes da nossa rede social. 

dicionario_ranking = {}

# quantidade_usuarios_id = [] 
for usuario in lista_usuarios:

    tupla = quantidade_amigos(usuario)

    # quantidade_usuarios_id.append(tupla) 

    chave = tupla[0]
    quantidade_usuarios = tupla[1]

    dicionario_ranking[chave] = quantidade_usuarios 

# print(quantidade_usuarios_id)

# Vou pegar os índices das tuplas vou ordenar e exibir conforme a ordenação. 

# quantidade_usuarios_id.sort()

for id_ in range(0, 10):

    print(f"Usuário {id_}: {dicionario_ranking[id_]}")