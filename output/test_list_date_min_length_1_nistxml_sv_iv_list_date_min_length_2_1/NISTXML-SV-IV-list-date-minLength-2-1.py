from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_min_length_2_xsd.nistschema_sv_iv_list_date_min_length_2 import NistschemaSvIvListDateMinLength2
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateMinLength2(
    value=[
        XmlDate(1886, 6, 6),
        XmlDate(1802, 6, 6),
        XmlDate(1885, 6, 5),
        XmlDate(1847, 6, 2),
        XmlDate(1819, 6, 3),
        XmlDate(1825, 6, 6),
        XmlDate(1835, 6, 2),
    ]
)
