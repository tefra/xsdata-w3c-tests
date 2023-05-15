from output.models.ms_data.particles.particles_t012_xsd.particles_t012 import Bar
from output.models.ms_data.particles.particles_t012_xsd.particles_t012 import Doc
from output.models.ms_data.particles.particles_t012_xsd.particles_t012 import R


obj = Doc(
    elem=R(
        c1_or_c2_or_c3=[
            Bar(
                foo="",
                att1="testing"
            ),
        ],
        foo=""
    )
)
