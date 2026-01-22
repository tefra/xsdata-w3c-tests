from output.models.ms_data.particles.particles_c041_xsd.particles_c041 import AnyType
from output.models.ms_data.particles.particles_c041_xsd.particles_c041 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        AnyType(
            target_namespace_local_element=[
                AnyElement(
                    qname='foo',
                    text=''
                ),
            ]
        ),
    ]
)
