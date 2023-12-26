from output.models.saxon_data.subsgroup.subsgroup001_xsd.subsgroup001 import Back
from output.models.saxon_data.subsgroup.subsgroup001_xsd.subsgroup001 import Body
from output.models.saxon_data.subsgroup.subsgroup001_xsd.subsgroup001 import Doc


obj = Doc(
    body=Body(
        para=[
            'one',
            'two',
        ]
    ),
    back=Back(
        para=[
            'one',
            'two',
        ]
    )
)
