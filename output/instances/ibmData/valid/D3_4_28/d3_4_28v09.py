from output.models.ibm_data.valid.d3_4_28.d3_4_28v09_xsd.d3_4_28v09 import Root


obj = Root(
    el_max_exclusive_min_inclusive=[
        "2000-02-01T00:00:00+09:00",
        "2002-01-31T23:59:59+09:00",
    ],
    el_max_exclusive_min_exclusive=[
        "2000-02-01T00:00:01+09:00",
        "2002-01-31T23:59:59+09:00",
    ],
    el_max_exclusive_max_inclusive=[
        "2002-01-31T23:59:59+09:00",
        "1002-01-31T23:59:59+09:00",
    ],
    el_max_exclusive_max_exclusive=[
        "2002-01-31T23:59:59+09:00",
        "1002-01-31T23:59:59+09:00",
    ]
)
