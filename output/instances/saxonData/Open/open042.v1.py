from output.models.saxon_data.open.open042_xsd.open042 import Beta
from output.models.saxon_data.open.open042_xsd.open042 import Doc
from output.models.saxon_data.open.open042_xsd.open042x import Alpha
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    content=[
        Alpha(

        ),
        Beta(
            other_element=AnyElement(
                qname="{http://open.com/}extra",
                text=""
            )
        ),
    ]
)
