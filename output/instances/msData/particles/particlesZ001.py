from output.models.ms_data.particles.particles_z001_xsd.particles_z001 import Derived
from output.models.ms_data.particles.particles_z001_xsd.particles_z001 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Derived(
        annotation="",
        element_or_any=[
            AnyElement(
                qname="element",
                text=""
            ),
            AnyElement(
                qname="element",
                text=""
            ),
            AnyElement(
                qname="element",
                text=""
            ),
            AnyElement(
                qname="element",
                text=""
            ),
        ]
    )
)
