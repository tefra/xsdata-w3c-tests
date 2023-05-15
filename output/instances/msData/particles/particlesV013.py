from output.models.ms_data.particles.particles_v013_xsd.particles_v013 import Doc
from output.models.ms_data.particles.particles_v013_xsd.particles_v013 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        e1_or_e2_or_e3=[
            AnyElement(
                qname="e2",
                text=""
            ),
            AnyElement(
                qname="e3",
                text=""
            ),
        ]
    )
)
