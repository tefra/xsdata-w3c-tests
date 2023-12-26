from output.models.ms_data.particles.particles_ec012_xsd.particles_ec012 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    a1_or_a2=AnyElement(
        qname='{http://xsdtesting}a1',
        text=''
    )
)
