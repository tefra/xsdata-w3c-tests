from output.models.ms_data.particles.particles_c002_xsd.particles_c002 import Doc
from output.models.ms_data.particles.particles_c002_xsd.particles_c002 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        Elem(
            any_element=AnyElement(
                qname="{http://xsdtesting}a",
                text="",
                tail=None,
                children=[],
                attributes={}
            )
        ),
    ]
)
