from output.models.nist_data.list_pkg.date_time.schema_instance.nistschema_sv_iv_list_date_time_max_length_5_xsd.nistschema_sv_iv_list_date_time_max_length_5 import NistschemaSvIvListDateTimeMaxLength5
from xsdata.models.datatype import XmlDateTime


obj = NistschemaSvIvListDateTimeMaxLength5(
    value=[
        XmlDateTime(2050, 2, 10, 13, 15, 25),
        XmlDateTime(1850, 2, 20, 3, 35, 26),
        XmlDateTime(1850, 2, 10, 3, 15, 20),
        XmlDateTime(1850, 2, 10, 3, 55, 22),
        XmlDateTime(1950, 2, 20, 13, 15, 27),
        XmlDateTime(1850, 2, 20, 13, 45, 25),
        XmlDateTime(1950, 2, 10, 13, 35, 22),
        XmlDateTime(1950, 2, 10, 13, 45, 27),
    ]
)
