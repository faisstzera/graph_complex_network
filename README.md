Welcome to the **Graph Complex Network** project! This project is focused on implementing various graph algorithms in Python to analyze a complex network derived from IMDB data. Specifically, we explore how different actors have interacted with each other throughout their careers and their interactions with directors.

## Overview

In this project, we dive deep into the realm of graph theory to understand the intricate web of connections between actors and directors. The goal is to construct and analyze these networks without relying on any graph libraries, purely using implementations derived from algorithmic pseudo-codes.

### Key Features

- **From Scratch Implementations**: All graph algorithms are implemented from scratch, based on pseudo-codes from authoritative algorithm books.
- **IMDB Data Analysis**: We focus on analyzing connections within the film industry, specifically the relationships between actors and directors over time.
- **Complex Network Analysis**: The project involves constructing and analyzing a network that reflects the interactions between individuals in the film industry.

## Project Components

### Data Collection

The initial step involves gathering data from IMDB. This data includes:

- **Actors**: Their movies and co-stars.
- **Directors**: Movies they have directed and the actors they have worked with.

### Graph Construction

Using the collected data, we construct a graph where:

- **Nodes** represent actors and directors.
- **Edges** represent interactions between actors (co-starring in the same movie) and between actors and directors (working together on a movie).

### Graph Algorithms

We implement and analyze several graph algorithms, including but not limited to:

1. **Breadth-First Search (BFS)**: To explore the shortest path between nodes.
2. **Depth-First Search (DFS)**: For exploring connectivity and component discovery.
3. **Dijkstra's Algorithm**: For finding the shortest paths between nodes.
4. **Graph Traversal**: To examine all possible paths and connections.
5. **Centrality Measures**: To determine the importance of nodes within the network.

### Analysis and Visualization

- **Network Metrics**: Calculation of various metrics such as degree distribution, clustering coefficient, and path length.
- **Community Detection**: Identifying clusters or communities within the network.
- **Visualization**: Although the primary focus is on algorithm implementation, some basic visualization techniques may be used to illustrate the network structure.

## Getting Started

### Prerequisites

To run this project, you will need:

- **Python 3.x**: The core programming language used for implementations.

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/graph_complex_network.git
cd graph_complex_network
```

### Running the Project

1. **Data Preparation**: Start by running the data collection script to fetch and preprocess IMDB data.
   ```bash
   python data_collection.py
   ```

2. **Graph Construction**: Use the prepared data to construct the graph.
   ```bash
   python graph_construction.py
   ```

3. **Algorithm Execution**: Execute various graph algorithms to analyze the network.
   ```bash
   python analyze_network.py
   ```

## Example Usage

After setting up, you can analyze the network to understand the connections in the film industry. Here are a few examples of what you can explore:

- **Shortest Path**: Find the shortest path between two actors.
- **Connected Components**: Identify all connected components in the network.
- **Central Actors**: Determine which actors are central based on their interactions.

## Contribution

Contributions are welcome! If you have any suggestions or improvements, feel free to fork the repository and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Dive into the world of graph theory and discover the hidden connections within the film industry! Enjoy exploring and analyzing the IMDB network.

---

