from output.models.saxon_data.id.id005_xsd.id005 import Doc
from output.models.saxon_data.id.id005_xsd.id005 import Node


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
                        Node.Idrefs(
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
                Node.Id(
                    value=[
                        'ccc',
                        'ddd',
                    ]
                ),
            ],
            id_attribute=[
                'aaa',
                'bbb',
            ]
        ),
    ]
)
