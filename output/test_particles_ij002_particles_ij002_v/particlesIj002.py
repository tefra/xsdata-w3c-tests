from output.models.ms_data.particles.particles_ij002_xsd.particles_ij002 import Doc
from output.models.ms_data.particles.particles_ij002_xsd.particles_ij002 import Elem
from output.models.ms_data.particles.particles_ij002_xsd.particles_ij002 import Foo


obj = Doc(
    elem=Elem(
        c1_or_c2=Foo(
            f1_or_f2=[
                Foo.F1(

                ),
                Foo.F1(

                ),
            ]
        )
    )
)
