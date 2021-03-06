"""
    Created by Mustafa Sencer Özcan on 19.05.2020.

    So when to use DFS over A*, when to use Dijkstra over A* to find the shortest paths ?
    We can summarise this as below-

    1) One source and One Destination-
    → Use A* Search Algorithm (For Unweighted as well as Weighted Graphs)

    2) One Source, All Destination –
    → Use BFS (For Unweighted Graphs)
    → Use Dijkstra (For Weighted Graphs without negative weights)
    → Use Bellman Ford (For Weighted Graphs with negative weights)

    3) Between every pair of nodes-
    → Floyd-Warshall
    → Johnson’s Algorithm
"""
