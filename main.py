from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph

def reachable(g, start_node):
    if start_node not in g:
        return set()
    result = set()
    frontier = {start_node}
    while frontier:
        u = frontier.pop()
        if u in result:
            continue
        result.add(u)
        for v in g[u]:
            if v not in result:
                frontier.add(v)
    return result


def connected(g):
    if not g:
        return True
    start = next(iter(g))
    return len(reachable(g, start)) == len(g)

def n_components(g):
    seen = set()
    comps = 0
    for u in g:
        if u not in seen:
            R = reachable(g, u)
            seen |= R
            comps += 1
    return comps


