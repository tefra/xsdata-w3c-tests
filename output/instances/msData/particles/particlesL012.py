from output.models.ms_data.particles.particles_l012_xsd.particles_l012 import B
from output.models.ms_data.particles.particles_l012_xsd.particles_l012 import Doc
from output.models.ms_data.particles.particles_l012_xsd.particles_l012 import Mixed
from output.models.ms_data.particles.particles_l012_xsd.particles_l012 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        c1_or_c2=Mixed(
            content=[
                AnyElement(
                    qname='foo',
                    text='testing'
                ),
            ]
        ),
        d1_or_d2=B.D1(
            content=AnyElement(
                text='testing'
            )
        )
    )
)
