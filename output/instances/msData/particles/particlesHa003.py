from output.models.ms_data.particles.particles_ha003_xsd.particles_ha003 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    e1_or_e2_or_e3=[
        AnyElement(
            qname="{http://xsdtesting}e1",
            text=""
        ),
    ]
)
