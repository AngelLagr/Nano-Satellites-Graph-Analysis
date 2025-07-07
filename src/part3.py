import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import math
import os

# Chemin vers le dossier contenant les données
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Remonte d'un niveau à partir de src/part1
data_dir = os.path.join(base_dir, "data")  # Accède au dossier data
output_dir = os.path.join(base_dir, "outputs", "part3")  # Chemin vers le dossier de sortie pour la partie 2

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
                    G.add_edge(i, j, weight=distance**2)
    return G

max_range = 60000

# Pour chaque densité et portée, calculer les caractéristiques
for density, file_path in file_paths.items():
    data = pd.read_csv(file_path)
    G = create_graph(data, max_range)
    
    # Créer un répertoire de sortie pour chaque cas
    case_dir = os.path.join(output_dir, f"{density}_{max_range}m")
    os.makedirs(case_dir, exist_ok=True)

    # Fichier d'analyse
    analysis_file_path = os.path.join(case_dir, "analysis.txt")
    with open(analysis_file_path, "w") as f:
        # 1. Degré moyen
        degree_mean = sum(dict(G.degree()).values()) / len(G.nodes)
        f.write(f"Degré moyen ({density}, {max_range} m): {degree_mean}\n\n")

        # 2. Distribution du degré (Histogramme)
        degrees = [deg for _, deg in G.degree()]
        str_frequence = 'Fréquence'
        degree_hist_file = os.path.join(case_dir, "degree_distribution.png")
        plt.hist(degrees, bins=range(min(degrees), max(degrees) + 1), alpha=0.75)
        plt.title(f'Distribution du degré ({density}, {max_range} m)')
        plt.xlabel('Degré')
        plt.ylabel(str_frequence)
        plt.savefig(degree_hist_file)
        plt.close()
        f.write(f"Graphique de la distribution du degré enregistré dans: {degree_hist_file}\n\n")

        # 3. Moyenne du degré de clustering
        clustering_mean = nx.average_clustering(G)
        f.write(f"Moyenne du degré de clustering ({density}, {max_range} m): {round(clustering_mean,3)}\n\n")
        
        clustering = list(nx.clustering(G).values())
        clustering_hist_file = os.path.join(case_dir, "clustering_distribution.png")
        plt.hist(clustering, bins=20, alpha=0.75)
        plt.title(f'Distribution du degré de clustering ({density}, {max_range} m)')
        plt.xlabel('Degré de clustering')
        plt.ylabel(str_frequence)
        plt.savefig(clustering_hist_file)
        plt.close()
        f.write(f"Graphique de la distribution du degré de clustering enregistré dans: {clustering_hist_file}\n\n")

        # 4. Nombre de cliques et leurs ordres
        cliques = list(nx.find_cliques(G))
        cliques_sizes = [len(clique) for clique in cliques]
        f.write(f"Nombre de cliques ({density}, {max_range} m): {len(cliques)}\n\n")
        cliques_hist_file = os.path.join(case_dir, "cliques_distribution.png")
        plt.hist(cliques_sizes, bins=20, alpha=0.75)
        plt.title(f'Distribution des de cliques ({density}, {max_range} m)')
        plt.xlabel('Tailles des cliques')
        plt.ylabel(str_frequence)
        plt.savefig(cliques_hist_file)
        plt.close()
        f.write(f"Graphique de la distribution de la taille de cliques enregistré dans: {cliques_hist_file}\n\n")

        # 5. Nombre de composantes connexes et leurs ordres
        components = list(nx.connected_components(G))
        components_sizes = [len(comp) for comp in components]
        f.write(f"Nombre de composantes connexes ({density}, {max_range} m): {len(components)}\n\n")
        components_hist_file = os.path.join(case_dir, "components_distribution.png")
        plt.hist(components_sizes, bins=20, alpha=0.75)
        plt.title(f'Distribution des de cliques ({density}, {max_range} m)')
        plt.xlabel('Tailles des cliques')
        plt.ylabel(str_frequence)
        plt.savefig(components_hist_file)
        plt.close()
        f.write(f"Graphique de la distribution de l'ordre des composantes connexes enregistré dans: {components_hist_file}\n\n")

        # 6. Longueur moyenne des plus courts chemins avec les poids
        all_shortest_paths = {}
        for source in G.nodes():
            # Utiliser shortest_path_length avec 'weight' pour chaque source
            all_shortest_paths[source] = dict(nx.shortest_path_length(G, source=source, weight='weight'))
        
        shortest_paths_lengths = [length for _, paths in all_shortest_paths.items() for length in paths.values()]
        
        if shortest_paths_lengths:
            avg_shortest_path_length = sum(shortest_paths_lengths) / len(shortest_paths_lengths)
            f.write(f"Longueur moyenne des plus courts chemins ({density}, {max_range} m): {round(avg_shortest_path_length/100000,1)} m\n\n")
        
        # 7. Distribution des plus courts chemins
        shortest_path_hist_file = os.path.join(case_dir, "shortest_path_distribution.png")
        plt.hist(shortest_paths_lengths, bins=20, alpha=0.75)
        plt.title(f'Distribution des plus courts chemins ({density}, {max_range} m)')
        plt.xlabel('Longueur du chemin')
        plt.ylabel(str_frequence)
        plt.savefig(shortest_path_hist_file)
        plt.close()
        f.write(f"Graphique de la distribution des plus courts chemins enregistré dans: {shortest_path_hist_file}\n\n")

        # 8. Nombre des plus courts chemins (en nombre de sauts)
        num_shortest_paths = len(shortest_paths_lengths)
        f.write(f"Nombre de plus courts chemins ({density}, {max_range} m): {num_shortest_paths}\n\n")

        print(f"Analyse pour {density}, {max_range} m sauvegardée dans: {case_dir}")
