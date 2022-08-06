from output.models.ms_data.particles.particles_oa003_xsd.particles_oa003 import Doc
from output.models.ms_data.particles.particles_oa003_xsd.particles_oa003 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        any_element=AnyElement(
            qname="{http://xsdtesting}foo",
            text="",
            tail=None,
            children=[],
            attributes={}
        )
    )
)
