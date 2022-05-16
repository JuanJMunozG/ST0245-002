import networkx as nx
import pydeck as pdk


def readRealtime(name: str, sep=";"):
    with open(name, 'r') as file:
        for i in file.readlines():
            yield i.split(sep)


def leerCsv():
    grafo = nx.Graph()
    ii = 0
    for i in readRealtime("data_csv.csv", sep=";"):
        if ii == 0:
            pass
        else:
            edge = eval(i[-2])
            grafo.add_edge(str(edge[0]), str(edge[1]), weight=i[-3])
            grafo.add_node(str(i[-1][:-2]))
        ii += 1
    return grafo


def dijkstra(grafo, inicio, fin):
    return(nx.dijkstra_path(grafo, inicio, fin, weight='weight'))


# Source https://github.com/jero98772/AlOtroLado by jero98772
class configMap:
    """
    class for draw in map
    """

    def __init__(self, data):
        self.emptyMap = pdk.Layer(
            type="PathLayer",
            data="",
            pickable=True,
            get_color=(0, 155, 0),
            width_scale=1,
            width_min_pixels=1,
            get_path="edges",
            get_width=1,
        )

        self.pathMap = pdk.Layer(
            type="PathLayer",
            data=data,
            pickable=True,
            get_color=(0, 155, 0),
            width_scale=1,
            width_min_pixels=1,
            get_path="edges",
            get_width=2,
        )

        self.nodesMap = pdk.Layer(
            "ScatterplotLayer",
            data=data,
            pickable=True,
            opacity=0.8,
            stroked=True,
            filled=True,
            radius_scale=6,
            radius_min_pixels=1,
            radius_max_pixels=100,
            line_width_min_pixels=1,
            get_position="node",
            get_radius=1,
            get_fill_color=[137, 36, 250],
            get_line_color=[0, 0, 0],
        )

    def newPath(data, tag="path", color=(0, 15, 205)):
        newPath = pdk.Layer(
            type="PathLayer",
            data=data,
            pickable=False,
            get_color=color,
            width_scale=5,
            width_min_pixels=5,
            get_path=tag,
            get_width=5,
        )
        return newPath

    def genMapMultlayer(self, fileName, layers: list):
        view = pdk.ViewState(latitude=6.256405968932449, longitude=-75.59835591123756, pitch=40, zoom=12)
        mapCompleate = pdk.Deck(layers=layers, initial_view_state=view)
        mapCompleate.to_html(fileName)

    def getEmptyMap(self): return self.emptyMap

    def getPathMap(self): return self.pathMap

    def getnodesMap(self): return self.nodesMap