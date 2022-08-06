from output.models.saxon_data.open.open043_xsd.open043 import Beta
from output.models.saxon_data.open.open043_xsd.open043 import Doc
from output.models.saxon_data.open.open043_xsd.open043x import Alpha
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

            ),
            type="beta"
        ),
    ]
)
