from output.models.ms_data.particles.particles_oa001_xsd.particles_oa001 import Doc
from output.models.ms_data.particles.particles_oa001_xsd.particles_oa001 import Foo
from output.models.ms_data.particles.particles_oa001_xsd.particles_oa001 import R


obj = Doc(
    elem=R(
        any_element=Doc(
            elem=R(
                any_element=Foo(

                )
            )
        )
    )
)
