from output.models.ms_data.particles.particles_q020_xsd.particles_q020 import Doc
from output.models.ms_data.particles.particles_q020_xsd.particles_q020 import R
from output.models.ms_data.particles.particles_q020_xsd.particles_q020_imp import Bar


obj = Doc(
    elem=R(
        foo="",
        other_element=[],
        bar=[
            Bar(
                any_element=None
            ),
            Bar(
                any_element=None
            ),
        ]
    )
)
