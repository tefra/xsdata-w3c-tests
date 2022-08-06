from output.models.ibm_data.valid.d3_4_27.d3_4_27v01_xsd.d3_4_27v01 import Root
from output.models.ibm_data.valid.d3_4_27.d3_4_27v01_xsd.d3_4_27v01 import YMdenumeration
from xsdata.models.datatype import XmlDuration


obj = Root(
    ely_mdtype=[
        XmlDuration("P343DT0H"),
        XmlDuration("-PT48M"),
        XmlDuration("P1DT4.00003S"),
    ],
    ely_mdenumeration=[
        YMdenumeration.PT54_H3_M2_3_S,
        YMdenumeration.P5_DT3_S,
        YMdenumeration.PT43_M4_2_S,
    ],
    ely_mdmin_max_inclusive=[
        XmlDuration("-P1D"),
        XmlDuration("PT47H3M"),
        XmlDuration("-PT46H59M3454.3S"),
    ],
    ely_mdmin_max_exclusive=[
        XmlDuration("-P1D"),
        XmlDuration("PT47H3M"),
        XmlDuration("-PT46H59M3454.3S"),
    ]
)
