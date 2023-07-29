from output.models.ms_data.particles.particles_oa011_xsd.particles_oa011 import Doc
from output.models.ms_data.particles.particles_oa011_xsd.particles_oa011 import Foo
from output.models.ms_data.particles.particles_oa011_xsd.particles_oa011 import R


obj = Doc(
    elem=R(
        any_element=[
            Foo(

            ),
            Foo(

            ),
        ]
    )
)
