from output.models.ibm_data.valid.d3_4_28.d3_4_28v08_xsd.d3_4_28v08 import Root


obj = Root(
    el_max_inclusive_min_inclusive=[
        '2002-02-01T00:00:00+09:00',
        '2000-02-01T02:00:00+09:00',
    ],
    el_max_inclusive_min_exclusive=[
        '2002-02-01T00:00:00+09:00',
        '2000-02-01T00:00:01+09:00',
    ],
    el_max_inclusive_max_inclusive=[
        '2002-01-01T00:00:00+09:00',
        '1002-02-01T00:00:00+09:00',
    ],
    el_max_inclusive_max_exclusive=[
        '2002-01-01T00:00:00+09:00',
        '2002-01-31T23:59:58+09:00',
    ]
)
