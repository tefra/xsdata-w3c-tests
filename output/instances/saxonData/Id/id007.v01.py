from output.models.saxon_data.id.id007_xsd.id007 import Doc
from output.models.saxon_data.id.id007_xsd.id007 import Node
from xsdata.formats.dataclass.models.generics import DerivedElement


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
                [
                    'A002',
                    'B002',
                ],
            ]
        ),
        Node(
            node_or_mixed_a_or_mixed_b=[
                DerivedElement(
                    qname='mixedB',
                    value=[
                        'A002',
                        'B002',
                    ]
                ),
            ]
        ),
    ]
)
