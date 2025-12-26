# Vamos criar uma lista de usuários maior. 


from faker import Faker 
import random
import funcoes


faker = Faker('pt_BR')

def gerar_usuarios():

    lista_usuarios = []


    # dicionarios_adicionar = int(input("Indique a quantidade de dicionários que você gostaria de adicionar: "))
    usuarios_adicionados, usuarios_adicionar = 0, 100

    while usuarios_adicionados <= usuarios_adicionar:

        usuario = {"id": funcoes.gerar_id(), "name": faker.name()}

        lista_usuarios.append(usuario)

        usuarios_adicionados += 1 

    return lista_usuarios 



lista_users = gerar_usuarios()

# Usuários
# print(lista_users[0:10])


# Tenho uma lista de usuários. 

# Missão 1, gerar uma lista contendo os pares de amizade para os ids que já existem na minha rede social. 


def gerando_lista_ids(lista_usuarios):
    lista_ids = []
    for usuario in lista_usuarios: 

        lista_ids.append(usuario["id"])

    return lista_ids 
# print(lista_ids[: 5])


lista_id = gerando_lista_ids(lista_users)


def gerando_pares_amizades(lista_ids):
    pares_amizade = []
    for elemento in lista_ids:

        tupla_1 = elemento
        random.shuffle(pares_amizade)

        id_amigo = random.choice(lista_ids)

        while id_amigo == tupla_1: 

            id_amigo = random.choice(lista_ids)


        par_amizade = (tupla_1, id_amigo)

        pares_amizade.append(par_amizade)


    return pares_amizade


    # print(pares_amizade[0: 10])

# Criando a lista com os pares de amizade. 
friendship_pairs = gerando_pares_amizades(lista_id)

print(friendship_pairs[0: 5])


# Criando uma lista de ids da rede social com lista vazias 
# para futuramente armazenar os ids dos amigos. 

# A minha forma de resolver 

# dicionarios_amigos = {}

# for usuario in lista_users:

#     amigo = {usuario["id"]: []}

#     dicionarios_amigos.append(amigo)

    # dicionarios_amigos += amigo

# Utilizando a resposta do livro 

dicionario_amigos = {}

for usuario in lista_users:
    dicionario_amigos[usuario["id"]] = []


# Nós fazemos isto para que o índice 1 seja acrescentado como amigo do índice 2
# e que o índice 2 também seja acrescentado como amigo do índice 1. 


for tupla_indice_1, tupla_indice_2 in friendship_pairs:
    dicionario_amigos[tupla_indice_1].append(tupla_indice_2)
    dicionario_amigos[tupla_indice_2].append(tupla_indice_1)


# Vamos extrair mais conhecimento acerca dos nossos dados. 

# Vamos descobrir a quantidade de conexões que a nossa rede social possui. 

def quantidade_amigos(user):
    id_user = user["id"]
    amigos = dicionario_amigos[id_user]
    quantidade_amigos = len(amigos)
    return quantidade_amigos 

def quantidade_conexoes():
    numero_conexoes = 0 

    for amigo in lista_users: 

        quantidade_amigos_user = quantidade_amigos(amigo)

        numero_conexoes += quantidade_amigos_user 

    # print("Quantidade total conexões:",numero_conexoes) 

    return numero_conexoes

# Definindo a quantidade média de conexões que cada usuário possui. 
# quantidade total de conexões dividida pela quantidade de usuário, nos 
# retorna o resultado de quantidade média de amigos que um usuário possui. 

def quantidade_media_conexoes():

    total_users = len(lista_users)
    total_conexoes = quantidade_conexoes()

    quantidade_media = total_conexoes / total_users 

    return quantidade_media

media_amigos = quantidade_media_conexoes()

print("A quantidade média de conexões:", media_amigos)

# Um pequeno relatório. 

def relatorio():

    print(f"""Número usuários: {len(lista_users)}
Total conexões: {}""")
# print(dicionario_amigos)