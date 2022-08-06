from output.models.sun_data.ctype.target_ns.target_ns00101m.target_ns00101m_xsd.target_ns00101m import Test
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = DerivedElement(
    qname="{targetNS}test",
    value=Test(
        abc="1"
    ),
    type="{targetNS}Test"
)
