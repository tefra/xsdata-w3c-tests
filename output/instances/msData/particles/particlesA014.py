from output.models.ms_data.particles.particles_a014_xsd.particles_a014 import Doc
from output.models.ms_data.particles.particles_a014_xsd.particles_a014 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        any_element=[
            AnyElement(
                qname="{bar}anything",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
            AnyElement(
                qname="{bar}anything",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
        ]
    )
)
