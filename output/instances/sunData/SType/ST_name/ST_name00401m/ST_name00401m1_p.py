from output.models.sun_data.stype.st_name.st_name00401m.st_name00401m_xsd.st_name00401m import Test
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = DerivedElement(
    qname='{ST_name}test',
    value=Test(
        value='2'
    ),
    type='{ST_name}Test'
)
