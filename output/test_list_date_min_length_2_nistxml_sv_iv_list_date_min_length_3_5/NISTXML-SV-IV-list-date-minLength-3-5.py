from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_min_length_3_xsd.nistschema_sv_iv_list_date_min_length_3 import NistschemaSvIvListDateMinLength3
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateMinLength3(
    value=[
        XmlDate(2055, 11, 11),
        XmlDate(2055, 12, 21),
        XmlDate(1955, 10, 21),
        XmlDate(1755, 12, 11),
        XmlDate(1855, 12, 11),
        XmlDate(2055, 12, 11),
        XmlDate(1955, 12, 11),
        XmlDate(1755, 10, 21),
    ]
)
