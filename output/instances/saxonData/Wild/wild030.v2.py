from output.models.saxon_data.wild.wild030_xsd.wild030 import QuietComputer
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = DerivedElement(
    qname="computer",
    value=QuietComputer(
        cpu="Intel",
        memory="4Gb",
        monitor="17inch",
        speaker=None,
        any_element=[
            AnyElement(
                qname="disk",
                text="Seagate",
                tail=None,
                children=[],
                attributes={}
            ),
            AnyElement(
                qname="mouse",
                text="USB",
                tail=None,
                children=[],
                attributes={}
            ),
        ]
    ),
    type="quietComputer"
)
