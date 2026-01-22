from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_min_length_3_xsd.nistschema_sv_iv_list_date_min_length_3 import NistschemaSvIvListDateMinLength3
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateMinLength3(
    value=[
        XmlDate(1959, 6, 23),
        XmlDate(2059, 5, 3),
        XmlDate(1859, 2, 13),
        XmlDate(1959, 4, 13),
        XmlDate(1959, 5, 3),
        XmlDate(1959, 3, 23),
        XmlDate(1959, 1, 13),
    ]
)
