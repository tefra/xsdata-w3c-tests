from output.models.ibm_data.valid.d3_3_10.d3_3_10v01_xsd.d3_3_10v01 import Root
from xsdata.models.datatype import XmlDate


obj = Root(
    el_date=[
        XmlDate(2000, 12, 12, 660),
    ]
)
