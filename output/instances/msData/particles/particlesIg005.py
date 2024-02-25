from output.models.ms_data.particles.particles_ig005_xsd.particles_ig005 import Base
from output.models.ms_data.particles.particles_ig005_xsd.particles_ig005 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    e2_or_e3_or_e4=Base.E2(
        content=AnyElement(
            text='a'
        )
    )
)
