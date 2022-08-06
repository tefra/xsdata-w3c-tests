from output.models.ms_data.particles.particles_c028_xsd.particles_c028 import Any
from output.models.ms_data.particles.particles_c028_xsd.particles_c028 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        Any(
            foo_bar_target_namespace_element=[
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
