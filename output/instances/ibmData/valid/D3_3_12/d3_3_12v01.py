from output.models.ibm_data.valid.d3_3_12.d3_3_12v01_xsd.d3_3_12v01 import Root
from xsdata.models.datatype import XmlPeriod


obj = Root(
    el_date=[
        XmlPeriod("2000+11:00"),
    ]
)
