from output.models.ms_data.particles.particles_fb004_xsd.particles_fb004 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    g1_or_g2=AnyElement(
        qname="{http://xsdtesting}g1",
        text="",
        tail=None,
        children=[],
        attributes={}
    ),
    s1="",
    s2=""
)
