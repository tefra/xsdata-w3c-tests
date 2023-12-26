from output.models.ms_data.particles.particles_c004_xsd.particles_c004 import Doc
from output.models.ms_data.particles.particles_c004_xsd.particles_c004 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        Elem(
            any_element=[
                AnyElement(
                    qname='{foo}foo',
                    text=''
                ),
            ]
        ),
    ]
)
