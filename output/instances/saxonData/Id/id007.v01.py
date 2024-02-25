from output.models.saxon_data.id.id007_xsd.id007 import Doc
from output.models.saxon_data.id.id007_xsd.id007 import Node


obj = Doc(
    node=[
        Node(
            mixed_a_attribute=[
                'A001',
                'B001',
            ]
        ),
        Node(
            mixed_b_attribute=[
                'A001',
                'B001',
            ]
        ),
        Node(
            node_or_mixed_a_or_mixed_b=[
                Node.MixedA(
                    value=[
                        'A002',
                        'B002',
                    ]
                ),
            ]
        ),
        Node(
            node_or_mixed_a_or_mixed_b=[
                Node.MixedB(
                    value=[
                        'A002',
                        'B002',
                    ]
                ),
            ]
        ),
    ]
)
