from output.models.ms_data.particles.particles_ij001_xsd.particles_ij001 import B
from output.models.ms_data.particles.particles_ij001_xsd.particles_ij001 import Doc
from output.models.ms_data.particles.particles_ij001_xsd.particles_ij001 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        c1_or_c2=[
            B.C1(
                content=AnyElement(
                    text='1',
                    attributes={
                        '{http://www.w3.org/2001/XMLSchema-instance}type': '{http://www.w3.org/2001/XMLSchema}int',
                    }
                )
            ),
        ]
    )
)
