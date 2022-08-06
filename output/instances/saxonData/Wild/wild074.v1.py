from output.models.saxon_data.wild.wild074_xsd.wild074 import A1
from output.models.saxon_data.wild.wild074_xsd.wild074 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=AnyElement(
        qname=None,
        text=None,
        tail=None,
        children=[
            AnyElement(
                qname="zizz",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
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
        ],
        attributes={}
    ),
    a_element=A1(
        any_element=None
    ),
    a=None,
    b="",
    c=""
)
