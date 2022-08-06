from output.models.nist_data.list_pkg.date_time.schema_instance.nistschema_sv_iv_list_date_time_length_1_xsd.nistschema_sv_iv_list_date_time_length_1 import NistschemaSvIvListDateTimeLength1
from xsdata.models.datatype import XmlDateTime


obj = NistschemaSvIvListDateTimeLength1(
    value=[
        XmlDateTime(1938, 6, 27, 2, 58, 10),
        XmlDateTime(2038, 6, 25, 2, 28, 11),
        XmlDateTime(1838, 6, 20, 2, 18, 18),
        XmlDateTime(1838, 6, 24, 12, 28, 13),
        XmlDateTime(2038, 6, 25, 12, 48, 18),
    ]
)
