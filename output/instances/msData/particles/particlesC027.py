from output.models.ms_data.particles.particles_c027_xsd.particles_c027 import AnyType
from output.models.ms_data.particles.particles_c027_xsd.particles_c027 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        AnyType(
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
