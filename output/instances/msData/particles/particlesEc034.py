from output.models.ms_data.particles.particles_ec034_xsd.particles_ec034 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    a_or_b=[
        AnyElement(
            qname="{http://xsdtesting}b",
            text=""
        ),
        AnyElement(
            qname="{http://xsdtesting}a",
            text=""
        ),
        AnyElement(
            qname="{http://xsdtesting}b",
            text=""
        ),
    ]
)
