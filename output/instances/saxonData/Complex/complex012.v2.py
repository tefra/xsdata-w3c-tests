from output.models.saxon_data.complex.complex012_xsd.complex012 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    content=[
        AnyElement(
            qname="e",
            text=""
        ),
    ]
)
