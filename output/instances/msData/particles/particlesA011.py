from output.models.ms_data.particles.particles_a011_xsd.particles_a011 import Doc
from output.models.ms_data.particles.particles_a011_xsd.particles_a011 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        e1_or_e2=[
            Elem.E2(

            ),
            Elem.E2(

            ),
            Elem.E2(
                content=AnyElement(
                    text=' test '
                )
            ),
        ]
    )
)
