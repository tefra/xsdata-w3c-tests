from output.models.ms_data.particles.particles_t012_xsd.particles_t012 import Bar
from output.models.ms_data.particles.particles_t012_xsd.particles_t012 import Doc
from output.models.ms_data.particles.particles_t012_xsd.particles_t012 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        choice=[
            Bar(
                foo="",
                att=None,
                att1="testing"
            ),
            AnyElement(
                qname="foo",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
        ]
    )
)
