from output.models.ms_data.model_groups.mg_f016_xsd.mg_f016 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    g1_or_g12=AnyElement(
        qname="g1",
        text="",
        tail=None,
        children=[],
        attributes={}
    ),
    g2_or_g22=AnyElement(
        qname="g2",
        text="",
        tail=None,
        children=[],
        attributes={}
    ),
    g3_or_g32=AnyElement(
        qname="g3",
        text="",
        tail=None,
        children=[],
        attributes={}
    ),
    g4_or_g42=AnyElement(
        qname="g4",
        text="",
        tail=None,
        children=[],
        attributes={}
    ),
    c1="",
    c2="",
    c3="",
    c4=""
)
