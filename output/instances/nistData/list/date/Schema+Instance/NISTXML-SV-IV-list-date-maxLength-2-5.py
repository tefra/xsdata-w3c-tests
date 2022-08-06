from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_max_length_2_xsd.nistschema_sv_iv_list_date_max_length_2 import NistschemaSvIvListDateMaxLength2
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateMaxLength2(
    value=[
        XmlDate(2077, 7, 7),
        XmlDate(1777, 4, 4),
        XmlDate(1977, 3, 3),
        XmlDate(2077, 7, 2),
        XmlDate(1977, 2, 8),
        XmlDate(1877, 8, 5),
    ]
)
