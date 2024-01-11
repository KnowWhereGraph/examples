# Graph Statistics

This generates node statistics for the KnowWhereGraph subgraphs. It retrieves the triple count in each subgraph and writes the results to disk.



## Running

1. `docker build -t graph_stats .`
2. `docker run -v ./results:/results graph_stats`
3. Once the queries complete, view the results in the `results/` folder
