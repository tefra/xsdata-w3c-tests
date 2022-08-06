from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_length_1_xsd.nistschema_sv_iv_list_date_length_1 import NistschemaSvIvListDateLength1
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateLength1(
    value=[
        XmlDate(1780, 5, 27),
        XmlDate(2080, 5, 26),
        XmlDate(1980, 5, 24),
        XmlDate(1980, 5, 26),
        XmlDate(1880, 5, 28),
    ]
)
