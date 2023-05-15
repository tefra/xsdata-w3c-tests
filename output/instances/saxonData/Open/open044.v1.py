from output.models.saxon_data.open.open044_xsd.open044 import Beta
from output.models.saxon_data.open.open044_xsd.open044 import Doc
from output.models.saxon_data.open.open044_xsd.open044x import Alpha


obj = Doc(
    content=[
        Alpha(

        ),
        Beta(
            other_attributes={
                "{http://www.w3.org/XML/1998/namespace}lang": "jp",
            }
        ),
    ]
)
