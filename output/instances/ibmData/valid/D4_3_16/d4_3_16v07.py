from output.models.ibm_data.valid.d4_3_16.d4_3_16v07_xsd.d4_3_16v07 import Root


obj = Root(
    eld_time_etzone_optional_fderived_optional=[
        '2000-01-28T12:00:00',
        '2001-01-28T12:00:00Z',
        '2002-01-28T12:00:00-05:00',
        '2003-01-28T12:00:00+09:00',
    ],
    eld_time_etzone_optional_fderived_required=[
        '2004-01-28T12:00:00Z',
        '2005-01-28T12:00:00+10:00',
        '2006-01-28T12:00:00-10:00',
    ],
    eld_time_etzone_optional_fderived_prohibited=[
        '2007-01-28T12:00:00',
    ],
    eld_time_etzone_optional_tderived_optional=[
        '2008-01-28T12:00:00',
        '2009-01-28T12:00:00Z',
        '2009-01-28T12:00:00-11:00',
        '2009-01-28T12:00:00+11:00',
    ]
)
