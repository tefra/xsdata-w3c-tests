from output.models.ibm_data.valid.d3_4_26.d3_4_26v05_xsd.d3_4_26v05 import Root
from xsdata.models.datatype import XmlDuration


obj = Root(
    el_max_exclusive_min_inclusive=[
        XmlDuration("P27Y3M"),
        XmlDuration("-P39Y3M"),
    ],
    el_max_exclusive_min_exclusive=[
        XmlDuration("-P39Y1M"),
        XmlDuration("P27Y4M"),
    ],
    el_max_exclusive_max_inclusive=[
        XmlDuration("-P3323Y"),
        XmlDuration("P27Y3M"),
    ],
    el_max_exclusive_max_exclusive=[
        XmlDuration("-P342Y23M"),
        XmlDuration("P26Y11M"),
    ]
)
