from output.models.ibm_data.valid.d3_4_27.d3_4_27v03_xsd.d3_4_27v03 import Root
from xsdata.models.datatype import XmlDuration


obj = Root(
    ely_mdunion_a=[
        "Computer",
        XmlDuration("P4DT4H"),
    ],
    ely_mdunion_b=[
        XmlDuration("-PT32H4M3.4S"),
        7,
    ],
    ely_mdunion_c=[
        XmlDuration("PT34.3S"),
        1,
        "once",
    ]
)
