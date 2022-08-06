from output.models.ms_data.particles.particles_c003_xsd.particles_c003 import Doc
from output.models.ms_data.particles.particles_c003_xsd.particles_c003 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=[
        Elem(
            any_element=[
                AnyElement(
                    qname="b",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                ),
                AnyElement(
                    qname="{http://foo}b",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                ),
                AnyElement(
                    qname="{xmlns}b",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                ),
                AnyElement(
                    qname="b",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                ),
                AnyElement(
                    qname="b",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                ),
            ]
        ),
    ]
)
