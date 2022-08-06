from output.models.saxon_data.id.id009_xsd.id009 import Doc
from output.models.saxon_data.id.id009_xsd.id009 import Node
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Doc(
    node=[
        Node(
            node_or_id_or_idref=[
                "aaa",
                DerivedElement(
                    qname="idref",
                    value="ccc",
                    type=None
                ),
            ]
        ),
        Node(
            node_or_id_or_idref=[
                "bbb",
                DerivedElement(
                    qname="idref",
                    value="aaa",
                    type=None
                ),
            ]
        ),
        Node(
            node_or_id_or_idref=[
                "ccc",
                DerivedElement(
                    qname="idref",
                    value="bbb",
                    type=None
                ),
            ]
        ),
        Node(
            node_or_id_or_idref=[
                None,
                DerivedElement(
                    qname="idref",
                    value=None,
                    type=None
                ),
            ]
        ),
    ]
)
