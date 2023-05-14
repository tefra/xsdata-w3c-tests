from output.models.ms_data.particles.particles_ha015_xsd.particles_ha015 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    foo_or_bar=AnyElement(
        qname="{http://xsdtesting}bar",
        text="",
        tail=None,
        children=[],
        attributes={}
    )
)
