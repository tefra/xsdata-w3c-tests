from output.models.nist_data.list_pkg.date_time.schema_instance.nistschema_sv_iv_list_date_time_white_space_1_xsd.nistschema_sv_iv_list_date_time_white_space_1 import NistschemaSvIvListDateTimeWhiteSpace1
from xsdata.models.datatype import XmlDateTime


obj = NistschemaSvIvListDateTimeWhiteSpace1(
    value=[
        XmlDateTime(1970, 1, 1, 0, 0, 0),
        XmlDateTime(1970, 5, 15, 13, 47, 12),
        XmlDateTime(2018, 1, 26, 4, 26, 7),
        XmlDateTime(2017, 5, 28, 9, 49, 7),
        XmlDateTime(1972, 8, 28, 13, 8, 15),
        XmlDateTime(2028, 7, 6, 7, 29, 30),
        XmlDateTime(2030, 12, 31, 23, 59, 59),
    ]
)
