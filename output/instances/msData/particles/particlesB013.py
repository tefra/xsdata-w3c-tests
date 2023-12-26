from output.models.ms_data.particles.particles_b013_xsd.particles_b013 import Doc
from output.models.ms_data.particles.particles_b013_xsd.particles_b013 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        any_element=[
            AnyElement(
                qname='{foo}b',
                text=''
            ),
        ]
    )
)
