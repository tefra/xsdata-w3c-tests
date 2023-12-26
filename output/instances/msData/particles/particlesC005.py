from output.models.ms_data.particles.particles_c005_xsd.particles_c005 import AnyType
from output.models.ms_data.particles.particles_c005_xsd.particles_c005 import Doc
from output.models.ms_data.particles.particles_c005_xsd.particles_c005 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        AnyType(
            any_element=[
                Foo(
                    any_element=[
                        AnyElement(
                            qname='abc',
                            text=''
                        ),
                        Doc(

                        ),
                    ]
                ),
            ]
        ),
    ]
)
