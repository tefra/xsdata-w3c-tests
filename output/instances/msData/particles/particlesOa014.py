from output.models.ms_data.particles.particles_oa014_xsd.particles_oa014 import Doc
from output.models.ms_data.particles.particles_oa014_xsd.particles_oa014 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        any_element=[
            AnyElement(
                qname="{http://xsdtesting}foo",
                text=""
            ),
            AnyElement(
                qname="{http://xsdtesting}foo",
                text=""
            ),
            AnyElement(
                qname="{http://xsdtesting}foo",
                text=""
            ),
        ]
    )
)
