from output.models.ms_data.errata10.err_e006_xsd.err_e006 import Root
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlPeriod


obj = Root(
    test_date=[
        XmlDate(2002, 12, 31, -300),
        XmlDate(2002, 12, 31, 0),
    ],
    test_gyear_month=[
        XmlPeriod("2002-12-05:00"),
        XmlPeriod("2002-12Z"),
    ],
    test_gmonth_day=[
        XmlPeriod("--12-31-05:00"),
        XmlPeriod("--12-31Z"),
    ],
    test_gday=[
        XmlPeriod("---31-05:00"),
        XmlPeriod("---31Z"),
    ],
    test_gmonth=[
        XmlPeriod("--12-05:00"),
        XmlPeriod("--12Z"),
    ],
    test_gyear=[
        XmlPeriod("2002-05:00"),
        XmlPeriod("2002Z"),
    ]
)
