from output.models.ms_data.particles.particles_c008_xsd.particles_c008 import Any
from output.models.ms_data.particles.particles_c008_xsd.particles_c008 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        Any(
            other_element=[
                AnyElement(
                    qname="{bar}a",
                    text=""
                ),
            ]
        ),
    ]
)
