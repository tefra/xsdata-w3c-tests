from output.models.saxon_data.open.open040_xsd.open040 import Alpha
from output.models.saxon_data.open.open040_xsd.open040 import Doc
from output.models.saxon_data.open.open040_xsd.open040x import Beta
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Doc(
    content=[
        DerivedElement(
            qname="a",
            value=Alpha(
                open_com_element=AnyElement(
                    qname="{http://open.com/}extra",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                )
            ),
            type="alpha"
        ),
        DerivedElement(
            qname="b",
            value=Beta(

            ),
            type="beta"
        ),
    ]
)
