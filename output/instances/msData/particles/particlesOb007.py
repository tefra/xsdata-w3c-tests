from output.models.ms_data.particles.particles_ob007_xsd.particles_ob007 import Doc
from output.models.ms_data.particles.particles_ob007_xsd.particles_ob007 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        any_element=AnyElement(
            qname="{foo}foo",
            text="",
            children=[
                AnyElement(
                    qname="{foo}e1",
                    text=""
                ),
            ]
        )
    )
)
