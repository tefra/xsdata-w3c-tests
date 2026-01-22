from output.models.ms_data.particles.particles_ig012_xsd.particles_ig012 import Base
from output.models.ms_data.particles.particles_ig012_xsd.particles_ig012 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    e1_or_e2=Base.E2(
        content=AnyElement(
            text='a'
        )
    )
)
