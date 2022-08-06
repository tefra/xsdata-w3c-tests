from output.models.ms_data.particles.particles_ju002_xsd.particles_ju002 import Doc
from output.models.ms_data.particles.particles_ju002_xsd.particles_ju002 import R
from output.models.ms_data.particles.particles_ju002_xsd.particles_ju002_imp import ImpElem1


obj = Doc(
    elem=R(
        local_foo_target_namespace_imported_xsd_bar_element=[],
        imp_elem1=[
            ImpElem1(
                any_element=None
            ),
            ImpElem1(
                any_element=None
            ),
        ]
    )
)
