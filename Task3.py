# Importing the libraries
import pandas as pd
import networkx as nx
import time
import Task1a_b

# importing data from the provided excel sheet
data = pd.read_excel('London Underground data.xlsx')  # Getting the data from provided excel sheet


def all_stations_with_lines():  # Calling all the immediate stations with times into list
    stations = []  # Keeping the data with no 'nan' strings
    for row in data.values:
        if str(row[3]) != 'nan':  # Ignoring the 'nan' strings
            stations.append([row[0].strip(), row[1].strip(), row[2].strip(), int(row[3])])  # Added strip() method to station names in order to fix the error of spaces of provided data
    return stations


def get_path_lines(path, edges, gr):
    minutes = []  # Minutes list keeps the times between the immediate neighbour stations in path list
    for i in range(len(path) - 1):
        minutes.append(nx.dijkstra_path_length(gr, path[i], path[i + 1], weight='weight'))  # Adding the times between immedate neighbour stations into minutes list
    lines = []       # Lines list keeps the zeroth element from the station list which are the underground lines.
    path_index = 0   # It is a count for path list indexes.
    flag = 0         # flag is resetting the edge_index
    edge_index = -1  # edge_index is a count for edges list indexes.

    # Loop (while) will run until the path_index is equal to one less than length of the path list
    while path_index != len(path) - 1:  # Algorithm get the one less than the list in order to count the last element.
        if flag == 1:                   # When flag is equal to one edges list will be checked from start again
            edge_index = 0
        edge_index += 1

        # If the current path list item and the next item is equal to current edges list's first and second items it will enter the next if statement!
        if [path[path_index], path[path_index + 1]] == [edges[edge_index][1], edges[edge_index][2]]:
            if edges[edge_index][3] == minutes[path_index]:  # If current edges list's thjrd item is equal to current minutes item it will add the current edges zeroth item (Line) into lines list.
                lines.append(edges[edge_index][0])  # Adding the current edges zeroth item (Line) into lines list.
                path_index += 1  # Increasing the path_index by one
                flag += 1  # Increasing the flag by one
        # Checking the for the other way around as well as for catching the possible other ways.
        elif [path[path_index + 1], path[path_index]] == [edges[edge_index][1], edges[edge_index][2]]: # If the current path list item and the next item is equal to current edges list's second and first items it will enter the next if statement!
            if edges[edge_index][3] == minutes[path_index]:  # If current edges list's thjrd item is equal to current minutes item it will add the current edges zeroth item (Line) into lines list.
                lines.append(edges[edge_index][0])  # Adding the current edges zeroth item (Line) into lines list.
                path_index += 1  # Increasing the path_index by one
                flag += 1  # Increasing the flag by one
        else:
            flag = 0  # If the current path list item and the next item is not equal to current edges list's first and second items it will reset the flag to zero
    return lines  # Calling the all_stations_with_lines function


def print_line_path(lines, path):
    pr = str()  # string for printing the path
    for i in range(len(lines) - 1):  # Loop for printing the path
        if lines[i] != lines[i + 1]:  # If the current line is not equal to the next line it will print the current line and the current station
            pr += f" when you reach \"{path[i + 1]}\", change line to \"{lines[i + 1]}\""  # Printing the current line and the current station
        elif len(lines) - 2 == i:  # If the current line is equal to the next line and the current line is the last line it will print the current line and the current station
            pr += "."  # Printing the current line and the current station
            break  # Breaking the loop
        if i != len(lines) - 2 and lines[i + 1] != lines[i + 2]:  # If the current line is equal to the next line and the next line is not equal to the next next line it will print the current line and the current station
            pr += ","  # Printing the current line and the current station
    print(f"\nStart from \"{path[0]}\" in \"{lines[0]}\" line{pr}")  # Printing the path


create_graph = Task1a_b.graph(Task1a_b.all_stations_with_times()) # Creating the graph
shortest_path, shortest_distance, _ = Task1a_b.output(Task1a_b.all_stations_with_times())  # Getting the shortest path, shortest distance and start time

print(f'Shortest list of stations the customer will travel: {shortest_path}\n\nTotal taken time: {shortest_distance} minutes.')  # Displayed the shortest path and total taken time during the journey.

# checking the total taken time while algorithm is running
start = time.time()  # Getting the start time
path_lines = get_path_lines(shortest_path, all_stations_with_lines(), create_graph)  # Getting the path lines

print_line_path(path_lines, shortest_path)  # Printing the path lines
print('\nTotal time taken while our linear search algorithm has been processed : ', (time.time() - start))  # Printing the total taken time while algorithm is running
