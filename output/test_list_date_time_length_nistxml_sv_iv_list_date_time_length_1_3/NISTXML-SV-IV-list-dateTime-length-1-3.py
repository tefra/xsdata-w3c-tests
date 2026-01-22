from output.models.nist_data.list_pkg.date_time.schema_instance.nistschema_sv_iv_list_date_time_length_1_xsd.nistschema_sv_iv_list_date_time_length_1 import NistschemaSvIvListDateTimeLength1
from xsdata.models.datatype import XmlDateTime


obj = NistschemaSvIvListDateTimeLength1(
    value=[
        XmlDateTime(1902, 2, 10, 4, 17, 37),
        XmlDateTime(1902, 2, 10, 4, 14, 27),
        XmlDateTime(1902, 2, 20, 14, 16, 17),
        XmlDateTime(1702, 2, 10, 4, 15, 37),
        XmlDateTime(1802, 2, 10, 14, 16, 47),
    ]
)
