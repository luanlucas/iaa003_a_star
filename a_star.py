import dists

# goal sempre sera 'bucharest'
def a_star(start, goal='Bucharest'):
    """
    Retorna uma lista com o caminho de start até 
    goal segundo o algoritmo A*
    """
    closed_list = []
    open_list = [start]
    came_from = {}
    
    g_score = {start: 0}
    f_score = {start: g_score[start] + dists.straight_line_dists_from_bucharest[start]}

    while open_list:
        current = min(open_list, key = lambda entry: f_score.get(entry))
        if current == goal:
            return reconstruct_path(came_from, goal)

        open_list.remove(current)
        closed_list.append(current)
        
        for adjacent_city in dists.dists[current]:
            neighbor_name = adjacent_city[0]
            if neighbor_name not in closed_list:
                neighbor_distance = adjacent_city[1]
                tentative_g_score = g_score.get(current) + neighbor_distance
                
                if neighbor_name not in open_list or tentative_g_score < g_score.get(neighbor_name):
                    came_from[neighbor_name] = current
                    g_score[neighbor_name] = tentative_g_score
                    f_score[neighbor_name] = tentative_g_score + dists.straight_line_dists_from_bucharest[neighbor_name]
                    
                    if neighbor_name not in open_list:
                        open_list.append(neighbor_name)
    
    return "Failure"

def reconstruct_path(came_from, goal):
    """
    Constrói o caminho percorrido pela função a_star
    """
    total_path = []
    for element in came_from:
        total_path.append(element)
    
    return total_path
