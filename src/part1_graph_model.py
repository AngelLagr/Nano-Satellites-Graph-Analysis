import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import math
import os

# Fonction pour calculer la distance entre deux satellites
def calculate_distance(sat1, sat2):
    return math.sqrt((sat1['x'] - sat2['x'])**2 + (sat1['y'] - sat2['y'])**2 + (sat1['z'] - sat2['z'])**2)

# Fonction pour créer un graphe basé sur les positions et la portée
def create_graph(data, max_range):
    G = nx.Graph()
    # Ajouter les noeuds
    for index, row in data.iterrows():
        G.add_node(index, pos=(row['x'], row['y'], row['z']))
    # Ajouter les arêtes si la distance est inférieure à la portée
    for i, sat1 in data.iterrows():
        for j, sat2 in data.iterrows():
            if i < j:  # éviter de recalculer pour j < i
                distance = calculate_distance(sat1, sat2)
                if distance <= max_range:
                    G.add_edge(i, j)
    return G

# Fonction pour sauvegarder le graphe en tant qu'image PNG
def save_graph_as_png(G, title, filepath):
    pos = nx.get_node_attributes(G, 'pos')
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos={k: (v[0], v[1]) for k, v in pos.items()}, with_labels=False, node_size=50)
    plt.title(title)
    plt.savefig(filepath, format='png')
    plt.close()

# Créer le dossier de sauvegarde si nécessaire
output_dir = './Partie 1/generated'
os.makedirs(output_dir, exist_ok=True)

# Charger les données
file_paths = {
    'low': './topology/topology_low.csv',
    'avg': './topology/topology_avg.csv',
    'high': './topology/topology_high.csv'
}
ranges = [20, 40, 60]

# Processus pour chaque densité et chaque portée
for density, file_path in file_paths.items():
    data = pd.read_csv(file_path)
    for max_range in ranges:
        G = create_graph(data, max_range)
        # Construire un nom de fichier lisible
        filename = f'essaim_{density}_density_{max_range}km.png'
        filepath = os.path.join(output_dir, filename)
        title = f'Density: {density.capitalize()} - Range: {max_range} km'
        save_graph_as_png(G, title, filepath)
        print(f"Graph saved: {filepath}")

