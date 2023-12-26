from output.models.ms_data.particles.particles_ha010_xsd.particles_ha010 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    x_or_y=[
        AnyElement(
            qname='{http://xsdtesting}y',
            text=''
        ),
    ]
)
