from output.models.ms_data.particles.particles_c011_xsd.particles_c011 import Any
from output.models.ms_data.particles.particles_c011_xsd.particles_c011 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        Any(
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
