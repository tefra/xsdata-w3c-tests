from output.models.ms_data.particles.particles_ob022_xsd.particles_ob022 import Doc
from output.models.ms_data.particles.particles_ob022_xsd.particles_ob022 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        local_element=AnyElement(
            qname='e1',
            text=''
        )
    )
)
