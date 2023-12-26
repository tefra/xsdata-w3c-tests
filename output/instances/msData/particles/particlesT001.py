from output.models.ms_data.particles.particles_t001_xsd.particles_t001 import Doc
from output.models.ms_data.particles.particles_t001_xsd.particles_t001 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        c1_or_c2=AnyElement(
            qname='c1',
            text=''
        ),
        foo=''
    )
)
