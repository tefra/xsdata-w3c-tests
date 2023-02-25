from output.models.ms_data.particles.particles_id007_xsd.particles_id007 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    e1_or_e2=AnyElement(
        qname="{http://xsdtesting}e1",
        text="",
        tail=None,
        children=[],
        attributes={}
    )
)
