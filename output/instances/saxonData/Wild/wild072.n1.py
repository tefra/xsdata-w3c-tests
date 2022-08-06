from output.models.saxon_data.wild.wild073_xsd.wild073 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    a_element=None,
    a="",
    b=None,
    c=None,
    any_element=[
        AnyElement(
            qname="a",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
    ]
)
