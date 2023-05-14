from output.models.saxon_data.wild.wild071_xsd.wild071 import A1
from output.models.saxon_data.wild.wild071_xsd.wild071 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    a_or_a=A1(
        any_element=None
    ),
    b="",
    c="",
    any_element=[
        AnyElement(
            qname="d",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="e",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
    ]
)
