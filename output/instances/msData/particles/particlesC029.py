from output.models.ms_data.particles.particles_c029_xsd.particles_c029 import AnyType
from output.models.ms_data.particles.particles_c029_xsd.particles_c029 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        AnyType(
            foo_bar_target_namespace_element=[
                AnyElement(
                    qname='{bar}bar',
                    text=''
                ),
            ]
        ),
    ]
)
