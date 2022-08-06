from output.models.ms_data.particles.particles_c015_xsd.particles_c015 import Any
from output.models.ms_data.particles.particles_c015_xsd.particles_c015 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        Any(
            foo_bar_element=[
                AnyElement(
                    qname="{foo}foo",
                    text="",
                    tail=None,
                    children=[
                        AnyElement(
                            qname="{just_testing_should_pass}bar",
                            text="",
                            tail=None,
                            children=[],
                            attributes={}
                        ),
                    ],
                    attributes={}
                ),
                AnyElement(
                    qname="{foo}foo",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                ),
            ]
        ),
    ]
)
