from output.models.ms_data.particles.particles_oa001_xsd.particles_oa001 import Doc
from output.models.ms_data.particles.particles_oa001_xsd.particles_oa001 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        any_element=AnyElement(
            qname="{http://xsdtesting}doc",
            text="",
            tail=None,
            children=[
                AnyElement(
                    qname="elem",
                    text="",
                    tail=None,
                    children=[
                        AnyElement(
                            qname="{http://xsdtesting}foo",
                            text="",
                            tail=None,
                            children=[],
                            attributes={}
                        ),
                    ],
                    attributes={}
                ),
            ],
            attributes={}
        )
    )
)
