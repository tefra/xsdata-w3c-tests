from output.models.ms_data.particles.particles_ig014_xsd.particles_ig014 import Base
from output.models.ms_data.particles.particles_ig014_xsd.particles_ig014 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    e1_or_e2=Base.E2(
        content=AnyElement(
            text='a'
        )
    )
)
