from output.models.ms_data.particles.particles_l012_xsd.particles_l012 import Doc
from output.models.ms_data.particles.particles_l012_xsd.particles_l012 import NotMixed
from output.models.ms_data.particles.particles_l012_xsd.particles_l012 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        c1=NotMixed(
            content=[
                AnyElement(
                    qname="foo",
                    text="testing",
                    tail=None,
                    children=[],
                    attributes={}
                ),
            ],
            foo=None
        ),
        c2=None,
        d1="testing",
        d2=None
    )
)
