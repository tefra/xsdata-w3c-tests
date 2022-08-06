from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_max_length_3_xsd.nistschema_sv_iv_list_date_max_length_3 import NistschemaSvIvListDateMaxLength3
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateMaxLength3(
    value=[
        XmlDate(1792, 9, 24),
        XmlDate(1992, 9, 27),
        XmlDate(2092, 9, 28),
        XmlDate(1892, 9, 27),
        XmlDate(1792, 9, 26),
        XmlDate(1892, 9, 20),
    ]
)
