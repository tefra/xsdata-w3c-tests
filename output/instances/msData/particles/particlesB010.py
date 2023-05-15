from output.models.ms_data.particles.particles_b010_xsd.particles_b010 import Doc
from output.models.ms_data.particles.particles_b010_xsd.particles_b010 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        choice=[
            AnyElement(
                qname="e4",
                text=""
            ),
            AnyElement(
                qname="e1",
                text=""
            ),
        ]
    )
)
