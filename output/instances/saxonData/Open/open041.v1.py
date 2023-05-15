from output.models.saxon_data.open.open041_xsd.open041 import Alpha
from output.models.saxon_data.open.open041_xsd.open041 import Doc
from output.models.saxon_data.open.open041_xsd.open041x import Beta
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    content=[
        Alpha(

        ),
        Beta(
            open_com_element=AnyElement(
                qname="{http://open.com/}extra",
                text=""
            )
        ),
    ]
)
