from output.models.ms_data.particles.particles_v004_xsd.particles_v004 import Doc
from output.models.ms_data.particles.particles_v004_xsd.particles_v004 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        e1_or_e2=[
            AnyElement(
                qname="e1",
                text=""
            ),
            AnyElement(
                qname="e1",
                text=""
            ),
            AnyElement(
                qname="e1",
                text=""
            ),
            AnyElement(
                qname="e2",
                text=""
            ),
            AnyElement(
                qname="e2",
                text=""
            ),
            AnyElement(
                qname="e2",
                text=""
            ),
        ]
    )
)
