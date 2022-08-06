from output.models.ms_data.particles.particles_c041_xsd.particles_c041 import Any
from output.models.ms_data.particles.particles_c041_xsd.particles_c041 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        Any(
            target_namespace_local_element=[
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
