from output.models.ibm_data.valid.d3_3_13.d3_3_13v01_xsd.d3_3_13v01 import Root
from xsdata.models.datatype import XmlPeriod


obj = Root(
    el_date=[
        XmlPeriod("--12-12+11:00"),
    ]
)
