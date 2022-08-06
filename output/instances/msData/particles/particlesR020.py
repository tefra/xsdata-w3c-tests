from output.models.ms_data.particles.particles_r020_xsd.particles_r020 import Doc
from output.models.ms_data.particles.particles_r020_xsd.particles_r020 import R
from output.models.ms_data.particles.particles_r020_xsd.particles_r020_imp import ImpElem2


obj = Doc(
    elem=R(
        foo="",
        other_element=[],
        imp_elem1=None,
        imp_elem2=ImpElem2(
            any_element=None
        )
    )
)
