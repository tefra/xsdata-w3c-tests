from output.models.ms_data.particles.particles_fa005_xsd.particles_fa005 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    target_namespace_foo_element=[
        AnyElement(
            qname="{foo}elem",
            text="&#10;&#9;",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{http://xsdtesting}foo",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
    ]
)
