from output.models.ms_data.particles.particles_ob057_xsd.particles_ob057 import Doc
from output.models.ms_data.particles.particles_ob057_xsd.particles_ob057 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        local_foo_bar_target_namespace_element=[
            AnyElement(
                qname="a",
                text="",
                tail=None,
                children=[
                    AnyElement(
                        qname="e1",
                        text="",
                        tail=None,
                        children=[],
                        attributes={}
                    ),
                ],
                attributes={}
            ),
        ],
        local_bar_element=[]
    )
)
