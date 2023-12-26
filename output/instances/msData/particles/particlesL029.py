from output.models.ms_data.particles.particles_l029_xsd.particles_l029 import Doc
from output.models.ms_data.particles.particles_l029_xsd.particles_l029 import Foo
from output.models.ms_data.particles.particles_l029_xsd.particles_l029 import R
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        foo_or_c2=Foo(
            any_element=AnyElement(
                text='1'
            )
        ),
        d1_or_d2=AnyElement(
            qname='d1',
            text='testing'
        )
    )
)
