from output.models.ms_data.particles.particles_c045_xsd.particles_c045 import AnyType
from output.models.ms_data.particles.particles_c045_xsd.particles_c045 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        AnyType(
            foo_target_namespace_bar_local_element=[
                AnyElement(
                    qname='foo',
                    text=''
                ),
            ]
        ),
    ]
)
