def find_neighbors(sub_population, org_index):
    org_row = org_index[0]
    org_column = org_index[1]
    neighbors = [sub_population[org_row][org_column-(len(sub_population)+1)],
                 sub_population[org_row][org_column-(len(sub_population)-1)],
                 sub_population[org_row-(len(sub_population+1)][org_column],
                 sub_population[org_row-(len(sub_population)-1][org_column]]

    return neighbors

