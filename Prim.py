# Criando infinito
INF = 9999999
# numero de vertices
N = 6

# matriz de adjacencia
G = [[0, 7, 8, 0, 0, 0],
     [7, 0, 3, 5, 0, 0],
     [8, 3, 0, 6, 3, 0],
     [0, 5, 6, 1, 2, 4],
     [0, 0, 3, 2, 0, 2],
     [0, 0, 0, 4, 2, 0]]

# variaveis de controle
selected_node = [0, 0, 0, 0, 0, 0]
no_edge = 0
selected_node[0] = True

print("Edge : Weight\n")
while (no_edge < N - 1):

    minimum = INF
    a = 0
    b = 0
    for m in range(N):  # Passando por todos os vertices

        if selected_node[m]:  # Se vertice ainda não está na arvore final

            for n in range(N):  # percorrer todos as conexões do vértice selecionado

                # se não está na arvore final e tem uma conexão
                if ((not selected_node[n]) and G[m][n]):

                    # se atual minimo for maior que aresta selecionada, troca aresta selecionada
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n

    print(str(chr(65+a)) + "-" + str(chr(65+b)) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1
