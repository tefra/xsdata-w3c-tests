from output.models.ms_data.particles.particles_ig014_xsd.particles_ig014 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    e1_or_e2=AnyElement(
        qname="{http://xsdtesting}e2",
        text="a"
    )
)
