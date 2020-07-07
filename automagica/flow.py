import json
import logging
import os

from .nodes import (
    ActivityNode,
    CommentNode,
    IfElseNode,
    DotPyFileNode,
    LoopNode,
    StartNode,
    SubFlowNode,
    PythonCodeNode,
)
from automagica.config import _


class Flow:
    def __init__(self, file_path=None, nodes=[], name=None):
        self.file_path = file_path
        self.nodes = nodes

        if not name:
            name = _("Unnamed Flow")

        self.name = name

        if self.file_path:
            self.load(self.file_path)

        else:
            node = StartNode(x=100, y=100)
            self.nodes.append(node)

    def load(self, file_path):
        self.file_path = file_path

        logging.debug(_("Loading Flow from {}").format(file_path))

        with open(file_path, "r") as f:
            data = json.load(f)

        working_dir = os.path.dirname(file_path)

        self.from_dict(data)

        logging.info(_("Loaded Flow from {}").format(file_path))

    def from_dict(self, data):
        self.name = data.get("name")
        self.nodes = []

        for d in data["nodes"]:
            if d["type"] == "StartNode":
                node = StartNode(
                    x=d.get("x"),
                    y=d.get("y"),
                    uid=d.get("uid"),
                    next_node=d.get("next_node"),
                    label=d.get("label"),
                )

            elif d["type"] == "ActivityNode":
                node = ActivityNode(
                    d["activity"],
                    label=d.get("label"),
                    x=d.get("x"),
                    y=d.get("y"),
                    uid=d.get("uid"),
                    next_node=d.get("next_node"),
                    args_=d.get("args"),
                    class_=d.get("class"),
                    return_=d.get("return_"),
                    on_exception_node=d.get("on_exception_node"),
                )

            elif d["type"] == "IfElseNode":
                node = IfElseNode(
                    d["condition"],
                    label=d.get("label"),
                    x=d.get("x"),
                    y=d.get("y"),
                    uid=d.get("uid"),
                    next_node=d.get("next_node"),
                    else_node=d.get("else_node"),
                )

            elif d["type"] == "LoopNode":
                node = LoopNode(
                    d["iterable"],
                    label=d.get("label"),
                    x=d.get("x"),
                    y=d.get("y"),
                    uid=d.get("uid"),
                    next_node=d.get("next_node"),
                    loop_node=d.get("loop_node"),
                    loop_variable=d.get("loop_variable"),
                    repeat_n_times=d.get("repeat_n_times"),
                    iterable=d.get("iterable"),
                )

            elif d["type"] == "DotPyFileNode":
                node = DotPyFileNode(
                    str(d["dotpyfile_path"]),
                    label=d.get("label"),
                    x=d.get("x"),
                    y=d.get("y"),
                    uid=d.get("uid"),
                    next_node=d.get("next_node"),
                    on_exception_node=d.get("on_exception_node"),
                )
            elif d["type"] == "PythonCodeNode":
                node = PythonCodeNode(
                    code=d["code"],
                    label=d.get("label"),
                    x=d.get("x"),
                    y=d.get("y"),
                    uid=d.get("uid"),
                    next_node=d.get("next_node"),
                    on_exception_node=d.get("on_exception_node"),
                )

            elif d["type"] == "CommentNode":
                node = CommentNode(
                    d["comment"],
                    label=d.get("label"),
                    x=d.get("x"),
                    y=d.get("y"),
                    uid=d.get("uid"),
                )

            elif d["type"] == "SubFlowNode":
                node = SubFlowNode(
                    str(d.get("subflow_path", "")),
                    label=d.get("label"),
                    x=d.get("x"),
                    y=d.get("y"),
                    uid=d.get("uid"),
                    next_node=d.get("next_node"),
                    on_exception_node=d.get("on_exception_node"),
                    subflow_path=d.get("subflow_path"),
                )

            self.nodes.append(node)

    def get_node_by_uid(self, uid):
        for node in self.nodes:
            if node.uid == uid:
                return node

    def validate(self):
        # Validation rules

        # 1. Unconnected nodes

        # 2. Missing (required) parameters for activity

        # 3. Multiple start nodes

        return [
            "Node 3Qse is not connected to any nodes",
            "Multiple Start nodes",
            "Missing parameter 'limit' for Random Number activity (node Swej)",
        ]

    def to_dict(self):
        return {"nodes": [node.to_dict() for node in self.nodes], "name": self.name}

    def save(self, file_path):
        logging.debug(_("Saving to {}").format(file_path))

        with open(file_path, "w") as f:
            json.dump(self.to_dict(), f, indent=4)

        logging.info(_("Saved to {}").format(file_path))

    def add_activity_node(self, activity, previous_node=None):
        node = ActivityNode(activity)

        if previous_node:
            previous_node.next_node = node.uid

            node.x = previous_node.x + 175
            node.y = previous_node.y

        self.nodes.append(node)

        return node

    def add_node(self, node_type):
        node = eval("{}Node()".format(node_type))  # TODO: Perhaps prevent eval() here?

        if self.nodes and node_type not in ("Start", "Comment"):
            previous_node = self.nodes[-1]
            previous_node.next_node = node.uid

            node.x = previous_node.x + 175
            node.y = previous_node.y

        self.nodes.append(node)
        return node

    def get_start_nodes(self):
        nodes = []
        for node in self.nodes:
            if isinstance(node, StartNode):
                nodes.append(node)
        return nodes

    def remove_dead_ends(self):
        uids = [node.uid for node in self.nodes]

        for node in self.nodes:
            if hasattr(node, "next_node"):
                if node.next_node not in uids:
                    node.next_node = None

            if hasattr(node, "else_node"):
                if node.else_node not in uids:
                    node.else_node = None

            if hasattr(node, "on_exception_node"):
                if node.on_exception_node not in uids:
                    node.on_exception_node = None

            if hasattr(node, "loop_node"):
                if node.loop_node not in uids:
                    node.loop_node = None

