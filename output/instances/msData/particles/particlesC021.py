from output.models.ms_data.particles.particles_c021_xsd.particles_c021 import AnyType
from output.models.ms_data.particles.particles_c021_xsd.particles_c021 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        AnyType(
            target_namespace_element=[
                AnyElement(
                    qname="{http://xsdtesting}foo",
                    text=""
                ),
            ]
        ),
    ]
)
