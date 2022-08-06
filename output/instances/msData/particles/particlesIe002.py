from output.models.ms_data.particles.particles_ie002_xsd.particles_ie002 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    e1_or_e2=[
        AnyElement(
            qname="{http://xsdtesting}e1",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
    ]
)
