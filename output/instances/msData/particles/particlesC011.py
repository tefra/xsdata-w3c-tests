from output.models.ms_data.particles.particles_c011_xsd.particles_c011 import AnyType
from output.models.ms_data.particles.particles_c011_xsd.particles_c011 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        AnyType(
            xslt_element=[
                AnyElement(
                    qname="{http://xslt}a",
                    text=""
                ),
                AnyElement(
                    qname="{http://xslt}a",
                    text=""
                ),
                AnyElement(
                    qname="{http://xslt}a",
                    text=""
                ),
            ]
        ),
    ]
)
