from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_min_length_4_xsd.nistschema_sv_iv_list_date_min_length_4 import NistschemaSvIvListDateMinLength4
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateMinLength4(
    value=[
        XmlDate(1984, 2, 25),
        XmlDate(1784, 2, 5),
        XmlDate(1784, 2, 25),
        XmlDate(1984, 2, 25),
        XmlDate(1984, 2, 5),
        XmlDate(1984, 2, 5),
        XmlDate(2084, 2, 25),
        XmlDate(1984, 2, 15),
        XmlDate(1984, 2, 5),
    ]
)
