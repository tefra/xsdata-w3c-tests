from output.models.ms_data.particles.particles_c016_xsd.particles_c016 import Any
from output.models.ms_data.particles.particles_c016_xsd.particles_c016 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        Any(
            foo_bar_element=[
                AnyElement(
                    qname="{bar}foo",
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
                    qname="{bar}foo",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                ),
            ]
        ),
    ]
)