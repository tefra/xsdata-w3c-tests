from output.models.saxon_data.wild.wild047_xsd.wild047 import Computer
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Computer(
    name="mine",
    local_element=[
        AnyElement(
            qname="f",
            text=""
        ),
    ]
)
