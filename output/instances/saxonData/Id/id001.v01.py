from output.models.saxon_data.id.id002_xsd.id002 import Doc
from output.models.saxon_data.id.id002_xsd.id002 import Para


obj = Doc(
    para=[
        Para(
            id_one='aaa',
            any_attributes={
                'id-two': 'bbb',
            }
        ),
        Para(
            id_one='ccc',
            any_attributes={
                'id-two': 'ddd',
            }
        ),
        Para(
            id_one='eee',
            any_attributes={
                'id-two': 'eee',
            }
        ),
    ]
)
