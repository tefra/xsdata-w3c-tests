from output.models.ibm_data.valid.d3_4_27.d3_4_27v04_xsd.d3_4_27v04 import Root
from xsdata.models.datatype import XmlDuration


obj = Root(
    ely_mdmin_inclusive_min_inclusive=[
        XmlDuration("P2D"),
        XmlDuration("P1DT535.4S"),
    ],
    ely_mdmin_inclusive_min_exclusive=[
        XmlDuration("P3D"),
        XmlDuration("P2DT1S"),
    ],
    ely_mdmin_inclusive_max_inclusive=[
        XmlDuration("P3452DT2H"),
        XmlDuration("P1D"),
    ],
    ely_mdmin_inclusive_max_exclusive=[
        XmlDuration("P43DT42M10.1S"),
        XmlDuration("P1D"),
    ]
)
