# Importing the libraries
import pandas as pd
import networkx as nx
'''Title: {NetworkX} 
Author: {Aric Hagberg, Dan Schult, Pieter Swart}
Date: {17 August 2008}
Code Version: {0.36}
Availablability: {https://networkx.org/documentation/networkx-0.37/}'''
import matplotlib.pyplot as plt
import time

data = pd.read_excel('London Underground data.xlsx')  # Getting the data from provided excel sheet


def all_stations_with_times():  # Calling all the immediate stations with times into list
    stations = []
    for row in data.values:
        if str(row[3]) != 'nan':  # Ignoring the 'nan' strings
            stations.append([row[1].strip(), row[2].strip(), int(row[3])])  # Added ".strip()" method to station names in order to fix the error of spaces of provided data
    return stations


def graph(calling_st):  # Creating the graph for Dijkstra
    gr = nx.Graph()
    gr.add_weighted_edges_from(calling_st)  # Getting the nodes and edges with their weights
    return gr


def dijkstra_path(gr, departing_st, arriving_st):
    path = nx.dijkstra_path(gr, departing_st, arriving_st)  # Using the "Dijkstra" in order to find the shortest path
    return path


def dijkstra_distance(gr, departing_st, arriving_st):
    distance = nx.dijkstra_path_length(gr, departing_st, arriving_st, weight='weight')  # Added the weight to find the sum of the taken times between given stations to get the total distance
    return distance


def output(edges):
    # Taking input from the customer as a start point
    departing_station = str(input("Please provide 'Destination' point of your journey?\n")).strip()
    # Taking input from the customer as end point
    arriving_station = str(input("Please provide 'Arriving' point of your journey?\n")).strip()
    t = time.time()
    try:
        create_graph = graph(edges)
        shortest_pt = dijkstra_path(create_graph, departing_station, arriving_station)
        shortest_dist = dijkstra_distance(create_graph, departing_station, arriving_station)
        return shortest_pt, shortest_dist, t
    except:
        print('Please enter valid station names!')
        return output(edges)


shortest_path, shortest_distance, start = output(all_stations_with_times())
print(f'List of stations the customer will travel: {shortest_path}\n\nTotal taken time during this journey: {shortest_distance} minutes.')  # Displayed the shortest path and total taken time during the journey.
print('\nTotal time taken while finding the shortest path and journey time : ', (time.time() - start))


# Creating the histogram with all the quickest possible journeys (Depends on time).
def histogram_1b(stations_times):
    gra = graph(stations_times)
    all_weighted_paths = []  # Fetching all the possible paths with their distances.
    histogram_list = []  # Fetching only all the distances, in order to plot a histogram.
    t = time.time()

    for i in stations_times:
        for j in stations_times:
            x = dijkstra_path(gra, i[0], j[1])  # Call the path for variable of "x".
            y = dijkstra_distance(gra, i[0], j[1])  # Call the distance for variable of "y".
            if [x, y] not in all_weighted_paths:  # If the paths and the distances are not in the "all_weighted_path" list, it will append them into it.
                all_weighted_paths.append([x, y])

    for i in all_weighted_paths:  # Fetching only all the distances, in order to plot a histogram.
        histogram_list.append(i[1])

    plt.hist(histogram_list, bins=range(0, 111, 1), color='black', align='left', edgecolor='white')  # Creating the display for the histogram.
    plt.title("Quickest Journey Times")
    plt.xticks(range(0, 111, 5), color="#572681")
    plt.title("Quickest Journey Times")
    plt.xlabel("Total Taken Minutes Of The Possible Routes")  # x axis
    plt.ylabel("Journey Frequency")  # y axis

    print('\nNumber of all possible journeys:', len(histogram_list))  # Displaying the length of the 'histogram_list'.
    print('\nTotal time taken while histogram being created : ', (time.time() - t))

    plt.show()


histogram_1b(all_stations_with_times())
