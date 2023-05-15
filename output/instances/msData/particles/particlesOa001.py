from output.models.ms_data.particles.particles_oa001_xsd.particles_oa001 import Doc
from output.models.ms_data.particles.particles_oa001_xsd.particles_oa001 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        any_element=AnyElement(
            qname="{http://xsdtesting}doc",
            text="",
            children=[
                AnyElement(
                    qname="elem",
                    text="",
                    children=[
                        AnyElement(
                            qname="{http://xsdtesting}foo",
                            text=""
                        ),
                    ]
                ),
            ]
        )
    )
)
