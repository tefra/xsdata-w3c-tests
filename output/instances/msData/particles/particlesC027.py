from output.models.ms_data.particles.particles_c027_xsd.particles_c027 import Any
from output.models.ms_data.particles.particles_c027_xsd.particles_c027 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        Any(
            local_element=[
                AnyElement(
                    qname="a",
                    text=""
                ),
                AnyElement(
                    qname="b",
                    text=""
                ),
            ]
        ),
    ]
)
