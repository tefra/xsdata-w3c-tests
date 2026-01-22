from output.models.ibm_data.valid.d3_4_27.d3_4_27v02_xsd.d3_4_27v02 import Root
from output.models.ibm_data.valid.d3_4_27.d3_4_27v02_xsd.d3_4_27v02 import YMdenumeration
from xsdata.models.datatype import XmlDuration


obj = Root(
    ay_mdtype=XmlDuration("P334DT348M"),
    ay_mdenumeration=YMdenumeration.P3_DT44_H2_M5783_33_S,
    ay_mdmin_max_inclusive=XmlDuration("-PT48H"),
    ay_mdmin_max_exclusive=XmlDuration("P29DT423H")
)
