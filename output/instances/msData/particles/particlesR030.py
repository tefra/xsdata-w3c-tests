from output.models.ms_data.particles.particles_r030_xsd.particles_r030 import Doc
from output.models.ms_data.particles.particles_r030_xsd.particles_r030 import R
from output.models.ms_data.particles.particles_r030_xsd.particles_r030_imp import ImpElem1


obj = Doc(
    elem=R(
        foo="",
        any_element=None,
        imp_elem1=ImpElem1(
            any_element=None
        )
    )
)