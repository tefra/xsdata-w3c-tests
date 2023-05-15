from output.models.ms_data.particles.particles_ob042_xsd.particles_ob042 import Doc
from output.models.ms_data.particles.particles_ob042_xsd.particles_ob042 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        foo_bar_element=[
            AnyElement(
                qname="{foo}e1",
                text=""
            ),
            AnyElement(
                qname="{bar}e1",
                text=""
            ),
        ]
    )
)
