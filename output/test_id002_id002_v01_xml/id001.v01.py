from output.models.saxon_data.id.id002_xsd.id002 import Doc
from output.models.saxon_data.id.id002_xsd.id002 import Para


obj = Doc(
    para=[
        Para(
            value='',
            id_one='aaa',
            any_attributes={
                'id-two': 'bbb',
            }
        ),
        Para(
            value='',
            id_one='ccc',
            any_attributes={
                'id-two': 'ddd',
            }
        ),
        Para(
            value='',
            id_one='eee',
            any_attributes={
                'id-two': 'eee',
            }
        ),
    ]
)
