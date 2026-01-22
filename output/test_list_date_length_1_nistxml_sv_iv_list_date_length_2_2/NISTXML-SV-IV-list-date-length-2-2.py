from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_length_2_xsd.nistschema_sv_iv_list_date_length_2 import NistschemaSvIvListDateLength2
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateLength2(
    value=[
        XmlDate(1980, 3, 2),
        XmlDate(1995, 3, 12),
        XmlDate(1995, 3, 12),
        XmlDate(1966, 3, 12),
        XmlDate(1931, 3, 22),
        XmlDate(1950, 3, 22),
    ]
)
