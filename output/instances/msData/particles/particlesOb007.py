from output.models.ms_data.particles.particles_ob007_xsd.particles_ob007 import Doc
from output.models.ms_data.particles.particles_ob007_xsd.particles_ob007 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        any_element=AnyElement(
            qname="{foo}foo",
            text="",
            tail=None,
            children=[
                AnyElement(
                    qname="{foo}e1",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                ),
            ],
            attributes={}
        ),
        local_foo_bar_target_namespace_element=None
    )
)
