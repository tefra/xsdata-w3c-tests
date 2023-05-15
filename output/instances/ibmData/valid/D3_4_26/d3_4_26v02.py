from output.models.ibm_data.valid.d3_4_26.d3_4_26v02_xsd.d3_4_26v02 import Root
from output.models.ibm_data.valid.d3_4_26.d3_4_26v02_xsd.d3_4_26v02 import YMdenumeration
from xsdata.models.datatype import XmlDuration


obj = Root(
    ay_mdtype=XmlDuration("-P3Y348M"),
    ay_mdenumeration=YMdenumeration.P34_Y233_M,
    ay_mdmin_max_inclusive=XmlDuration("-P24M"),
    ay_mdmin_max_exclusive=XmlDuration("P23Y23M")
)
