from output.models.ms_data.particles.particles_ha016_xsd.particles_ha016 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    foo_or_bar=[
        AnyElement(
            qname="{http://xsdtesting}foo",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{http://xsdtesting}bar",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
    ]
)
