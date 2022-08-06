from output.models.ms_data.model_groups.mg_i018_xsd.mg_i018 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    s1=None,
    s2=None,
    s3=None,
    s4=None,
    n1_element=None,
    n2_element=None,
    n3_element=None,
    n4_element=AnyElement(
        qname="{http://n4}foo",
        text="",
        tail=None,
        children=[],
        attributes={}
    )
)
