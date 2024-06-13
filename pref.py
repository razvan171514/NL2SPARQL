import rdflib

def get_prefixes(rdf_file_path):
    # Create a graph
    g = rdflib.Graph()
    
    # Parse the RDF file
    g.parse(rdf_file_path, format='application/rdf+xml')
    
    # Extract namespaces and prefixes
    namespaces = {}
    for prefix, namespace in g.namespaces():
        namespaces[prefix] = str(namespace)
    
    return namespaces

# Specify the path to your RDF file
rdf_file_path = '../wine.rdf'

# Get prefixes and namespaces
prefixes = get_prefixes(rdf_file_path)

# Print prefixes and namespaces
for prefix, namespace in prefixes.items():
    print(f"Prefix: {prefix}, Namespace: {namespace}")
