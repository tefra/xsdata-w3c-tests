from output.models.ms_data.particles.particles_q017_xsd.particles_q017 import Doc
from output.models.ms_data.particles.particles_q017_xsd.particles_q017 import R
from output.models.ms_data.particles.particles_q017_xsd.particles_q017_imp import Foo


obj = Doc(
    elem=R(
        foo="",
        any_element=[],
        foo_foo=[
            Foo(
                any_element=None
            ),
            Foo(
                any_element=None
            ),
        ]
    )
)
