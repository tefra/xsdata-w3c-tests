from output.models.nist_data.list_pkg.g_month_day.schema_instance.nistschema_sv_iv_list_g_month_day_max_length_2_xsd.nistschema_sv_iv_list_g_month_day_max_length_2 import NistschemaSvIvListGMonthDayMaxLength2
from xsdata.models.datatype import XmlPeriod


obj = NistschemaSvIvListGMonthDayMaxLength2(
    value=[
        XmlPeriod("--10-11"),
        XmlPeriod("--11-15"),
        XmlPeriod("--12-14"),
        XmlPeriod("--12-16"),
        XmlPeriod("--11-13"),
    ]
)
