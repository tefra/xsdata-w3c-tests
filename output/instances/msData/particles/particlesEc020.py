from output.models.ms_data.particles.particles_ec020_xsd.particles_ec020 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    a_or_b=[
        AnyElement(
            qname="{http://xsdtesting}b",
            text=""
        ),
        AnyElement(
            qname="{http://xsdtesting}b",
            text=""
        ),
    ]
)
