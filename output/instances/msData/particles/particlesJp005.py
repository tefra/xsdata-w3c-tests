from output.models.ms_data.particles.particles_jp005_xsd.particles_jp005 import Doc
from output.models.ms_data.particles.particles_jp005_xsd.particles_jp005 import Foo
from output.models.ms_data.particles.particles_jp005_xsd.particles_jp005 import R


obj = Doc(
    elem=R(
        foo=[
            Foo(

            ),
        ]
    )
)
