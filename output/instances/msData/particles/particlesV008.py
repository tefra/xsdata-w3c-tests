from output.models.ms_data.particles.particles_v008_xsd.particles_v008 import Doc
from output.models.ms_data.particles.particles_v008_xsd.particles_v008 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        e1_or_e2=[
            AnyElement(
                qname="e1",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
            AnyElement(
                qname="e2",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
        ]
    )
)
