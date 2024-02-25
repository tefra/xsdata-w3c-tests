from output.models.ms_data.particles.particles_l018_xsd.particles_l018 import B
from output.models.ms_data.particles.particles_l018_xsd.particles_l018 import Doc
from output.models.ms_data.particles.particles_l018_xsd.particles_l018 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        c1_or_c2=B.C1(
            content=AnyElement(
                text='1',
                attributes={
                    '{http://www.w3.org/2001/XMLSchema-instance}type': '{http://www.w3.org/2001/XMLSchema}int',
                }
            )
        ),
        d1_or_d2=B.D1(
            content=AnyElement(
                text='testing'
            )
        )
    )
)
