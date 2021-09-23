import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
df1 = pd.read_csv (r'C:\Users\saySa\OneDrive\Desktop\dataset_1_HP.csv')
print (df1)
df1=df1[['Parasites', 'Hosts' , 'Value']]
G=nx.from_pandas_edgelist(df=df1, source='Parasites', target='Hosts', edge_attr='Value', create_using=nx.Graph())
print(nx.info(G), "\n")
nx.draw(G)
print("Network Density: ",nx.density(G))
print("Network Transitivity: ",nx.transitivity(G))
print("Network Assortativity: ",nx.assortativity.degree_pearson_correlation_coefficient(G))
print("Average Shortest Path Length: ",nx.average_shortest_path_length(G))


