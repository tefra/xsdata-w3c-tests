from output.models.ms_data.particles.particles_v007_xsd.particles_v007 import Doc
from output.models.ms_data.particles.particles_v007_xsd.particles_v007 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        e1_or_e2=[
            AnyElement(
                qname='e1',
                text=''
            ),
        ]
    )
)
