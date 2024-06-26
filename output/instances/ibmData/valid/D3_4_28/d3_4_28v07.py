from output.models.ibm_data.valid.d3_4_28.d3_4_28v07_xsd.d3_4_28v07 import Root


obj = Root(
    el_min_exclusive_min_inclusive=[
        '2009-02-02T02:00:00+09:00',
        '2002-02-02T02:00:01+09:00',
    ],
    el_min_exclusive_min_exclusive=[
        '2002-02-02T01:00:02+08:00',
        '2009-12-02T10:59:59+09:00',
    ],
    el_min_exclusive_max_inclusive=[
        '2005-02-02T02:00:00+09:00',
        '2002-02-02T02:00:01+09:00',
    ],
    el_min_exclusive_max_exclusive=[
        '2005-02-02T01:59:58+09:00',
        '2002-02-02T02:00:01+09:00',
    ]
)
