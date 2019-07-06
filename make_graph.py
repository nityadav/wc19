from graph_tool.all import *

run_rate_graph = Graph(directed=True)
edge_weights = run_rate_graph.new_edge_property('float')
vertex_map = {}

with open('all_run_rates.tsv') as inp_f:
    for line in inp_f:
        parts = line.strip().split('\t')
        if parts[0] not in vertex_map:
            vertex_map[parts[0]] = run_rate_graph.add_vertex()
        if parts[1] not in vertex_map:
            vertex_map[parts[1]] = run_rate_graph.add_vertex()
        edge = run_rate_graph.add_edge(vertex_map[parts[0]], vertex_map[parts[1]])
        edge_weights[edge] = float(parts[2])

ranks = pagerank(run_rate_graph, damping=0.95, max_iter=30)
print(ranks)

#graph_draw(run_rate_graph, vertex_text=run_rate_graph.vertex_index, vertex_font_size=18, output_size=(200, 200), vertex_size=ranks, edge_pen_width=edge_weights, output="run-rate-graph.png")
