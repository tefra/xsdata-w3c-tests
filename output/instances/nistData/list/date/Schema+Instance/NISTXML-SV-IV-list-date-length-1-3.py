from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_length_1_xsd.nistschema_sv_iv_list_date_length_1 import NistschemaSvIvListDateLength1
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateLength1(
    value=[
        XmlDate(2078, 1, 1),
        XmlDate(1778, 2, 21),
        XmlDate(1978, 8, 1),
        XmlDate(1978, 9, 11),
        XmlDate(2078, 7, 11),
    ]
)
