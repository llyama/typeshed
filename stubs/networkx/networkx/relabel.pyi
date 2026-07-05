from collections.abc import Callable, Hashable, Mapping
from typing import Literal, TypeVar, overload

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _EdgeData, _Node, _NodeData
from networkx.classes.multidigraph import MultiDiGraph
from networkx.classes.multigraph import MultiGraph
from networkx.utils.backends import _dispatchable

_NewNode = TypeVar("_NewNode", bound=Hashable, default=_Node)

__all__ = ["convert_node_labels_to_integers", "relabel_nodes"]

@overload
def relabel_nodes(
    G: MultiDiGraph[_Node, _NodeData, _EdgeData], mapping: Mapping[_Node, _NewNode], copy: bool = True
) -> MultiDiGraph[_Node | _NewNode, _NodeData, _EdgeData]: ...
@overload
def relabel_nodes(
    G: MultiDiGraph[_Node, _NodeData, _EdgeData], mapping: Callable[[_Node], _NewNode], copy: bool = True
) -> MultiDiGraph[_NewNode, _NodeData, _EdgeData]: ...
@overload
def relabel_nodes(
    G: DiGraph[_Node, _NodeData, _EdgeData], mapping: Mapping[_Node, _NewNode], copy: bool = True
) -> DiGraph[_Node | _NewNode, _NodeData, _EdgeData]: ...
@overload
def relabel_nodes(
    G: DiGraph[_Node, _NodeData, _EdgeData], mapping: Callable[[_Node], _NewNode], copy: bool = True
) -> DiGraph[_NewNode, _NodeData, _EdgeData]: ...
@overload
def relabel_nodes(
    G: MultiGraph[_Node, _NodeData, _EdgeData], mapping: Mapping[_Node, _NewNode], copy: bool = True
) -> MultiGraph[_Node | _NewNode, _NodeData, _EdgeData]: ...
@overload
def relabel_nodes(
    G: MultiGraph[_Node, _NodeData, _EdgeData], mapping: Callable[[_Node], _NewNode], copy: bool = True
) -> MultiGraph[_NewNode, _NodeData, _EdgeData]: ...
@overload
def relabel_nodes(
    G: Graph[_Node, _NodeData, _EdgeData], mapping: Mapping[_Node, _NewNode], copy: bool = True
) -> Graph[_Node | _NewNode, _NodeData, _EdgeData]: ...
@overload
def relabel_nodes(
    G: Graph[_Node, _NodeData, _EdgeData], mapping: Callable[[_Node], _NewNode], copy: bool = True
) -> Graph[_NewNode, _NodeData, _EdgeData]: ...

@_dispatchable
def convert_node_labels_to_integers(
    G: Graph[Hashable],
    first_label: int = 0,
    ordering: Literal["default", "sorted", "increasing degree", "decreasing degree"] = "default",
    label_attribute=None,
) -> Graph[int]: ...
