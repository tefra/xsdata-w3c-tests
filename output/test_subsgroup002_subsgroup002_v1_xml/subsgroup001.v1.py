from output.models.saxon_data.subsgroup.subsgroup002_xsd.subsgroup002 import Back
from output.models.saxon_data.subsgroup.subsgroup002_xsd.subsgroup002 import Body
from output.models.saxon_data.subsgroup.subsgroup002_xsd.subsgroup002 import Doc
from output.models.saxon_data.subsgroup.subsgroup002_xsd.subsgroup002 import Para


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
