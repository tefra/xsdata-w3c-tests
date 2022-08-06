from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_min_length_1_xsd.nistschema_sv_iv_list_date_min_length_1 import NistschemaSvIvListDateMinLength1
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateMinLength1(
    value=[
        XmlDate(2038, 3, 13),
        XmlDate(1738, 2, 10),
        XmlDate(1738, 6, 12),
        XmlDate(1938, 4, 16),
        XmlDate(1738, 5, 13),
        XmlDate(1838, 3, 13),
        XmlDate(1838, 8, 12),
    ]
)
