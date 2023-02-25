from output.models.ms_data.particles.particles_l012_xsd.particles_l012 import Doc
from output.models.ms_data.particles.particles_l012_xsd.particles_l012 import Mixed
from output.models.ms_data.particles.particles_l012_xsd.particles_l012 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        c1_or_c2=[
            Mixed(
                content=[
                    AnyElement(
                        qname="foo",
                        text="testing",
                        tail=None,
                        children=[],
                        attributes={}
                    ),
                ]
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
        ]
    )
)
