# Main formula, new_rank = damping_factor * M @ rank + (1-damping_factor) * teleport 
import numpy as np

def page_rank(graph, damping_factor=0.85, tol=1e-6):

    node_index = {node:i for i, node in enumerate(graph)}
    N = len(node_index)
    M = np.zeros((N,N))

    for node, links in graph.items():
        out_degree = len(links)
        for link in links:
            M[node_index[link], node_index[node]] = 1/out_degree

    rank = np.full(N, 1/N)
    teleport = np.full(N, 1/N)
    
    # Main formula code
    for _ in range(100):
        new_rank = damping_factor * M @ rank + (1-damping_factor) * teleport
        if np.linalg.norm(new_rank - rank, 1) < tol:
            break;
        rank = new_rank
    
    rank = rank/np.sum(rank)
    return {node:rank[i] for node, i in node_index.items()}



if __name__ == "__main__":
    graph = {
        'A':['B','C'],
        'B':['C'],
        'C':['A'],
        'D':['C']
    }

    ranks = page_rank(graph)

    for node, rank in ranks.items():
        print(f"{node} : {rank:.4f}")   
