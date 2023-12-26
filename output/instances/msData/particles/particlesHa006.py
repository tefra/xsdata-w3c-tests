from output.models.ms_data.particles.particles_ha006_xsd.particles_ha006 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    e2_or_e3=AnyElement(
        qname='{http://xsdtesting}e3',
        text=''
    )
)
