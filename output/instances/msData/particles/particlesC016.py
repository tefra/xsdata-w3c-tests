from output.models.ms_data.particles.particles_c016_xsd.particles_c016 import AnyType
from output.models.ms_data.particles.particles_c016_xsd.particles_c016 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        AnyType(
            foo_bar_element=[
                AnyElement(
                    qname="{bar}foo",
                    text="",
                    children=[
                        AnyElement(
                            qname="{just_testing_should_pass}bar",
                            text=""
                        ),
                    ]
                ),
                AnyElement(
                    qname="{bar}foo",
                    text=""
                ),
            ]
        ),
    ]
)
