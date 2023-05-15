from output.models.saxon_data.id.id008_xsd.id008 import Doc
from output.models.saxon_data.id.id008_xsd.id008 import Node
from output.models.saxon_data.id.id008_xsd.id008 import PseudoId
from output.models.saxon_data.id.id008_xsd.id008 import PseudoIdref


obj = Doc(
    node=[
        Node(
            node_or_id_or_idref=[
                PseudoId(
                    value="aaa"
                ),
                PseudoIdref(
                    value="bbb"
                ),
            ]
        ),
        Node(
            node_or_id_or_idref=[
                PseudoId(
                    value="bbb"
                ),
                PseudoIdref(
                    value="aaa"
                ),
            ]
        ),
    ]
)
