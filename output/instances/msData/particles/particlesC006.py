from output.models.ms_data.particles.particles_c006_xsd.particles_c006 import AnyType
from output.models.ms_data.particles.particles_c006_xsd.particles_c006 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        AnyType(
            any_element=[
                AnyElement(
                    qname="foo",
                    text=""
                ),
            ]
        ),
    ]
)
