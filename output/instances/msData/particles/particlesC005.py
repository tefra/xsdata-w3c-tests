from output.models.ms_data.particles.particles_c005_xsd.particles_c005 import AnyType
from output.models.ms_data.particles.particles_c005_xsd.particles_c005 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        AnyType(
            any_element=[
                AnyElement(
                    qname="{http://xsdtesting}foo",
                    text="",
                    children=[
                        AnyElement(
                            qname="abc",
                            text=""
                        ),
                        AnyElement(
                            qname="{http://xsdtesting}doc",
                            text=""
                        ),
                    ]
                ),
            ]
        ),
    ]
)
