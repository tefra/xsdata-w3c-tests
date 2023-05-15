from output.models.ms_data.particles.particles_ob005_xsd.particles_ob005 import Doc
from output.models.ms_data.particles.particles_ob005_xsd.particles_ob005 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        any_element=AnyElement(
            qname="{http://xsdtesting}foo",
            text=""
        )
    )
)
