# NanoSatellites Graph Analysis

## Description du Projet
Ce projet porte sur l'analyse de graphes modélisant un essaim de nanosatellites en orbite autour de la Lune. Les nanosatellites échangent des données via un routage opportuniste, avec des portées de communication modulables (20 km, 40 km, 60 km). Le projet vise à modéliser l'essaim sous forme de graphes et à analyser leurs caractéristiques dans différentes configurations.

### Objectifs
1. Modéliser les graphes pour trois densités (élevée, moyenne, faible) et trois portées.
2. Analyser les caractéristiques des graphes non valués (degré, cliques, composantes connexes, etc.).
3. Explorer les graphes valués avec un coût d'arête proportionnel au carré de la distance.

## Structure du Projet

```plaintext
NanoSatellites_GraphAnalysis/
├── data/                      # Données CSV
│   ├── topology_low.csv
│   ├── topology_avg.csv
│   └── topology_high.csv
├── src/                       # Scripts Python
│   ├── part1_graph_model.py   # Partie 1 : Modélisation des graphes
│   ├── part2_unweighted.py    # Partie 2 : Analyse des graphes non valués
│   ├── part3_weighted.py      # Partie 3 : Analyse des graphes valués
│   └── utils.py               # Fonctions utilitaires
├── outputs/                   # Résultats générés
│   ├── images/                # Graphes en PNG
│   ├── reports/               # Rapports de calculs
├── README.md                  # Documentation
├── requirements.txt           # Dépendances Python
├── rapport.pdf                # Rapport de 5 pages
└── video.mp4                  # Capsule vidéo de 3 minutes
```

## Prérequis
- Python 3.8+
- Bibliothèques Python : `pandas`, `networkx`, `matplotlib`, `numpy`

Pour installer les dépendances :
```bash
pip install -r requirements.txt
```

## Instructions d'Exécution

1. **Partie 1 : Modélisation des Graphes**
   - Exécutez le script pour générer les graphes en PNG :
     ```bash
     python src/part1_graph_model.py
     ```
   - Les images seront sauvegardées dans `outputs/images/`.

2. **Partie 2 : Analyse des Graphes Non Valués**
   - Lancez le script :
     ```bash
     python src/part2_unweighted.py
     ```
   - Les résultats (degrés, cliques, chemins, etc.) seront dans `outputs/reports/`.

3. **Partie 3 : Analyse des Graphes Valués**
   - Exécutez le script pour la portée de 60 km avec coûts :
     ```bash
     python src/part3_weighted.py
     ```
   - Les résultats seront sauvegardés dans `outputs/reports/`.

## Livrables
- **Rapport PDF** : 5 pages contenant les méthodes et résultats du projet.
- **Capsule Vidéo** : Vidéo de 3 minutes expliquant les choix conceptuels et résultats.
- **Code Source** : Scripts Python pour la modélisation et l'analyse des graphes.

## Auteurs
- **Riadh DHAOU** (Encadrant)
- [Votre Nom] (Etudiant)

## Références
1. Evelyne Akopyan, Riadh Dhaou, Emmanuel Lochin, Bernard Pontet, Jacques Sombrin. *On the Network Characterization of Nano-Satellite Swarms.* 28th IEEE Symposium on Computers and Communications (ISCC 2023), IEEE, Jul 2023. ([Lien vers l'article](https://ieeexplore.ieee.org/document/10218020))

