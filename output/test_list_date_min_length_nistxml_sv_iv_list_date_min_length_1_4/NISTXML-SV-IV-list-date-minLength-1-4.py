from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_min_length_1_xsd.nistschema_sv_iv_list_date_min_length_1 import NistschemaSvIvListDateMinLength1
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateMinLength1(
    value=[
        XmlDate(1823, 8, 21),
        XmlDate(1823, 8, 21),
        XmlDate(1923, 8, 27),
        XmlDate(1923, 8, 26),
        XmlDate(1823, 8, 20),
        XmlDate(2023, 8, 25),
    ]
)
