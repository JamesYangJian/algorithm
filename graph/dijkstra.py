import sys


def find_shortest_unhandled_node(node_list, costs):
    shortest = sys.maxint
    selected_node = None

    for node in node_list:
        if costs[node] < shortest:
            shortest = costs[node]
            selected_node = node

    node_list.remove(selected_node)
    return selected_node

def dijkstra(graph, start, end):
    costs = {}
    parent = {}
    node_list = []
    new_cost = 0

    for node in graph:
        for neighbour in graph[node]:
            if node == start:
                costs[neighbour] = graph[node][neighbour]
                parent[neighbour] = node
            else:
                costs[neighbour] = sys.maxint
                parent[neighbour] = ''

    for node in costs:
        node_list.insert(0, node)
    node_list.remove(end)


    while len(node_list) > 0:
        node = find_shortest_unhandled_node(node_list, costs)
        base_cost = costs[node]
        try:
            for neighbour in graph[node]:
                new_cost = base_cost + graph[node][neighbour]
                if new_cost < costs[neighbour]:
                    costs[neighbour] = new_cost
                    parent[neighbour] = node
        except Exception, e:
            pass

    print 'The shortest path length is %d' % costs[end]

    path = end
    p = parent[path]
    while p != start:
        path += ' <-- %s' %(p)
        p = parent[p]
    path += ' <-- Start'
    print 'The path is %s' % (path)
    return (costs, parent)

if __name__ == '__main__':
    start = 'Start'
    end = 'End'
    graph = {}
    graph['Start'] = {}
    graph['Start']['A'] = 3
    graph['Start']['B'] = 2
    graph['A'] = {}
    graph['A']['C'] = 5
    graph['A']['D'] = 2
    graph['B'] = {}
    graph['B']['C'] = 1
    graph['B']['D'] = 4
    graph['C'] = {}
    graph['C']['E'] = 4
    graph['C']['F'] = 3
    graph['D'] = {}
    graph['D']['E'] = 6
    graph['E'] = {}
    graph['E']['End'] = 4
    graph['F'] = {}
    graph['F']['E'] = 2
    graph['F']['G'] = 1
    graph['F']['End'] = 3

    costs, parent = dijkstra(graph, start, end) 

    #print costs
    #print parent
