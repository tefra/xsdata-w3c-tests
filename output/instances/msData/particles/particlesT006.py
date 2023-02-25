from output.models.ms_data.particles.particles_t006_xsd.particles_t006 import Doc
from output.models.ms_data.particles.particles_t006_xsd.particles_t006 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        c1_or_c2_or_c3=[
            AnyElement(
                qname="c1",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
        ],
        foo=""
    )
)
