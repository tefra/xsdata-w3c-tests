from output.models.ms_data.particles.particles_ec031_xsd.particles_ec031 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    a_or_b=[
        AnyElement(
            qname="{http://xsdtesting}a",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{http://xsdtesting}b",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
    ]
)