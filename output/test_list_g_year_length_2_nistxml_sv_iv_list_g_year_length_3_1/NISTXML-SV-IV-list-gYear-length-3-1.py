from output.models.nist_data.list_pkg.g_year.schema_instance.nistschema_sv_iv_list_g_year_length_3_xsd.nistschema_sv_iv_list_g_year_length_3 import NistschemaSvIvListGYearLength3
from xsdata.models.datatype import XmlPeriod


obj = NistschemaSvIvListGYearLength3(
    value=[
        XmlPeriod("2038"),
        XmlPeriod("1938"),
        XmlPeriod("1838"),
        XmlPeriod("1738"),
        XmlPeriod("1838"),
        XmlPeriod("2038"),
        XmlPeriod("1838"),
    ]
)
