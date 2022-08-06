from output.models.ms_data.particles.particles_m035_xsd.particles_m035 import Doc
from output.models.ms_data.particles.particles_m035_xsd.particles_m035 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        choice=[
            AnyElement(
                qname="d2",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
            AnyElement(
                qname="d2",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
        ]
    )
)
