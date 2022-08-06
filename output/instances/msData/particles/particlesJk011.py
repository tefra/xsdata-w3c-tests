from output.models.ms_data.particles.particles_jk011_xsd.particles_jk011 import Doc
from output.models.ms_data.particles.particles_jk011_xsd.particles_jk011 import R
from output.models.ms_data.particles.particles_jk011_xsd.particles_jk011_imp import ImpElem1
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
