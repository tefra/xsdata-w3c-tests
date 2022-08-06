from output.models.ibm_data.valid.d3_3_11.d3_3_11v01_xsd.d3_3_11v01 import Root
from xsdata.models.datatype import XmlPeriod


obj = Root(
    el_date=[
        XmlPeriod("2000-12+11:00"),
    ]
)
