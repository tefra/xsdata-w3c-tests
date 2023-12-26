from output.models.ms_data.particles.particles_a010_xsd.particles_a010 import Doc
from output.models.ms_data.particles.particles_a010_xsd.particles_a010 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        e1_or_e2=[
            AnyElement(
                qname='e2',
                text=''
            ),
            AnyElement(
                qname='e1',
                text=''
            ),
        ]
    )
)
