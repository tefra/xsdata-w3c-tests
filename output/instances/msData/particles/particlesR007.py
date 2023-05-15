from output.models.ms_data.particles.particles_r007_xsd.particles_r007 import Doc
from output.models.ms_data.particles.particles_r007_xsd.particles_r007 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        foo="",
        e1_or_e2=[
            AnyElement(
                qname="e1",
                text=""
            ),
            AnyElement(
                qname="e1",
                text=""
            ),
        ]
    )
)
