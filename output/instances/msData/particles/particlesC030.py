from output.models.ms_data.particles.particles_c030_xsd.particles_c030 import Any
from output.models.ms_data.particles.particles_c030_xsd.particles_c030 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        Any(
            foo_bar_target_namespace_element=[
                AnyElement(
                    qname="{http://xsdtesting}foo",
                    text=""
                ),
            ]
        ),
    ]
)
