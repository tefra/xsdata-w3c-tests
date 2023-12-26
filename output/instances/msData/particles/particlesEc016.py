from output.models.ms_data.particles.particles_ec016_xsd.particles_ec016 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    a_or_b=[
        AnyElement(
            qname='{http://xsdtesting}a',
            text=''
        ),
    ]
)
