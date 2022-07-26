# Hurricane Katrina Path

This example demonstrates how to use KnowWhereGraph's SPARQL endpoint to
download, plot, and export the trajectory of Hurricane Katrina (2005) as
a shapefile.

## Running

1. `docker build -t katrina .`
2. `docker run -p 8888:8888 katrina`
3. Visit the URL provided at the end of the Docker log output
4. Open `katrina_path.ipynb`