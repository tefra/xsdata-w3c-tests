from output.models.ms_data.particles.particles_l018_xsd.particles_l018 import Doc
from output.models.ms_data.particles.particles_l018_xsd.particles_l018 import R
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Doc(
    elem=R(
        c1_or_c2=DerivedElement(
            qname="c1",
            value=1,
            type=None
        ),
        d1_or_d2=AnyElement(
            qname="d1",
            text="testing",
            tail=None,
            children=[],
            attributes={}
        )
    )
)
