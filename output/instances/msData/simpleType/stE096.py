from output.models.ms_data.simple_type.st_e096_xsd.st_e096 import Root
from xsdata.models.datatype import XmlPeriod


obj = Root(
    value=[
        XmlPeriod("2004"),
        XmlPeriod("---04"),
        XmlPeriod("--05"),
    ]
)
