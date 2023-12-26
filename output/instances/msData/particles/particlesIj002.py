from output.models.ms_data.particles.particles_ij002_xsd.particles_ij002 import Doc
from output.models.ms_data.particles.particles_ij002_xsd.particles_ij002 import Elem
from output.models.ms_data.particles.particles_ij002_xsd.particles_ij002 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        c1_or_c2=Foo(
            f1_or_f2=[
                AnyElement(
                    qname='{http://xsdtesting}f1',
                    text='\n\t\t\t'
                ),
                AnyElement(
                    qname='{http://xsdtesting}f1',
                    text=''
                ),
            ]
        )
    )
)
