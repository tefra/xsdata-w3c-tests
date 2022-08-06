from output.models.saxon_data.open.open041_xsd.open041 import Alpha
from output.models.saxon_data.open.open041_xsd.open041 import Doc
from output.models.saxon_data.open.open041_xsd.open041x import Beta
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Doc(
    content=[
        DerivedElement(
            qname="a",
            value=Alpha(

            ),
            type="alpha"
        ),
        DerivedElement(
            qname="b",
            value=Beta(
                open_com_element=AnyElement(
                    qname="{http://open.com/}extra",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                )
            ),
            type="beta"
        ),
    ]
)
