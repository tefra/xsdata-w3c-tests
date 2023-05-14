from output.models.ms_data.particles.particles_q024_xsd.particles_q024 import Doc
from output.models.ms_data.particles.particles_q024_xsd.particles_q024 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        foo_or_target_namespace_element=[
            AnyElement(
                qname="{http://xsdtesting}foo",
                text="",
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
            AnyElement(
                qname="{http://xsdtesting}foo",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
        ]
    )
)
