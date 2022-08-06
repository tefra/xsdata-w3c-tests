from output.models.ms_data.particles.particles_s011_xsd.particles_s011 import Address1
from output.models.ms_data.particles.particles_s011_xsd.particles_s011 import Doc
from output.models.ms_data.particles.particles_s011_xsd.particles_s011 import R


obj = Doc(
    elem=R(
        e1="",
        e2=Address1(
            street=[
                "",
                "",
            ],
            zip=""
        )
    )
)
