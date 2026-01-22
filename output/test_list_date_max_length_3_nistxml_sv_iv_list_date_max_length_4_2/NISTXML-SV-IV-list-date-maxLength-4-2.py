from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_max_length_4_xsd.nistschema_sv_iv_list_date_max_length_4 import NistschemaSvIvListDateMaxLength4
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateMaxLength4(
    value=[
        XmlDate(2070, 5, 24),
        XmlDate(1770, 5, 26),
        XmlDate(1970, 5, 25),
        XmlDate(1770, 5, 24),
        XmlDate(1970, 5, 22),
        XmlDate(1770, 5, 23),
        XmlDate(1970, 5, 27),
    ]
)
