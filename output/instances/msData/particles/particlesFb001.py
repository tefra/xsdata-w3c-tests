from output.models.ms_data.particles.particles_fb001_xsd.particles_fb001 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    c1_or_c2=AnyElement(
        qname="{http://xsdtesting}c1",
        text="",
        tail=None,
        children=[],
        attributes={}
    ),
    g1_or_g2=AnyElement(
        qname="{http://xsdtesting}g2",
        text="",
        tail=None,
        children=[],
        attributes={}
    )
)
