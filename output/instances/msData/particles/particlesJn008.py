from output.models.ms_data.particles.particles_jn008_xsd.particles_jn008 import Doc
from output.models.ms_data.particles.particles_jn008_xsd.particles_jn008 import R
from output.models.ms_data.particles.particles_jn008_xsd.particles_jn008_imp import ImpElem1


obj = Doc(
    elem=R(
        foo_imported_xsd_bar_element=None,
        imp_elem1=ImpElem1(
            any_element=None
        )
    )
)
