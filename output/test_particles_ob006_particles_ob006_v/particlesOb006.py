from output.models.ms_data.particles.particles_ob006_xsd.particles_ob006 import Doc
from output.models.ms_data.particles.particles_ob006_xsd.particles_ob006 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        foo_bar_element=AnyElement(
            qname='{bar}bar',
            text='',
            children=[
                AnyElement(
                    qname='{bar}e1',
                    text=''
                ),
            ]
        )
    )
)
