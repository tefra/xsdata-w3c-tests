from output.models.ms_data.particles.particles_ij005_xsd.particles_ij005 import Doc
from output.models.ms_data.particles.particles_ij005_xsd.particles_ij005 import Elem
from output.models.ms_data.particles.particles_ij005_xsd.particles_ij005 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        c1_or_c2=Foo(
            f1_or_f2=[
                Foo.F1(
                    content=AnyElement(
                        text='\n\t\ttest\n\t'
                    )
                ),
                Foo.F1(

                ),
                Foo.F1(

                ),
                Foo.F1(

                ),
            ]
        )
    )
)
