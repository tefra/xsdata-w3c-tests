from output.models.ms_data.particles.particles_jj005_xsd.particles_jj005 import Doc
from output.models.ms_data.particles.particles_jj005_xsd.particles_jj005 import R
from output.models.ms_data.particles.particles_jj005_xsd.particles_jj005_imp import ImpElem1
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        imp_elem1=[
            ImpElem1(

            ),
            ImpElem1(
                any_element=AnyElement(
                    text='testing'
                )
            ),
        ]
    )
)
