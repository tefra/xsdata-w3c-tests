from output.models.ms_data.particles.particles_c037_xsd.particles_c037 import AnyType
from output.models.ms_data.particles.particles_c037_xsd.particles_c037 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        AnyType(
            foo_local_element=[
                AnyElement(
                    qname="foo",
                    text=""
                ),
            ]
        ),
    ]
)
