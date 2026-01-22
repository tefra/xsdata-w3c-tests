from output.models.ms_data.errata10.err_e006_xsd.err_e006 import Root
from output.models.ms_data.errata10.err_e006_xsd.err_e006 import TestDate
from output.models.ms_data.errata10.err_e006_xsd.err_e006 import TestGday
from output.models.ms_data.errata10.err_e006_xsd.err_e006 import TestGmonth
from output.models.ms_data.errata10.err_e006_xsd.err_e006 import TestGmonthDay
from output.models.ms_data.errata10.err_e006_xsd.err_e006 import TestGyear
from output.models.ms_data.errata10.err_e006_xsd.err_e006 import TestGyearMonth
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlPeriod


obj = Root(
    test_date=[
        TestDate(
            value=XmlDate(2002, 12, 31, -300)
        ),
        TestDate(
            value=XmlDate(2002, 12, 31, 0)
        ),
    ],
    test_gyear_month=[
        TestGyearMonth(
            value=XmlPeriod("2002-12-05:00")
        ),
        TestGyearMonth(
            value=XmlPeriod("2002-12Z")
        ),
    ],
    test_gmonth_day=[
        TestGmonthDay(
            value=XmlPeriod("--12-31-05:00")
        ),
        TestGmonthDay(
            value=XmlPeriod("--12-31Z")
        ),
    ],
    test_gday=[
        TestGday(
            value=XmlPeriod("---31-05:00")
        ),
        TestGday(
            value=XmlPeriod("---31Z")
        ),
    ],
    test_gmonth=[
        TestGmonth(
            value=XmlPeriod("--12-05:00")
        ),
        TestGmonth(
            value=XmlPeriod("--12Z")
        ),
    ],
    test_gyear=[
        TestGyear(
            value=XmlPeriod("2002-05:00")
        ),
        TestGyear(
            value=XmlPeriod("2002Z")
        ),
    ]
)
