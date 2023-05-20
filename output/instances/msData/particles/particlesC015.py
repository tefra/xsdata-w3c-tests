from output.models.ms_data.particles.particles_c015_xsd.particles_c015 import AnyType
from output.models.ms_data.particles.particles_c015_xsd.particles_c015 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        AnyType(
            foo_bar_element=[
                AnyElement(
                    qname="{foo}foo",
                    text="",
                    children=[
                        AnyElement(
                            qname="{just_testing_should_pass}bar",
                            text=""
                        ),
                    ]
                ),
                AnyElement(
                    qname="{foo}foo",
                    text=""
                ),
            ]
        ),
    ]
)
