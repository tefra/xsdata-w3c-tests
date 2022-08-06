from output.models.nist_data.list_pkg.date_time.schema_instance.nistschema_sv_iv_list_date_time_length_2_xsd.nistschema_sv_iv_list_date_time_length_2 import NistschemaSvIvListDateTimeLength2
from xsdata.models.datatype import XmlDateTime


obj = NistschemaSvIvListDateTimeLength2(
    value=[
        XmlDateTime(1796, 4, 10, 12, 6, 42),
        XmlDateTime(2096, 5, 20, 12, 3, 2),
        XmlDateTime(2096, 5, 10, 12, 2, 22),
        XmlDateTime(1796, 5, 20, 2, 6, 22),
        XmlDateTime(1896, 8, 20, 2, 4, 42),
        XmlDateTime(1996, 3, 10, 2, 1, 32),
    ]
)
