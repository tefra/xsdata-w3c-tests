from output.models.ms_data.particles.particles_q016_xsd.particles_q016 import Doc
from output.models.ms_data.particles.particles_q016_xsd.particles_q016 import R
from output.models.ms_data.particles.particles_q016_xsd.particles_q016_imp import Foo


obj = Doc(
    elem=R(
        xsdtesting_foo="",
        any_element=[],
        foo=[
            Foo(
                any_element=None
            ),
            Foo(
                any_element=None
            ),
        ]
    )
)