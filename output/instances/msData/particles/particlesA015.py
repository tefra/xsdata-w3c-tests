from output.models.ms_data.particles.particles_a015_xsd.particles_a015 import Doc
from output.models.ms_data.particles.particles_a015_xsd.particles_a015 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        any_element=[
            AnyElement(
                qname="{foo}any",
                text="&#10;&#9;&#9;&#9;testing&#10;&#9;&#9;",
                tail=None,
                children=[],
                attributes={}
            ),
            AnyElement(
                qname="{foo}foo",
                text="&#10;&#9;&#9;&#9;really testing&#10;&#9;&#9;",
                tail=None,
                children=[],
                attributes={}
            ),
            AnyElement(
                qname="{foo}foo",
                text="&#10;&#9;&#9;&#9;really testing&#10;&#9;&#9;",
                tail=None,
                children=[],
                attributes={}
            ),
        ]
    )
)
