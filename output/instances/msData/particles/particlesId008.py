from output.models.ms_data.particles.particles_id008_xsd.particles_id008 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    e1_or_e2=[
        AnyElement(
            qname="{http://xsdtesting}e1",
            text=""
        ),
        AnyElement(
            qname="{http://xsdtesting}e1",
            text=""
        ),
    ]
)
