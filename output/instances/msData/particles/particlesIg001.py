from output.models.ms_data.particles.particles_ig001_xsd.particles_ig001 import Base
from output.models.ms_data.particles.particles_ig001_xsd.particles_ig001 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    e1_or_e2=Base.E2(
        content=AnyElement(
            text='a',
            attributes={
                '{http://www.w3.org/2001/XMLSchema-instance}type': '{http://www.w3.org/2001/XMLSchema}Name',
            }
        )
    )
)
