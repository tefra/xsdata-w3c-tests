from output.models.ms_data.particles.particles_l012_xsd.particles_l012 import Doc
from output.models.ms_data.particles.particles_l012_xsd.particles_l012 import NotMixed
from output.models.ms_data.particles.particles_l012_xsd.particles_l012 import R


obj = Doc(
    elem=R(
        c1=NotMixed(
            foo='testing'
        ),
        d1='testing'
    )
)
