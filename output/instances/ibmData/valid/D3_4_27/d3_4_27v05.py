from output.models.ibm_data.valid.d3_4_27.d3_4_27v05_xsd.d3_4_27v05 import Root
from xsdata.models.datatype import XmlDuration


obj = Root(
    el_max_exclusive_min_inclusive=[
        XmlDuration("P27DT23H"),
        XmlDuration("-P39DT3M"),
    ],
    el_max_exclusive_min_exclusive=[
        XmlDuration("P27DT23H"),
        XmlDuration("-P39DT1M"),
    ],
    el_max_exclusive_max_inclusive=[
        XmlDuration("-P3323D"),
        XmlDuration("P27DT3M"),
    ],
    el_max_exclusive_max_exclusive=[
        XmlDuration("P26DT23H"),
        XmlDuration("-P342D"),
    ]
)
