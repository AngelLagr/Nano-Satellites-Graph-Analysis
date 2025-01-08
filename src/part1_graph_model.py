import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Nécessaire pour le 3D
import math
import os

# Chemin vers le dossier contenant les données
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Remonte d'un niveau à partir de src/part1
data_dir = os.path.join(base_dir, "data")  # Accède au dossier data
output_dir = os.path.join(base_dir, "outputs", "part1")  # Chemin vers le dossier de sortie

# Chemin vers les fichiers CSV
file_paths = {
    'low': os.path.join(data_dir, 'topology_low.csv'),
    'avg': os.path.join(data_dir, 'topology_avg.csv'),
    'high': os.path.join(data_dir, 'topology_high.csv')
}

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
                    print("AEZAE")
    return G

# Fonction pour sauvegarder le graphe 3D en tant qu'image PNG
def save_graph_as_3d_png(G, title, filepath):
    pos = nx.get_node_attributes(G, 'pos')

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Extraire les coordonnées des nœuds
    xs, ys, zs = [], [], []
    for node, (x, y, z) in pos.items():
        xs.append(x)
        ys.append(y)
        zs.append(z)
    
    # Tracer les nœuds
    ax.scatter(xs, ys, zs, c='b', s=20, label='Satellites')

    # Tracer les arêtes
    for edge in G.edges():
        x_coords = [pos[edge[0]][0], pos[edge[1]][0]]
        y_coords = [pos[edge[0]][1], pos[edge[1]][1]]
        z_coords = [pos[edge[0]][2], pos[edge[1]][2]]
        ax.plot(x_coords, y_coords, z_coords, c='r', alpha=0.7, linewidth=1)
        
    # Configuration de l'affichage
    ax.set_title(title, fontsize=14)
    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')
    plt.legend()
    plt.savefig(filepath, format='png')
    plt.close()

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
        save_graph_as_3d_png(G, title, filepath)
        print(f"3D Graph saved: {filepath}")
