from output.models.ms_data.particles.particles_v012_xsd.particles_v012 import Doc
from output.models.ms_data.particles.particles_v012_xsd.particles_v012 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        e1_or_e2_or_e3=[
            AnyElement(
                qname='e1',
                text=''
            ),
            AnyElement(
                qname='e2',
                text=''
            ),
        ]
    )
)
