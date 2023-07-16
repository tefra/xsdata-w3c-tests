from output.models.ms_data.particles.particles_ie016_xsd.particles_ie016 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    e1_or_e2=AnyElement(
        qname="{http://xsdtesting}e1",
        text=""
    )
)
