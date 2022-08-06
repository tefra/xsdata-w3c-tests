from output.models.ms_data.wildcards.wild_z003_a_xsd.wild_z003_a import Elt1
from output.models.ms_data.wildcards.wild_z003_a_xsd.wild_z003_b import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Elt1(
    elt2="",
    elem=Elem(
        any_element=None
    ),
    other_element=[
        AnyElement(
            qname="{urn:bar}elem",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{urn:bar}elem",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{urn:bar}elem",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
    ]
)
