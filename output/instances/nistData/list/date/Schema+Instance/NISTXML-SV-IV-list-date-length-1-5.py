from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_length_1_xsd.nistschema_sv_iv_list_date_length_1 import NistschemaSvIvListDateLength1
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateLength1(
    value=[
        XmlDate(1759, 1, 12),
        XmlDate(1959, 1, 15),
        XmlDate(1959, 1, 16),
        XmlDate(2059, 1, 13),
        XmlDate(1859, 1, 13),
    ]
)
