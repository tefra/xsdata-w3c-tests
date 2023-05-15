from output.models.ms_data.particles.particles_c044_xsd.particles_c044 import Any
from output.models.ms_data.particles.particles_c044_xsd.particles_c044 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        Any(
            foo_target_namespace_bar_local_element=[
                AnyElement(
                    qname="{bar}foo",
                    text=""
                ),
            ]
        ),
    ]
)
