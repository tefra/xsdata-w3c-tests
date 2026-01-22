from output.models.ms_data.particles.particles_s001_xsd.particles_s001 import Address
from output.models.ms_data.particles.particles_s001_xsd.particles_s001 import Doc
from output.models.ms_data.particles.particles_s001_xsd.particles_s001 import E3
from output.models.ms_data.particles.particles_s001_xsd.particles_s001 import R


obj = Doc(
    elem=R(
        e1='',
        e2=Address(
            street='',
            zip=''
        ),
        e3=E3(

        )
    )
)
