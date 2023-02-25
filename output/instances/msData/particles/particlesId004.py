from output.models.ms_data.particles.particles_id004_xsd.particles_id004 import Doc
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
