from output.models.nist_data.list_pkg.date_time.schema_instance.nistschema_sv_iv_list_date_time_max_length_3_xsd.nistschema_sv_iv_list_date_time_max_length_3 import NistschemaSvIvListDateTimeMaxLength3
from xsdata.models.datatype import XmlDateTime


obj = NistschemaSvIvListDateTimeMaxLength3(
    value=[
        XmlDateTime(1989, 8, 22, 19, 18, 19),
        XmlDateTime(1989, 3, 26, 19, 10, 10),
        XmlDateTime(1989, 5, 23, 9, 13, 13),
        XmlDateTime(1889, 8, 22, 9, 18, 16),
        XmlDateTime(1889, 1, 27, 9, 14, 16),
    ]
)
