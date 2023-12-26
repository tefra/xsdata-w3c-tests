from output.models.ms_data.particles.particles_z012_xsd.particles_z012 import E3
from output.models.ms_data.particles.particles_z012_xsd.particles_z012 import MyType10Value
from output.models.ms_data.particles.particles_z012_xsd.particles_z012 import Root
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    e2_or_e1_or_e3=[
        DerivedElement(
            qname='{http://xsdtesting}E1',
            value=1
        ),
        DerivedElement(
            qname='{http://xsdtesting}E1',
            value=True
        ),
        DerivedElement(
            qname='{http://xsdtesting}E1',
            value=False
        ),
        DerivedElement(
            qname='{http://xsdtesting}E1',
            value=MyType10Value.X
        ),
        DerivedElement(
            qname='{http://xsdtesting}E1',
            value=MyType10Value.Y
        ),
        1,
        E3(
            att1=123
        ),
    ]
)
