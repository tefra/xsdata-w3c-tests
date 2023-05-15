from output.models.ms_data.particles.particles_ob032_xsd.particles_ob032 import Doc
from output.models.ms_data.particles.particles_ob032_xsd.particles_ob032 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        target_namespace_element=AnyElement(
            qname="{http://xsdtesting}foo",
            text=""
        )
    )
)
