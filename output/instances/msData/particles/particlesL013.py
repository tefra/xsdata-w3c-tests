from output.models.ms_data.particles.particles_l013_xsd.particles_l013 import B
from output.models.ms_data.particles.particles_l013_xsd.particles_l013 import Doc
from output.models.ms_data.particles.particles_l013_xsd.particles_l013 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        c1_or_c2=B.C1(

        ),
        d1_or_d2=B.D1(
            content=AnyElement(
                text='testing'
            )
        )
    )
)
