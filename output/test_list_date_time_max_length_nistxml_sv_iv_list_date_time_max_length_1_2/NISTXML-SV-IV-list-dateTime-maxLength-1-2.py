from output.models.nist_data.list_pkg.date_time.schema_instance.nistschema_sv_iv_list_date_time_max_length_1_xsd.nistschema_sv_iv_list_date_time_max_length_1 import NistschemaSvIvListDateTimeMaxLength1
from xsdata.models.datatype import XmlDateTime


obj = NistschemaSvIvListDateTimeMaxLength1(
    value=[
        XmlDateTime(1984, 6, 10, 7, 10, 29),
        XmlDateTime(1984, 6, 20, 6, 17, 9),
        XmlDateTime(1784, 6, 10, 8, 14, 49),
        XmlDateTime(2084, 6, 20, 5, 12, 19),
        XmlDateTime(1784, 6, 10, 5, 13, 29),
    ]
)
