from output.models.saxon_data.id.id006_xsd.id006 import Doc
from output.models.saxon_data.id.id006_xsd.id006 import Node
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Doc(
    node=[
        Node(
            node_or_id_or_idrefs=[
                Node(
                    idrefs_attribute=[
                        'bbb',
                        'ccc',
                        29,
                        'ggg',
                    ]
                ),
                Node(
                    node_or_id_or_idrefs=[
                        DerivedElement(
                            qname='idrefs',
                            value=[
                                'aaa',
                                97,
                                'ddd',
                            ]
                        ),
                    ],
                    id_attribute=[
                        'ggg',
                        23,
                    ]
                ),
                [
                    'ccc',
                    'ddd',
                ],
                [
                    12,
                ],
            ],
            id_attribute=[
                'aaa',
                23,
                'bbb',
            ]
        ),
    ]
)
