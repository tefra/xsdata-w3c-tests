from output.models.ms_data.particles.particles_l003_xsd.particles_l003 import Doc
from output.models.ms_data.particles.particles_l003_xsd.particles_l003 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        c1_or_c2=[
            AnyElement(
                qname="c1",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
            AnyElement(
                qname="c1",
                text="testing",
                tail=None,
                children=[],
                attributes={}
            ),
        ],
        d1_or_d2=[
            AnyElement(
                qname="d1",
                text="testing",
                tail=None,
                children=[],
                attributes={}
            ),
            AnyElement(
                qname="d1",
                text="testing",
                tail=None,
                children=[],
                attributes={}
            ),
        ]
    )
)