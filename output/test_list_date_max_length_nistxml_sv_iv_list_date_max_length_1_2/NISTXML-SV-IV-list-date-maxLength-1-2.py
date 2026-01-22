from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_max_length_1_xsd.nistschema_sv_iv_list_date_max_length_1 import NistschemaSvIvListDateMaxLength1
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateMaxLength1(
    value=[
        XmlDate(2082, 3, 3),
        XmlDate(2082, 3, 1),
        XmlDate(1982, 3, 1),
        XmlDate(2082, 3, 5),
        XmlDate(1882, 3, 8),
    ]
)
