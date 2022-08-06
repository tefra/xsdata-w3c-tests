from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_max_length_3_xsd.nistschema_sv_iv_list_date_max_length_3 import NistschemaSvIvListDateMaxLength3
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateMaxLength3(
    value=[
        XmlDate(1996, 3, 9),
        XmlDate(1934, 3, 19),
        XmlDate(1934, 7, 19),
        XmlDate(1991, 7, 19),
        XmlDate(1982, 8, 19),
    ]
)
