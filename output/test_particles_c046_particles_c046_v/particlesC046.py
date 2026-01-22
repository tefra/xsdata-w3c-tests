from output.models.ms_data.particles.particles_c046_xsd.particles_c046 import AnyType
from output.models.ms_data.particles.particles_c046_xsd.particles_c046 import Doc
from output.models.ms_data.particles.particles_c046_xsd.particles_c046 import Foo


obj = Doc(
    elem=[
        AnyType(
            foo_target_namespace_bar_local_element=[
                Foo(

                ),
            ]
        ),
    ]
)
