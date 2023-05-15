from output.models.ms_data.particles.particles_ob056_xsd.particles_ob056 import Doc
from output.models.ms_data.particles.particles_ob056_xsd.particles_ob056 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        local_foo_bar_target_namespace_element=AnyElement(
            qname="{http://xsdtesting}foo",
            text=""
        )
    )
)
