from output.models.saxon_data.id.id009_xsd.id009 import Doc
from output.models.saxon_data.id.id009_xsd.id009 import Node


obj = Doc(
    node=[
        Node(
            node_or_id_or_idref=[
                Node.Id(
                    value='aaa'
                ),
                Node.Idref(
                    value='ccc'
                ),
            ]
        ),
        Node(
            node_or_id_or_idref=[
                Node.Id(
                    value='bbb'
                ),
                Node.Idref(
                    value='aaa'
                ),
            ]
        ),
        Node(
            node_or_id_or_idref=[
                Node.Id(
                    value='ccc'
                ),
                Node.Idref(
                    value='bbb'
                ),
            ]
        ),
        Node(
            node_or_id_or_idref=[
                Node.Id(
                    value=None
                ),
                Node.Idref(
                    value=None
                ),
            ]
        ),
    ]
)
