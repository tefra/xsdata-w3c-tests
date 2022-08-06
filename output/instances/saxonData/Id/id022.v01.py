from output.models.saxon_data.id.id022_xsd.id022 import Doc
from output.models.saxon_data.id.id022_xsd.id022 import Para


obj = Doc(
    para=[
        Para(
            value="",
            key="alpha",
            ref=[]
        ),
        Para(
            value="",
            key="beta",
            ref=[
                "alpha",
            ]
        ),
        Para(
            value="",
            key="gamma",
            ref=[
                "beta",
            ]
        ),
    ]
)
