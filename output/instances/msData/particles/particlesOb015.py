from output.models.ms_data.particles.particles_ob015_xsd.particles_ob015 import Doc
from output.models.ms_data.particles.particles_ob015_xsd.particles_ob015 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        foo_bar_element=AnyElement(
            qname='{foo}foo',
            text='',
            children=[
                AnyElement(
                    qname='{foo}e1',
                    text=''
                ),
            ]
        )
    )
)
