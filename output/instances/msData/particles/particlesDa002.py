from output.models.ms_data.particles.particles_da002_xsd.particles_da002 import A
from output.models.ms_data.particles.particles_da002_xsd.particles_da002 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem1='',
    elem2=A(
        a1_or_a2=AnyElement(
            qname='{http://xsdtesting}a1',
            text=''
        )
    )
)
