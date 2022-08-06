from output.models.nist_data.list_pkg.g_month_day.schema_instance.nistschema_sv_iv_list_g_month_day_white_space_1_xsd.nistschema_sv_iv_list_g_month_day_white_space_1 import NistschemaSvIvListGMonthDayWhiteSpace1
from xsdata.models.datatype import XmlPeriod


obj = NistschemaSvIvListGMonthDayWhiteSpace1(
    value=[
        XmlPeriod("--01-01"),
        XmlPeriod("--02-16"),
        XmlPeriod("--02-28"),
        XmlPeriod("--02-11"),
        XmlPeriod("--07-31"),
        XmlPeriod("--12-31"),
    ]
)
