from output.models.ms_data.particles.particles_ig015_xsd.particles_ig015 import Base
from output.models.ms_data.particles.particles_ig015_xsd.particles_ig015 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    e1_or_e2=Base.E2(
        content=AnyElement(
            text='a'
        )
    )
)
