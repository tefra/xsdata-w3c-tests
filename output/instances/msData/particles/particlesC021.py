from output.models.ms_data.particles.particles_c021_xsd.particles_c021 import AnyType
from output.models.ms_data.particles.particles_c021_xsd.particles_c021 import Doc
from output.models.ms_data.particles.particles_c021_xsd.particles_c021 import Foo


obj = Doc(
    elem=[
        AnyType(
            target_namespace_element=[
                Foo(

                ),
            ]
        ),
    ]
)
