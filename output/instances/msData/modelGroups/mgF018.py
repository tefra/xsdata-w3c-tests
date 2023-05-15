from output.models.ms_data.model_groups.mg_f018_xsd.mg_f018 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    s1="",
    s2="",
    s3="",
    s4="",
    any_element=[
        AnyElement(
            qname="{http://n1}foo",
            text=""
        ),
        AnyElement(
            qname="{http://n2}foo",
            text=""
        ),
        AnyElement(
            qname="{http://n3}foo",
            text=""
        ),
        AnyElement(
            qname="{http://n4}foo",
            text=""
        ),
    ]
)
