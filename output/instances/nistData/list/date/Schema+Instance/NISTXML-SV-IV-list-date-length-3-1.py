from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_length_3_xsd.nistschema_sv_iv_list_date_length_3 import NistschemaSvIvListDateLength3
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateLength3(
    value=[
        XmlDate(1753, 1, 6),
        XmlDate(1798, 1, 6),
        XmlDate(1789, 1, 6),
        XmlDate(1707, 1, 6),
        XmlDate(1746, 1, 26),
        XmlDate(1770, 1, 26),
        XmlDate(1778, 1, 16),
    ]
)
