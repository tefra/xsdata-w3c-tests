from output.models.saxon_data.id.id003_xsd.id003 import Doc
from output.models.saxon_data.id.id003_xsd.id003 import Node


obj = Doc(
    node=[
        Node(
            node_or_id=[
                'zzz',
                Node(
                    id_one='ccc',
                    any_attributes={
                        'id-two': 'ddd',
                    }
                ),
                Node(
                    id_one='eee',
                    any_attributes={
                        'id-two': 'eee',
                    }
                ),
                'zzz',
                'aaa',
            ],
            id_one='aaa',
            any_attributes={
                'id-two': 'bbb',
            }
        ),
    ]
)
