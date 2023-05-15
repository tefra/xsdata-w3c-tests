from output.models.ms_data.particles.particles_b014_xsd.particles_b014 import Doc
from output.models.ms_data.particles.particles_b014_xsd.particles_b014 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        any_element=[
            AnyElement(
                qname="{foo}a",
                text=""
            ),
            AnyElement(
                qname="{bar}d",
                text=""
            ),
        ]
    )
)
