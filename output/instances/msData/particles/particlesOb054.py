from output.models.ms_data.particles.particles_ob054_xsd.particles_ob054 import Doc
from output.models.ms_data.particles.particles_ob054_xsd.particles_ob054 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        local_foo_bar_target_namespace_element=AnyElement(
            qname="{foo}e1",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        foo_bar_element=None
    )
)
