from __future__ import print_function

from flowpipe import Graph, Node


@Node(outputs=["output"])
def Node1(input):
    pass


def test_plugs_can_only_be_compared_with_other_plugs(clear_default_graph):
    assert Node1(name="1").inputs["input"] != "Not a plug"