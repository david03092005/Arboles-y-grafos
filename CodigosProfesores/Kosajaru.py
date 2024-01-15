visited, disc, fin, time = None, None, None, None

def reverse(G):
    ans = [list() for _ in G]
    for u in range(len(G)):
        for v in G[u]:
            ans[v].append(u)
    return ans

def dfs(G, order):
    global visited, disc, fin, time
    ans = list()
    visited, disc, fin, time = list(), list(), list(), 0
    for _ in G:
        visited.append(0)
        disc.append(None)
        fin.append(None)
    for u in order:
        if visited[u] == 0:
            ans.append(list())
            dfs_visit(G, u, ans[-1])
    return ans

def dfs_visit(G, u, comp):
    global visited, disc, fin, time
    visited[u], disc[u], time = 1, time, time + 1
    comp.append(u)
    for v in G[u]:
        if visited[v] == 0:
            dfs_visit(G, v, comp)
    visited[u], fin[u], time = 2, time, time + 1

def main():
    G = [
        [1],
        [2, 4, 5],
        [3, 6],
        [2, 7],
        [0, 5],
        [6],
        [5, 7],
        [7]
    ]
    dfs(G, range(len(G)))
    order = [x for x in range(len(G))]  # No necesitas ordenar, se calcula en dfs_visit
    GT = reverse(G)
    scc = dfs(GT, order)
    print(scc)

main()
