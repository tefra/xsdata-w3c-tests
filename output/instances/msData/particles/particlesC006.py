from output.models.ms_data.particles.particles_c006_xsd.particles_c006 import Any
from output.models.ms_data.particles.particles_c006_xsd.particles_c006 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        Any(
            any_element=[
                AnyElement(
                    qname="foo",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                ),
            ]
        ),
    ]
)
