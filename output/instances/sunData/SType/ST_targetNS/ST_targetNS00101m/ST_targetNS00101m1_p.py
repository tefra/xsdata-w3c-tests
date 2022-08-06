from output.models.sun_data.stype.st_target_ns.st_target_ns00101m.st_target_ns00101m_xsd.st_target_ns00101m import Test
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = DerivedElement(
    qname="{ST_targetNS}test",
    value=Test(
        value="1"
    ),
    type="{ST_targetNS}Test"
)
