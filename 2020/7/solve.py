#!/usr/bin/python3

import sys
import re
from typing import List, Tuple

import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import matplotlib.pyplot as plt

Rule = Tuple[str, List[Tuple[str, int]]]
def extract_rule(s: str) -> Rule:
    m = re.match(r"^([a-z ]+) bags contain ", s)
    color = m.group(1)

    rest = s[m.end():]
    if rest == "no other bags.":
        return (color, [])

    contents = []
    rest = rest.split(", ")
    for b in rest:
        m = re.match(r"^(\d+) ([a-z ]+) bag(?:s)?", b)
        i = int(m.group(1))
        c = m.group(2)

        contents += [(c, i)]

    return (color, contents)

def get_count(g, n: str) -> int:
    if g.out_degree(n) == 0:
        return 1

    res = 0
    for e in g.out_edges(n):
        res += g.edges[e]['count'] * get_count(g, e[1])
    return res + 1

def dbg_draw(g, root: str):
    pos = graphviz_layout(g, prog="dot", root=root)
    nx.draw(g, pos, with_labels=True)

    lbls = nx.get_edge_attributes(g, "count")
    nx.draw_networkx_edge_labels(g, pos, edge_labels=lbls, font_size=7)

    sinks = [n for n in g.nodes() if g.out_degree(n) == 0]
    nx.draw_networkx(g, pos, node_color="red", nodelist=[root])
    nx.draw_networkx(g, pos, node_color="purple", nodelist=sinks)

    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(-1)

    with open(sys.argv[1], 'r') as f:
        lines = [l.rstrip() for l in f.readlines()]

    rules = [extract_rule(l) for l in lines]

    DG = nx.DiGraph()

    for r in rules:
        for c in r[1]:
            DG.add_edge(r[0], c[0], count=c[1])

    # Part 1
    rev = DG.reverse()
    d = nx.descendants(rev, "shiny gold")
    print(len(d))

    # Part 2
    K = DG.subgraph([*nx.descendants(DG, "shiny gold"), "shiny gold"])
    print(get_count(K, "shiny gold") - 1)

    #dbg_draw(K, "shiny gold")
