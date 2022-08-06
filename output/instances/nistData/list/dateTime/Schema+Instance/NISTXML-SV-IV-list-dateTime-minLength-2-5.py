from output.models.nist_data.list_pkg.date_time.schema_instance.nistschema_sv_iv_list_date_time_min_length_2_xsd.nistschema_sv_iv_list_date_time_min_length_2 import NistschemaSvIvListDateTimeMinLength2
from xsdata.models.datatype import XmlDateTime


obj = NistschemaSvIvListDateTimeMinLength2(
    value=[
        XmlDateTime(2013, 5, 23, 15, 59, 45),
        XmlDateTime(2004, 6, 20, 12, 59, 35),
        XmlDateTime(2045, 5, 26, 16, 19, 5),
        XmlDateTime(2032, 4, 23, 14, 9, 5),
        XmlDateTime(2021, 7, 25, 14, 49, 25),
        XmlDateTime(2071, 2, 25, 19, 39, 25),
        XmlDateTime(2038, 6, 21, 11, 49, 35),
    ]
)
