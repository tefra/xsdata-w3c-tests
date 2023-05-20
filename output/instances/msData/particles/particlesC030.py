from output.models.ms_data.particles.particles_c030_xsd.particles_c030 import AnyType
from output.models.ms_data.particles.particles_c030_xsd.particles_c030 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        AnyType(
            foo_bar_target_namespace_element=[
                AnyElement(
                    qname="{http://xsdtesting}foo",
                    text=""
                ),
            ]
        ),
    ]
)
