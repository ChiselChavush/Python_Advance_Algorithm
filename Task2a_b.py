# Importing libraries
import pandas as pd
import numpy as np
import time
import Task1a_b
data = pd.read_excel('London Underground data.xlsx')
start = time.time()


# Creating the class for Kruskal's Algorithm
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # Adding edges to our graph with this function
    def add_edge(self, u, v, w):
        # "u" and "v" are vertices of the edge, and "w" is the weight.
        self.graph.append([u, v, w])

    # Search function
    def find(self, parent, i):  # "i" is the vertex
        if parent[i] == i:  # If the vertex is the parent of itself
            return i  # Return the vertex
        # Function to get the key for any value
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):  # Applying union
        xroot = self.find(parent, x)  # Finding the root of x
        yroot = self.find(parent, y)  # Finding the root of y
        if rank[xroot] < rank[yroot]:  # If the rank of x is less than the rank of y
            parent[xroot] = yroot  # Make x the child of y
        elif rank[xroot] > rank[yroot]:  # If the rank of x is greater than the rank of y
            parent[yroot] = xroot  # Make y the child of x
        else:
            parent[yroot] = xroot  # Make y the child of x
            rank[xroot] += 1  # Function to get the key for any value

    #  Applying Kruskal algorithm
    def kruskal_algo(self):  # Function to get the key for any value
        result = []  # This will store the resultant MST
        i, e = 0, 0  # "i" is the index for sorted edges, "e" is the index for result[]
        # Sorting the graph in ascending order
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []  # This will store the parent of each vertex
        rank = []  # This will store the rank of each vertex
        for node in range(self.V):  # For each vertex
            parent.append(node)  # Make the parent of each vertex as itself
            rank.append(0)  # Make the rank of each vertex as 0
        while e < self.V - 1:  # While the number of edges in the MST is less than the number of vertices - 1
            u, v, w = self.graph[i]  # Get the next edge
            i = i + 1  # Increment the index for the next edge
            x = self.find(parent, u)  # Find the parent of u
            y = self.find(parent, v)  # Find the parent of v

            if x != y:  # If the parent of u is not equal to the parent of v
                e = e + 1  # Increment the number of edges in the MST
                result.append([u, v, w])  # Append the edge to the result
                self.apply_union(parent, rank, x, y)  # Apply union
            else:
                for row in data.values:  # For each row in the data
                    if str(row[3]) == 'nan':  # If the value in the 4th column is nan
                        continue  # Continue
                    # If the edge is in the data
                    if [get_key(u), get_key(v)] == [row[1].strip(), row[2].strip()]:
                        # Append the edge to the closed list
                        closed.append([row[0].strip(), get_key(u), get_key(v)])
        return result


''' Title: {Kruskal's Algorithm}
Author: {Cannot Found}
Date: {Cannot Found}
Code Version: {Python3}
Availability: {https://www.programiz.com/dsa/kruskal-algorithm} '''


def get_key(val):  # Function to get the key for any value
    for key, value in unique_stations_dict.items():  # For each key and value in the dictionary
        if val == value:  # If the value is equal to the value in the dictionary
            return key  # Return the key

    return "key doesn't exist"


''' Title: {Python | Get key from value in Dictionary}
Author: {Adarsh Verma}
Date: {10 August 2022}
Code Version: {Python3}
Availability: {https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/} '''


def unique_st():  # Function to get the unique stations
    stations = []  # This will store the stations

    for st in data['From']:  # For each station in the "From" column
        stations.append(st.strip())  # Append the station to the list

    return list(np.unique(stations))  # Return the unique stations


unique_stations = unique_st()  # Calling the function to get the unique stations
unique_stations_dict = {}  # This will store the unique stations as a dictionary

# For each station in the unique stations
for ids, station in enumerate(unique_stations):
    unique_stations_dict[station] = ids  # Add the station to the dictionary

stations_dict = {}  # This will store the stations as a dictionary

closed = []  # This will store the closed stations

for ids, row in enumerate(data.values):  # For each row in the data
    if str(row[3]) == 'nan':  # If the value in the 4th column is nan
        continue  # Continue
    # If the edge is in the dictionary
    if [unique_stations_dict[str(row[1]).strip()], unique_stations_dict[str(row[2]).strip()], int(row[3])] in stations_dict.values():
        closed.append([row[0].strip(), get_key(unique_stations_dict[str(row[1]).strip()]), get_key(
            unique_stations_dict[str(row[2]).strip()])])  # Append the edge to the closed list
        continue
    # If the edge is in the dictionary
    if [unique_stations_dict[str(row[2]).strip()], unique_stations_dict[str(row[1]).strip()], int(row[3])] in stations_dict.values():
        closed.append([row[0].strip(), get_key(unique_stations_dict[str(row[2]).strip()]), get_key(
            unique_stations_dict[str(row[1]).strip()])])  # Append the edge to the closed list
        continue
    stations_dict[ids] = [unique_stations_dict[str(row[1]).strip()], unique_stations_dict[str(
        row[2]).strip()], int(row[3])]  # Add the edge to the dictionary


def could_be_closed(line):  # Function to check if the line could be closed
    # Print the message
    print(
        f'\nFollowing immediate neighbouring stations could be closed from {line} line: ')
    for i in closed:  # For each edge in the closed list
        if i[0] == line:  # If the line is equal to the line in the closed list
            print(f'{i[1]} - {i[2]}')  # Print the edge


g = Graph(270)  # Creating the graph

for i in stations_dict.keys():  # For each edge in the dictionary
    g.add_edge(stations_dict[i][0], stations_dict[i][1], stations_dict[i][2])  # Add the edge to the graph

kruskal_graph = g.kruskal_algo()  # Calling the function to apply Kruskal algorithm


closed_lines = []  # This will store the closed lines
for i in closed:  # For each edge in the closed list
    if i[0] not in closed_lines:  # If the line is not in the closed lines list
        closed_lines.append(i[0])  # Append the line to the closed lines list
        # Call the function to check if the line could be closed
        could_be_closed(i[0])


print(f'\nMaximum {len(closed)} immediate neighbouring stations can be closed.')
for_dijkstra = []  # This will store the edges for Dijkstra algorithm

for i in kruskal_graph:  # For each edge in the Kruskal graph
    # Append the edge to the list
    for_dijkstra.append([get_key(i[0]), get_key(i[1]), i[2]])


print('\nTotal time taken while graph being created by Kruskal Algorithm : ', (time.time() - start), '\n')
# Calling the function to get the shortest path and distance
shortest_path, shortest_distance, start = Task1a_b.output(for_dijkstra)
print(f'List of stations the customer will travel after closures: {shortest_path}\n\nTotal taken time during this journey after closures: {shortest_distance} minutes.')  # Displayed the shortest path and total taken time during the journey.

Task1a_b.histogram_1b(for_dijkstra)  # Display histogram for Task2b
