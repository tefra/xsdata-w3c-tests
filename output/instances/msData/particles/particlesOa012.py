from output.models.ms_data.particles.particles_oa012_xsd.particles_oa012 import Doc
from output.models.ms_data.particles.particles_oa012_xsd.particles_oa012 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        any_element=[
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
