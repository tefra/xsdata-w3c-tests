from output.models.ms_data.particles.particles_jk013_xsd.particles_jk013 import Doc
from output.models.ms_data.particles.particles_jk013_xsd.particles_jk013 import R
from output.models.ms_data.particles.particles_jk013_xsd.particles_jk013_imp import ImpElem1
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        other_element=None,
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