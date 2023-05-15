from output.models.saxon_data.id.id022_xsd.id022 import Doc
from output.models.saxon_data.id.id022_xsd.id022 import Para


obj = Doc(
    para=[
        Para(
            key="alpha"
        ),
        Para(
            key="beta",
            ref=[
                "alpha",
            ]
        ),
        Para(
            key="gamma",
            ref=[
                "beta",
            ]
        ),
    ]
)
