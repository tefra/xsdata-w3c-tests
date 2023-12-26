from output.models.ms_data.particles.particles_t004_xsd.particles_t004 import Doc
from output.models.ms_data.particles.particles_t004_xsd.particles_t004 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        c1_or_c2_or_c3=[
            AnyElement(
                qname='c2',
                text=''
            ),
            AnyElement(
                qname='c2',
                text=''
            ),
            AnyElement(
                qname='c2',
                text=''
            ),
        ],
        foo=''
    )
)
