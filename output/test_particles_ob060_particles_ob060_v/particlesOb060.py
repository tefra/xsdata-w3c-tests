from output.models.ms_data.particles.particles_ob060_xsd.particles_ob060 import Doc
from output.models.ms_data.particles.particles_ob060_xsd.particles_ob060 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        bar_element=AnyElement(
            qname='{bar}e1',
            text=''
        )
    )
)
