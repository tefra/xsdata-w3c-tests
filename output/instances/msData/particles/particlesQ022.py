from output.models.ms_data.particles.particles_q022_xsd.particles_q022 import Doc
from output.models.ms_data.particles.particles_q022_xsd.particles_q022 import R
from output.models.ms_data.particles.particles_q022_xsd.particles_q022_imp import Foo


obj = Doc(
    elem=R(
        xsdtesting_foo="",
        local_element=[],
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