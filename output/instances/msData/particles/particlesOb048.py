from output.models.ms_data.particles.particles_ob048_xsd.particles_ob048 import Doc
from output.models.ms_data.particles.particles_ob048_xsd.particles_ob048 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        foo_bar_element=AnyElement(
            qname="{bar}e1",
            text=""
        )
    )
)
