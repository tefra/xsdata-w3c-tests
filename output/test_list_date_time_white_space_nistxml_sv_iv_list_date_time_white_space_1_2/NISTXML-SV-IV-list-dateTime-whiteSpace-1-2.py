from output.models.nist_data.list_pkg.date_time.schema_instance.nistschema_sv_iv_list_date_time_white_space_1_xsd.nistschema_sv_iv_list_date_time_white_space_1 import NistschemaSvIvListDateTimeWhiteSpace1
from xsdata.models.datatype import XmlDateTime


obj = NistschemaSvIvListDateTimeWhiteSpace1(
    value=[
        XmlDateTime(1970, 1, 1, 0, 0, 0),
        XmlDateTime(2020, 5, 4, 11, 3, 11),
        XmlDateTime(1985, 3, 7, 6, 58, 32),
        XmlDateTime(1971, 5, 25, 1, 42, 15),
        XmlDateTime(2030, 12, 31, 23, 59, 59),
    ]
)
