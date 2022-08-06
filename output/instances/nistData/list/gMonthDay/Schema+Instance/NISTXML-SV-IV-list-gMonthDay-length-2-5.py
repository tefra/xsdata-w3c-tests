from output.models.nist_data.list_pkg.g_month_day.schema_instance.nistschema_sv_iv_list_g_month_day_length_2_xsd.nistschema_sv_iv_list_g_month_day_length_2 import NistschemaSvIvListGMonthDayLength2
from xsdata.models.datatype import XmlPeriod


obj = NistschemaSvIvListGMonthDayLength2(
    value=[
        XmlPeriod("--04-23"),
        XmlPeriod("--05-24"),
        XmlPeriod("--04-25"),
        XmlPeriod("--09-23"),
        XmlPeriod("--03-25"),
        XmlPeriod("--04-23"),
    ]
)
