from output.models.ms_data.particles.particles_r017_xsd.particles_r017 import Doc
from output.models.ms_data.particles.particles_r017_xsd.particles_r017 import R
from output.models.ms_data.particles.particles_r017_xsd.particles_r017_imp import ImpElem2


obj = Doc(
    elem=R(
        foo="",
        any_element=[],
        imp_elem1=None,
        imp_elem2=ImpElem2(
            any_element=None
        )
    )
)
