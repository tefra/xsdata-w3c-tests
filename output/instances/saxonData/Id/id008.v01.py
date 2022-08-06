from output.models.saxon_data.id.id008_xsd.id008 import Doc
from output.models.saxon_data.id.id008_xsd.id008 import Node
from output.models.saxon_data.id.id008_xsd.id008 import PseudoId
from output.models.saxon_data.id.id008_xsd.id008 import PseudoIdref


obj = Doc(
    node=[
        Node(
            node_or_id_or_idref=[
                PseudoId(
                    value="aaa",
                    a=None
                ),
                PseudoIdref(
                    value="bbb",
                    a=None
                ),
            ]
        ),
        Node(
            node_or_id_or_idref=[
                PseudoId(
                    value="bbb",
                    a=None
                ),
                PseudoIdref(
                    value="aaa",
                    a=None
                ),
            ]
        ),
    ]
)
