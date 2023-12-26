from output.models.ms_data.particles.particles_b009_xsd.particles_b009 import Doc
from output.models.ms_data.particles.particles_b009_xsd.particles_b009 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        choice=[
            AnyElement(
                qname='e1',
                text=''
            ),
        ]
    )
)
