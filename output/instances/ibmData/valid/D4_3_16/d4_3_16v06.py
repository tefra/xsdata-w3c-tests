from output.models.ibm_data.valid.d4_3_16.d4_3_16v06_xsd.d4_3_16v06 import Root


obj = Root(
    eld_time_pattern=[
        "2000-12-28T12:00:00",
    ],
    eld_time_etrequired=[
        "2001-12-28T12:00:00Z",
        "2002-12-28T12:00:00+02:00",
        "2003-12-28T12:00:00-02:00",
    ],
    eld_time_etoptional=[
        "2003-12-28T12:00:00+02:00",
        "2004-12-28T12:00:00",
        "2005-12-28T12:00:00-02:00",
        "2003-12-28T12:00:00Z",
    ],
    eld_time_etprohibited=[
        "2005-12-28T12:00:00",
    ],
    d_time_etoptional_der_req=[
        "2000-12-28T12:00:00Z",
        "2001-12-28T12:00:00-02:00",
        "2002-12-28T12:00:00+02:00",
    ],
    d_time_etoptional_der_pro=[
        "2003-12-28T12:00:00",
    ]
)
