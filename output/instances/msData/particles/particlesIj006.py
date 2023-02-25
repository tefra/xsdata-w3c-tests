from output.models.ms_data.particles.particles_ij006_xsd.particles_ij006 import Bar
from output.models.ms_data.particles.particles_ij006_xsd.particles_ij006 import Doc
from output.models.ms_data.particles.particles_ij006_xsd.particles_ij006 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        c1_or_c2=Bar(
            f1_or_f2=[
                AnyElement(
                    qname="{http://xsdtesting}f1",
                    text="&#10;&#9;&#9;test&#10;&#9;",
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
                AnyElement(
                    qname="{http://xsdtesting}f1",
                    text="",
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
        )
    )
)
