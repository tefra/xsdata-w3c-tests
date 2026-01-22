from output.models.nist_data.list_pkg.date_time.schema_instance.nistschema_sv_iv_list_date_time_length_3_xsd.nistschema_sv_iv_list_date_time_length_3 import NistschemaSvIvListDateTimeLength3
from xsdata.models.datatype import XmlDateTime


obj = NistschemaSvIvListDateTimeLength3(
    value=[
        XmlDateTime(1983, 1, 20, 16, 4, 31),
        XmlDateTime(1783, 2, 27, 16, 2, 21),
        XmlDateTime(1783, 9, 25, 6, 5, 31),
        XmlDateTime(2083, 8, 22, 16, 2, 41),
        XmlDateTime(1783, 6, 25, 6, 4, 31),
        XmlDateTime(1883, 8, 26, 16, 0, 41),
        XmlDateTime(1983, 8, 25, 16, 2, 21),
    ]
)
