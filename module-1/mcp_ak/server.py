import networkx as nx
from mcp.server.fastmcp import FastMCP

# 1. Initialize the Server
mcp = FastMCP("SterlingFamilyVault")

# 2. Setup the Knowledge Graph (In-memory for this test)
kg = nx.MultiDiGraph()
triplets = [
    ('Arthur', 'Is Parent Of', 'Bob'),
    ('Arthur', 'Is Parent Of', 'Diana'),
    ('Diana', 'Is Parent Of', 'Alice'),
    ('Bob', 'Is Sibling Of', 'Diana'),
    ('Edward', 'Is Parent Of', 'Alice')
]
for s, r, o in triplets:
    kg.add_edge(s, o, relation=r)

# 3. Define the Tool the AI will discover
@mcp.tool()
def graph_lookup(entity_query: str) -> str:
    """Consult the Knowledge Graph to see relationships for a specific entity."""
    # Normalize to Title Case to match our graph data
    node = entity_query.title()
    
    if node not in kg:
        return f"Entity '{node}' not found in the family records."
    
    results = []
    # Check Successors (Out-edges)
    for neighbor in kg.successors(node):
        edge_data = kg.get_edge_data(node, neighbor)
        relation = list(edge_data.values())[0]['relation']
        results.append(f"{node} {relation} {neighbor}")
        
    # Check Predecessors (In-edges)
    for source in kg.predecessors(node):
        edge_data = kg.get_edge_data(source, node)
        relation = list(edge_data.values())[0]['relation']
        results.append(f"{source} {relation} {node}")
    
    return "\n".join(results) if results else "No relationships found."

if __name__ == "__main__":
    mcp.run(transport="stdio")