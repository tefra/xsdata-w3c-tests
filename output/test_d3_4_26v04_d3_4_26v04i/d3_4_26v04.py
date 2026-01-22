from output.models.ibm_data.valid.d3_4_26.d3_4_26v04_xsd.d3_4_26v04 import Root
from xsdata.models.datatype import XmlDuration


obj = Root(
    ely_mdmin_inclusive_min_inclusive=[
        XmlDuration("P2M"),
        XmlDuration("P3M"),
    ],
    ely_mdmin_inclusive_min_exclusive=[
        XmlDuration("P3M"),
        XmlDuration("P1Y"),
    ],
    ely_mdmin_inclusive_max_inclusive=[
        XmlDuration("P3452Y2M"),
        XmlDuration("P1M"),
    ],
    ely_mdmin_inclusive_max_exclusive=[
        XmlDuration("P23Y1M"),
        XmlDuration("P1M"),
    ]
)
