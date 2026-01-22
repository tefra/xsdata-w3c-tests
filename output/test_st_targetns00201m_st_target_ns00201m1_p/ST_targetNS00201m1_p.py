from output.models.sun_data.stype.st_target_ns.st_target_ns00201m.st_target_ns00201m_xsd.st_target_ns00201m import Test
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = DerivedElement(
    qname='{ST_targetNS}test',
    value=Test(
        value='2'
    ),
    type='{ST_targetNS}Test'
)
