import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
# read the excel (.xls) file
df1 = pd.read_excel (r'C:\Users\saySa\OneDrive\Desktop\Dataset\A_HP_041.xls',index_col=[0])

# Delete the first column that has data on the total number of samples
del df1['Num. of hosts sampled']

# convert to a list
df2 = df1.stack().reset_index()

#create a graph with labels
G=nx.from_pandas_edgelist(df=df2, source='level_0', target='level_1', create_using=nx.Graph())
nx.draw(G,with_labels =True)