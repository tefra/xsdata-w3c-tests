from output.models.ms_data.particles.particles_jm004_xsd.particles_jm004 import Doc
from output.models.ms_data.particles.particles_jm004_xsd.particles_jm004 import R
from output.models.ms_data.particles.particles_jm004_xsd.particles_jm004_imp import ImpElem1
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        foo_imported_xsd_bar_element=None,
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
