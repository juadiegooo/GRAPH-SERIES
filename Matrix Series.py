import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Definir matrices de series, géneros, duración y estilo
series = np.array(["Los Simpson", "Padre de Familia", "Friends", "Rick y Morty", "The Big Bang Theory","Batman. La serie animada", "Bojack Horseman", "Breaking Bad", "Chernobyl", "Cowboy Bebop", "Expediente X", "Futurama", "Juego de Tronos", "Neon Genesis Evangelion", "The Office", "Lost", "South Park", "The Walking Dead", "Vikingos", "Caballero Luna", "The Boys", "Mr Robot", "Peaky Blinders"])
generos = np.array(["Comedia", "Humor negro", "Comedia", "Ciencia ficcion", "Comedia", "Aventura", "Psicologia", "Drama", "Documental", "Aventura", "Misterio", "Ciencia ficcion", "Aventura", "Misterio", "Comedia", "Misterio", "Humor negro", "Drama", "Documental", "Psicologia", "Drama", "Psicologia", "Documental"])
duracion = np.array(["Larga", "Larga", "Larga", "Corta", "Larga", "Corta", "Corta", "Larga", "Corta", "Corta", "Larga", "Corta", "Larga", "Corta", "Larga", "Corta", "Larga", "Larga", "Larga", "Corta", "Larga", "Corta", "Larga"])
estilo = np.array(["Animacion", "Animacion", "Live action", "Animacion", "Live action", "Animacion", "Animacion", "Live action", "Live action", "Anime", "Live action", "Animacion", "Live action", "Anime", "Live action", "Live action", "Animacion", "Live action", "Live action", "Live action", "Live action", "Live action", "Live action"])

# Solicitar al usuario el nombre de una serie
serie_usuario = input("Ingrese el nombre de una serie: ")

# Verificar si la serie ingresada por el usuario está en la lista
if serie_usuario in series:
    # Encontrar el índice de la serie ingresada por el usuario
    indice_usuario = np.where(series == serie_usuario)[0][0]

    # Crear una nueva matriz excluyendo la serie ingresada por el usuario
    matriz_series = np.delete(series, indice_usuario)
    matriz_generos = np.delete(generos, indice_usuario)
    matriz_duracion = np.delete(duracion, indice_usuario)
    matriz_estilo = np.delete(estilo, indice_usuario)

    # Crear la matriz de similitud
    matriz_similitud = np.zeros((3, len(matriz_series)), dtype=int)

    # Comparar las similitudes entre la serie del usuario y las demás series
    matriz_similitud[0, :] = (matriz_generos == generos[indice_usuario]).astype(int)
    matriz_similitud[1, :] = (matriz_duracion == duracion[indice_usuario]).astype(int)
    matriz_similitud[2, :] = (matriz_estilo == estilo[indice_usuario]).astype(int)

    # Calcular la puntuación de similitud para cada serie
    puntuacion_similitud = np.dot(matriz_similitud.T, np.array([1, 1, 1]))

    # Calcular el porcentaje de recomendación y redondear a dos decimales
    porcentaje_recomendacion = np.round((puntuacion_similitud / 3) * 100, 2)

    # Crear el grafo
    G = nx.Graph()
    G.add_node(serie_usuario, color="blue")

    # Bucle para agregar nodos y aristas al grafo
    for serie, porcentaje in zip(matriz_series, porcentaje_recomendacion):
    # Agregar nodos solo si el porcentaje de recomendación es mayor a 0
        if porcentaje > 0:
            G.add_node(serie, color="green" if porcentaje == 100 else "yellow")
            G.add_edge(serie_usuario, serie, weight=porcentaje)


    # Visualizar el grafo
    pos = nx.spring_layout(G, k =5.5)
    node_colors = [G.nodes[serie]['color'] for serie in G]
    edge_weights = [G[serie_usuario][serie]['weight'] for serie in G.neighbors(serie_usuario)]
    nx.draw(G, pos, with_labels=True, node_size=800, font_size=10, font_color='black', node_color=node_colors)
    edge_labels = {(serie_usuario, serie): f"{weight}%" for serie, weight in zip(G.neighbors(serie_usuario), edge_weights)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(f"Grafo de Recomendaciones para {serie_usuario}")
    plt.show()

else:
    print("La serie ingresada no está en la lista.")