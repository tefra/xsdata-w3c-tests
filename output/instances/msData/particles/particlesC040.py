from output.models.ms_data.particles.particles_c040_xsd.particles_c040 import AnyType
from output.models.ms_data.particles.particles_c040_xsd.particles_c040 import Doc
from output.models.ms_data.particles.particles_c040_xsd.particles_c040 import Foo


obj = Doc(
    elem=[
        AnyType(
            target_namespace_local_element=[
                Foo(

                ),
            ]
        ),
    ]
)
