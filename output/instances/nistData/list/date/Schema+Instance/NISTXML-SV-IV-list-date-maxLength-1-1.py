from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_max_length_1_xsd.nistschema_sv_iv_list_date_max_length_1 import NistschemaSvIvListDateMaxLength1
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateMaxLength1(
    value=[
        XmlDate(1931, 5, 22),
        XmlDate(2031, 4, 2),
        XmlDate(1931, 3, 2),
        XmlDate(1931, 4, 22),
        XmlDate(1931, 4, 12),
    ]
)
