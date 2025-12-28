# explain_my_repo/visualizer.py
"""
Simple Graphviz visualizer that draws files and classes and connects them.
Generates a .gv (and optionally renders to PNG if graphviz is installed).
"""
import os
from typing import Dict, Any, Optional
from graphviz import Digraph

def visualize(analysis: Dict[str, Any], out_path: Optional[str] = None, render: bool = False) -> str:
    """
    Create a graph showing files and classes.
    - out_path: base path for output (no extension). If None, uses 'structure'.
    - render: if True, call graph.render(...)
    Returns the path to the generated .gv file (or rendered file if render True).
    """
    base = out_path or "structure"
    gv_path = f"{base}.gv"

    dot = Digraph(comment="Repository structure")
    dot.attr(rankdir='LR')

    # Add file nodes
    for f in analysis.get("files", []):
        dot.node(f, label=os.path.basename(f), shape="note")

    # Add class nodes and edges
    for f, details in analysis.get("python", {}).get("files", {}).items():
        classes = details.get("classes", [])
        for cls in classes:
            cls_node = f"{f}::{cls}"
            dot.node(cls_node, label=cls, shape="box", style="filled", fillcolor="lightblue")
            dot.edge(f, cls_node)

    dot.save(gv_path)
    if render:
        try:
            dot.render(base, format='png', cleanup=True)
            return f"{base}.png"
        except Exception:
            # In case graphviz rendering is not available, just return the .gv path
            return gv_path
    return gv_path
