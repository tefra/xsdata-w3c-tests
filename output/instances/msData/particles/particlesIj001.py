from output.models.ms_data.particles.particles_ij001_xsd.particles_ij001 import Doc
from output.models.ms_data.particles.particles_ij001_xsd.particles_ij001 import Elem
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Doc(
    elem=Elem(
        c1_or_c2=[
            DerivedElement(
                qname='{http://xsdtesting}c1',
                value=1
            ),
        ]
    )
)
