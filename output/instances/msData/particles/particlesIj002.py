from output.models.ms_data.particles.particles_ij002_xsd.particles_ij002 import Doc
from output.models.ms_data.particles.particles_ij002_xsd.particles_ij002 import Elem
from output.models.ms_data.particles.particles_ij002_xsd.particles_ij002 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        c1=Foo(
            f1_or_f2=[
                AnyElement(
                    qname="{http://xsdtesting}f1",
                    text="&#10;&#9;&#9;&#9;",
                    tail=None,
                    children=[],
                    attributes={}
                ),
                AnyElement(
                    qname="{http://xsdtesting}f1",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                ),
            ]
        ),
        c2=None
    )
)