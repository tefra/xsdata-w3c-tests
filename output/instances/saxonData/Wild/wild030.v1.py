from output.models.saxon_data.wild.wild030_xsd.wild030 import Computer
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Computer(
    cpu="Intel",
    memory="4Gb",
    monitor="17inch",
    speaker="loud",
    any_element=[
        AnyElement(
            qname="disk",
            text="Seagate"
        ),
        AnyElement(
            qname="mouse",
            text="USB"
        ),
    ]
)
