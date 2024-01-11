from SPARQLWrapper import SPARQLWrapper, CSV

sparql = SPARQLWrapper("https://stko-kwg.geog.ucsb.edu/sparql")
sparql.setReturnFormat(CSV)
query = """PREFIX kwgr: <http://stko-kwg.geog.ucsb.edu/lod/resource/>
SELECT ?g (COUNT(*) as ?triple_count)
WHERE {
  GRAPH ?g {
    ?subject ?predicate ?object .
  }
} GROUP BY ?g"""
sparql.setQuery(query)

try:
    res = sparql.query().convert()
    with open('/results/stats.csv','wb') as file:
        file.write(res)
except Exception as e:
    print(f"Error retrieving named graph results: {e}")
