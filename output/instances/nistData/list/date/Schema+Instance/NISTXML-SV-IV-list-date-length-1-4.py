from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_length_1_xsd.nistschema_sv_iv_list_date_length_1 import NistschemaSvIvListDateLength1
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateLength1(
    value=[
        XmlDate(1956, 6, 22),
        XmlDate(1973, 6, 25),
        XmlDate(1947, 6, 23),
        XmlDate(1972, 6, 24),
        XmlDate(1937, 6, 22),
    ]
)
