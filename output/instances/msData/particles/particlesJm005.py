from output.models.ms_data.particles.particles_jm005_xsd.particles_jm005 import Doc
from output.models.ms_data.particles.particles_jm005_xsd.particles_jm005 import R
from output.models.ms_data.particles.particles_jm005_xsd.particles_jm005_imp import ImpElem1
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        foo_imported_xsd_bar_element=[],
        imp_elem1=[
            ImpElem1(
                any_element=AnyElement(
                    qname=None,
                    text="testing",
                    tail=None,
                    children=[],
                    attributes={}
                )
            ),
            ImpElem1(
                any_element=AnyElement(
                    qname=None,
                    text="testing",
                    tail=None,
                    children=[],
                    attributes={}
                )
            ),
        ]
    )
)
