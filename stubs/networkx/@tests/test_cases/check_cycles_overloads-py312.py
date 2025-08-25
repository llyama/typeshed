from collections.abc import Hashable
from typing import Literal
from typing_extensions import assert_type

import networkx as nx

multi_di_graph = nx.MultiDiGraph[str]()
assert_type(nx.find_cycle(multi_di_graph), list[tuple[str, str, Hashable]])
assert_type(nx.find_cycle(multi_di_graph, orientation="original"), list[tuple[str, str, Hashable, Literal["forward"]]])
assert_type(nx.find_cycle(multi_di_graph, orientation="reverse"), list[tuple[str, str, Hashable, Literal["reverse"]]])
assert_type(nx.find_cycle(multi_di_graph, orientation="ignore"), list[tuple[str, str, Hashable, Literal["forward", "reverse"]]])

multi_graph = nx.MultiGraph[str]()
assert_type(nx.find_cycle(multi_graph), list[tuple[str, str, Hashable]])
assert_type(nx.find_cycle(multi_graph, orientation="original"), list[tuple[str, str, Hashable, Literal["forward"]]])
assert_type(nx.find_cycle(multi_graph, orientation="reverse"), list[tuple[str, str, Hashable, Literal["forward"]]])
assert_type(nx.find_cycle(multi_graph, orientation="ignore"), list[tuple[str, str, Hashable, Literal["forward"]]])

di_graph = nx.DiGraph[str]()
assert_type(nx.find_cycle(di_graph), list[tuple[str, str]])
assert_type(nx.find_cycle(di_graph, orientation="original"), list[tuple[str, str, Literal["forward"]]])
assert_type(nx.find_cycle(di_graph, orientation="reverse"), list[tuple[str, str, Literal["reverse"]]])
assert_type(nx.find_cycle(di_graph, orientation="ignore"), list[tuple[str, str, Literal["forward", "reverse"]]])

graph = nx.Graph[str]()
assert_type(nx.find_cycle(graph), list[tuple[str, str]])
assert_type(nx.find_cycle(graph, orientation="original"), list[tuple[str, str, Literal["forward"]]])
assert_type(nx.find_cycle(graph, orientation="reverse"), list[tuple[str, str, Literal["forward"]]])
assert_type(nx.find_cycle(graph, orientation="ignore"), list[tuple[str, str, Literal["forward"]]])
