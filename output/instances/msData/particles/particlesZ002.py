from output.models.ms_data.particles.particles_z002_xsd.particles_z002 import Derived1
from output.models.ms_data.particles.particles_z002_xsd.particles_z002 import Derived2
from output.models.ms_data.particles.particles_z002_xsd.particles_z002 import Derived3
from output.models.ms_data.particles.particles_z002_xsd.particles_z002 import Doc


obj = Doc(
    elem1=Derived1(

    ),
    elem2=Derived2(
        bar="123"
    ),
    elem3=Derived3(
        foo="123"
    )
)
