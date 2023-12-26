from output.models.ms_data.particles.particles_ec017_xsd.particles_ec017 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    a_or_b=[
        AnyElement(
            qname='{http://xsdtesting}b',
            text=''
        ),
    ]
)
