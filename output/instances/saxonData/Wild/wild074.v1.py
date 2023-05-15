from output.models.saxon_data.wild.wild074_xsd.wild074 import A1
from output.models.saxon_data.wild.wild074_xsd.wild074 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=AnyElement(
        children=[
            AnyElement(
                qname="zizz",
                text=""
            ),
            AnyElement(
                qname="d",
                text=""
            ),
            AnyElement(
                qname="e",
                text=""
            ),
        ]
    ),
    a_or_a=A1(

    ),
    b="",
    c=""
)
