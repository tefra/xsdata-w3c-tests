from output.models.nist_data.list_pkg.g_month_day.schema_instance.nistschema_sv_iv_list_g_month_day_length_1_xsd.nistschema_sv_iv_list_g_month_day_length_1 import NistschemaSvIvListGMonthDayLength1
from xsdata.models.datatype import XmlPeriod


obj = NistschemaSvIvListGMonthDayLength1(
    value=[
        XmlPeriod("--03-15"),
        XmlPeriod("--03-10"),
        XmlPeriod("--05-16"),
        XmlPeriod("--05-17"),
        XmlPeriod("--08-12"),
    ]
)
