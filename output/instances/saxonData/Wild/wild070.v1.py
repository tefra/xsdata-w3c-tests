from output.models.saxon_data.wild.wild070_xsd.wild070 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    a="",
    b="",
    c="",
    any_element=[
        AnyElement(
            qname="d",
            text=""
        ),
        AnyElement(
            qname="e",
            text=""
        ),
    ]
)
