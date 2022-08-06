from output.models.ibm_data.valid.d3_4_26.d3_4_26v01_xsd.d3_4_26v01 import Root
from output.models.ibm_data.valid.d3_4_26.d3_4_26v01_xsd.d3_4_26v01 import YMdenumeration
from xsdata.models.datatype import XmlDuration


obj = Root(
    ely_mdtype=[
        XmlDuration("P124Y"),
        XmlDuration("-P3Y348M"),
        XmlDuration("P1Y2M"),
    ],
    ely_mdenumeration=[
        YMdenumeration.P1_Y3_M,
        YMdenumeration.P45_M,
        YMdenumeration.P34_Y233_M,
    ],
    ely_mdmin_max_inclusive=[
        XmlDuration("-P1Y"),
        XmlDuration("P23Y23M"),
        XmlDuration("P53M"),
    ],
    ely_mdmin_max_exclusive=[
        XmlDuration("-P21M"),
        XmlDuration("P42M"),
        XmlDuration("P31Y2M"),
    ]
)
