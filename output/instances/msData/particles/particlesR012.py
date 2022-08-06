from output.models.ms_data.particles.particles_r012_xsd.particles_r012 import Doc
from output.models.ms_data.particles.particles_r012_xsd.particles_r012 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        foo="",
        any_element=[],
        e1_or_e2=[
            AnyElement(
                qname="e2",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
            AnyElement(
                qname="e1",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
        ]
    )
)
