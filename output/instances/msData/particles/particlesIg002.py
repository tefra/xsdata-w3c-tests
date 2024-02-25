from output.models.ms_data.particles.particles_ig002_xsd.particles_ig002 import Base
from output.models.ms_data.particles.particles_ig002_xsd.particles_ig002 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    e1_or_e2=Base.E2(
        content=AnyElement(
            text='12',
            attributes={
                '{http://www.w3.org/2001/XMLSchema-instance}type': '{http://www.w3.org/2001/XMLSchema}int',
            }
        )
    )
)
