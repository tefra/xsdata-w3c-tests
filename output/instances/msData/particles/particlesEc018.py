from output.models.ms_data.particles.particles_ec018_xsd.particles_ec018 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    a_or_b=[
        AnyElement(
            qname="{http://xsdtesting}a",
            text=""
        ),
        AnyElement(
            qname="{http://xsdtesting}a",
            text=""
        ),
    ]
)
