from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_min_length_2_xsd.nistschema_sv_iv_list_date_min_length_2 import NistschemaSvIvListDateMinLength2
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateMinLength2(
    value=[
        XmlDate(1875, 5, 6),
        XmlDate(1875, 5, 26),
        XmlDate(1975, 5, 16),
        XmlDate(1875, 5, 16),
        XmlDate(1775, 5, 6),
        XmlDate(1975, 5, 16),
        XmlDate(1975, 5, 16),
    ]
)
