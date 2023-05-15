from output.models.ms_data.particles.particles_ig001_xsd.particles_ig001 import Doc
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Doc(
    e1_or_e2=DerivedElement(
        qname="{http://xsdtesting}e2",
        value="a"
    )
)
