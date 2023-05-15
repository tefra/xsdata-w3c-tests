from output.models.ms_data.particles.particles_m002_xsd.particles_m002 import Doc
from output.models.ms_data.particles.particles_m002_xsd.particles_m002 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        choice=[
            AnyElement(
                qname="c1",
                text=""
            ),
            AnyElement(
                qname="c1",
                text=""
            ),
        ]
    )
)
