from output.models.saxon_data.subsgroup.subsgroup001_xsd.subsgroup001 import Back
from output.models.saxon_data.subsgroup.subsgroup001_xsd.subsgroup001 import Body
from output.models.saxon_data.subsgroup.subsgroup001_xsd.subsgroup001 import Doc
from output.models.saxon_data.subsgroup.subsgroup001_xsd.subsgroup001 import Para


obj = Doc(
    body=Body(
        para=[
            Para(
                value='one'
            ),
            Para(
                value='two'
            ),
        ]
    ),
    back=Back(
        para=[
            Para(
                value='one'
            ),
            Para(
                value='two'
            ),
        ]
    )
)
