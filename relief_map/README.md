# Disaster Relief Map


## Running

1. `docker build -t relief_map .`
2. `docker run -p 8888:8888 -v rasters:/home/jovyan/work/rasters 
   relief_map`
3. Visit the URL provided at the end of the Docker log output
4. Open `map.ipynb`