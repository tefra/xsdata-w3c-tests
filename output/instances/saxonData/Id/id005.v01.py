from output.models.saxon_data.id.id005_xsd.id005 import Doc
from output.models.saxon_data.id.id005_xsd.id005 import Node
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Doc(
    node=[
        Node(
            node_or_id_or_idrefs=[
                Node(
                    idrefs_attribute=[
                        'bbb',
                        'ccc',
                        'ggg',
                    ]
                ),
                Node(
                    node_or_id_or_idrefs=[
                        DerivedElement(
                            qname='idrefs',
                            value=[
                                'aaa',
                                'ddd',
                            ]
                        ),
                    ],
                    id_attribute=[
                        'ggg',
                    ]
                ),
                [
                    'ccc',
                    'ddd',
                ],
            ],
            id_attribute=[
                'aaa',
                'bbb',
            ]
        ),
    ]
)
