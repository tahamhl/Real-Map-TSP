import osmnx as ox
import random
import folium
import networkx as nx

# 1. Gerçek Dünya Sokak Ağı İndirme
# Kadıköy, İstanbul'un sokak ağını indiriyoruz
place_name = "Kadıköy, Istanbul, Turkey"
graph = ox.graph_from_place(place_name, network_type='all')

# 2. TSP için Lokasyonları Seçme
# Harita üzerindeki rastgele 5 kavşak (node) seçiyoruz
nodes = list(graph.nodes)
tsp_nodes = random.sample(nodes, 5)  # 5 rastgele nokta seç

# 3. Heuristik Yöntem ile TSP Çözümü
# En yakın komşu algoritmasını kullanıyoruz
def nearest_neighbor(graph, start_node, tsp_nodes):
    tour = [start_node]
    unvisited = set(tsp_nodes) - {start_node}
    
    while unvisited:
        last_node = tour[-1]
        # NetworkX'in shortest_path_length fonksiyonunu kullanıyoruz
        nearest = min(unvisited, key=lambda node: nx.shortest_path_length(graph, last_node, node, weight='length'))
        tour.append(nearest)
        unvisited.remove(nearest)
    return tour

# Başlangıç noktası olarak rastgele bir node seçiyoruz
start_node = random.choice(tsp_nodes)

# TSP çözümünü buluyoruz
tour = nearest_neighbor(graph, start_node, tsp_nodes)

# 4. Harita Üzerinde Görselleştirme

# Harita merkezini Kadıköy'e alalım
map_center = [40.9902, 29.0228]
m = folium.Map(location=map_center, zoom_start=14)

# 4.1: Seçilen noktaları harita üzerinde işaretleyelim
for node in tsp_nodes:
    node_coords = (graph.nodes[node]['y'], graph.nodes[node]['x'])
    folium.Marker(location=node_coords, popup=f"Node {node}").add_to(m)

# 4.2: Rotayı çizelim
for i in range(len(tour)-1):
    node1 = tour[i]
    node2 = tour[i+1]
    node1_coords = (graph.nodes[node1]['y'], graph.nodes[node1]['x'])
    node2_coords = (graph.nodes[node2]['y'], graph.nodes[node2]['x'])
    folium.PolyLine([node1_coords, node2_coords], color="blue", weight=2.5, opacity=1).add_to(m)

# 5. Haritayı HTML Olarak Kaydetme
m.save("tsp_tour_map.html")

print("TSP çözümü tamamlandı ve harita 'tsp_tour_map.html' olarak kaydedildi.")
