from output.models.ms_data.particles.particles_c040_xsd.particles_c040 import AnyType
from output.models.ms_data.particles.particles_c040_xsd.particles_c040 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        AnyType(
            target_namespace_local_element=[
                AnyElement(
                    qname="{http://xsdtesting}foo",
                    text=""
                ),
            ]
        ),
    ]
)
