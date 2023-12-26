from output.models.saxon_data.id.id004_xsd.id004 import Doc
from output.models.saxon_data.id.id004_xsd.id004 import Node


obj = Doc(
    node=[
        Node(
            node_or_id=[
                Node(
                    id_one=[
                        'ccc',
                        'ccc',
                    ],
                    any_attributes={
                        'id-two': 'ddd ddd',
                    }
                ),
                Node(
                    id_one=[
                        'eee',
                    ],
                    any_attributes={
                        'id-two': '',
                    }
                ),
                [
                    'zzz',
                    'bbb',
                ],
                [
                    'aaa',
                    'zzz',
                    'bbb',
                ],
            ],
            any_attributes={
                'id': 'aaa bbb',
            }
        ),
    ]
)
