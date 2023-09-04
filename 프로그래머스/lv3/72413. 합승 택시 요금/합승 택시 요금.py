def solution(n, s, a, b, fares):
    graph = [[1e9] * (n+1) for _ in range(n+1)]
    answer = 1e9
    for i in range(n+1):
        graph[i][i] = 0
    for i, j, fare in fares:
        graph[i][j] = fare
        graph[j][i] = fare

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for z in range(1, n+1):
        answer = min(answer, graph[s][z] + graph[z][a] + graph[z][b])
    return answer