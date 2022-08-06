from output.models.ms_data.particles.particles_jk004_xsd.particles_jk004 import Doc
from output.models.ms_data.particles.particles_jk004_xsd.particles_jk004 import R
from output.models.ms_data.particles.particles_jk004_xsd.particles_jk004_imp import ImpElem1
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        other_element=[],
        imp_elem1=ImpElem1(
            any_element=AnyElement(
                qname=None,
                text="testing",
                tail=None,
                children=[],
                attributes={}
            )
        )
    )
)
