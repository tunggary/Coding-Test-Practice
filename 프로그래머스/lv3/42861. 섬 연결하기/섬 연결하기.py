def find_parent(x, parent):
    if parent[x] != x:
         parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union_parent(x, y, parent):
    x = find_parent(x, parent)
    y = find_parent(y, parent)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    for x, y, cost in sorted(costs, key=lambda x: x[2]):
        if find_parent(x, parent) != find_parent(y, parent):
            union_parent(x, y, parent)
            answer += cost
    return answer