from output.models.ms_data.particles.particles_db002_xsd.particles_db002 import Doc
from output.models.ms_data.particles.particles_db002_xsd.particles_db002 import Elem1
from output.models.ms_data.particles.particles_db002_xsd.particles_db002 import Elem2
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem1=Elem1(

    ),
    elem2=Elem2(
        a1_or_a2=AnyElement(
            qname="{http://xsdtesting}a1",
            text=""
        )
    )
)
