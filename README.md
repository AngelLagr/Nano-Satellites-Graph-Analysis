# NanoSatellites Graph Analysis

## Project Description
This project focuses on analyzing graphs that model a swarm of nanosatellites in orbit around the Moon. These nanosatellites exchange data using opportunistic routing, with adjustable communication ranges (20 km, 40 km, 60 km). The goal is to model the swarm as graphs and analyze their properties under different configurations.

### Objectives
1. Model the graphs for three densities (high, medium, low) and three communication ranges.
2. Analyze the characteristics of unweighted graphs (degree, cliques, connected components, etc.).
3. Explore weighted graphs with edge costs proportional to the square of the distance.

## Project Structure

```plaintext
NanoSatellites_GraphAnalysis/
├── data/                      # CSV data
│   ├── topology_low.csv
│   ├── topology_avg.csv
│   └── topology_high.csv
├── src/                       # Python scripts
│   ├── part1_graph_model.py   # Part 1: Graph modeling
│   ├── part2_unweighted.py    # Part 2: Unweighted graph analysis
│   ├── part3_weighted.py      # Part 3: Weighted graph analysis
│   └── utils.py               # Utility functions
├── outputs/                   # Generated results
│   ├── images/                # Graph PNGs
│   ├── reports/               # Analysis reports
├── README.md                  # Documentation
├── requirements.txt           # Python dependencies
├── report.pdf                 # 5-page project report
└── video.mp4                  # 3-minute video presentation
```

## Prerequisites
- Python 3.8+
- Python libraries: `pandas`, `networkx`, `matplotlib`, `numpy`

To install dependencies:
```bash
pip install -r requirements.txt
```

## Execution Instructions

1. **Part 1: Graph Modeling**
   - Run the script to generate graphs as PNG images:
     ```bash
     python src/part1_graph_model.py
     ```
   - Images will be saved in `outputs/images/`.

2. **Part 2: Unweighted Graph Analysis**
   - Execute the script:
     ```bash
     python src/part2_unweighted.py
     ```
   - Results (degree, cliques, paths, etc.) will be saved in `outputs/reports/`.

3. **Part 3: Weighted Graph Analysis**
   - Run the script for 60 km range with edge costs:
     ```bash
     python src/part3_weighted.py
     ```
   - Results will be saved in `outputs/reports/`.

## Deliverables
- **PDF Report**: 5 pages presenting the project methods and results.
- **Video Presentation**: A 3-minute video explaining conceptual choices and outcomes.
- **Source Code**: Python scripts for graph modeling and analysis.

## Authors
- **Riadh DHAOU** (Supervisor)
- [Your Name] (Student)

## References
1. Evelyne Akopyan, Riadh Dhaou, Emmanuel Lochin, Bernard Pontet, Jacques Sombrin. *On the Network Characterization of Nano-Satellite Swarms.* 28th IEEE Symposium on Computers and Communications (ISCC 2023), IEEE, Jul 2023. ([Link to article](https://ieeexplore.ieee.org/document/10218020))

