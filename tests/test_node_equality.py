from __future__ import print_function

from flowpipe import Graph, Node, OutputPlug, InputPlug


@Node(outputs=["output"])
def Node1(input):
    pass


@Node(outputs=["output"])
def Node2(input):
    pass


def test_nodes_can_only_be_compared_with_other_nodes(clear_default_graph):
    assert Node1(name="1") != "Not a node"


def test_nodes_are_not_equal_if_their_class_names_differ(clear_default_graph):
    assert Node1(name="1") == Node1(name="2")
    assert Node1(name="3") != Node2(name="4")


def test_nodes_are_not_equal_if_their_is_dirty_state_differ(clear_default_graph):
    node1 = Node1(name="1")
    node2 = Node1(name="2")

    assert node1 == node2

    node1.evaluate()

    assert node1 != node2


def test_nodes_are_not_equal_if_they_dont_have_the_same_upstream_nodes(clear_default_graph):
    graph = Graph()
    node1 = Node1(name="1", graph=graph)
    node2 = Node1(name="2", graph=graph)
    node3 = Node1(name="3", graph=graph)
    node4 = Node1(name="4", graph=graph)

    node1.outputs["output"] >> node2.inputs["input"]
    node1.outputs["output"] >> node4.inputs["input"]

    assert node2 == node4

    node3.outputs["output"] >> node4.inputs["input"]

    assert node2 != node4


def test_nodes_are_not_equal_if_their_plugs_are_not_equal(clear_default_graph):
    graph = Graph()
    node1 = Node1(name="1", graph=graph)
    node2 = Node1(name="2", graph=graph)

    assert node1 == node2

    node1.inputs["input"].name = "Different plug name"

    assert node1 != node2














########################################################
############ PLUGS #####################################
########################################################


def test_plugs_can_only_be_compared_with_other_plugs(clear_default_graph):
    assert Node1(name="1").inputs["input"] != "Not a plug"


def test_plugs_are_not_equal_if_their_types_differ(clear_default_graph):
    node = Node1()
    input_ = InputPlug("plug", node)
    output = OutputPlug("plug", node)
    assert input_ != output


def test_plugs_are_not_equal_if_their_names_differ(clear_default_graph):
    node1 = Node1(name="1")
    node2 = Node1(name="2")
    plug1 = node1.inputs["input"]
    plug2 = node2.inputs["input"]

    assert plug1 == plug2

    plug1.name = "Faking a different Name"

    assert plug1 != plug2


def test_plugs_are_not_equal_if_their_values_differ(clear_default_graph):
    node1 = Node1(name="1")
    node2 = Node1(name="2")
    plug1 = node1.inputs["input"]
    plug2 = node2.inputs["input"]

    plug1.value = "value"
    plug2.value = "value"

    assert plug1 == plug2

    plug1.value = "Different value"

    assert plug1 != plug2


def test_plugs_are_not_equal_if_their_connections_differ(clear_default_graph):
    graph = Graph()
    node1 = Node1(name="1", graph=graph)
    node2 = Node1(name="2", graph=graph)
    node3 = Node1(name="3", graph=graph)

    node1.outputs["output"] >> node2.inputs["input"]
    node1.outputs["output"] >> node3.inputs["input"]

    assert node2.inputs["input"] == node3.inputs["input"]

    node2.outputs["output"] >> node3.inputs["input"]

    assert node2.inputs["input"] != node3.inputs["input"]
