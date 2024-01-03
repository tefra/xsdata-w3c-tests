from output.models.ms_data.particles.particles_ob057_xsd.particles_ob057 import Doc
from output.models.ms_data.particles.particles_ob057_xsd.particles_ob057 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        local_bar_element=[
            AnyElement(
                qname='a',
                text='',
                children=[
                    AnyElement(
                        qname='e1',
                        text=''
                    ),
                ]
            ),
        ]
    )
)
