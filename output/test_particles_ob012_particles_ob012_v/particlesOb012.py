from output.models.ms_data.particles.particles_ob012_xsd.particles_ob012 import Doc
from output.models.ms_data.particles.particles_ob012_xsd.particles_ob012 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        other_element=AnyElement(
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
