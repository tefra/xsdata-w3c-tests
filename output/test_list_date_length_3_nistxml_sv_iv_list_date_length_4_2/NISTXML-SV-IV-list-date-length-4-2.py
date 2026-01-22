from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_length_4_xsd.nistschema_sv_iv_list_date_length_4 import NistschemaSvIvListDateLength4
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateLength4(
    value=[
        XmlDate(1983, 2, 26),
        XmlDate(1983, 7, 22),
        XmlDate(2083, 5, 20),
        XmlDate(1983, 8, 22),
        XmlDate(1883, 8, 25),
        XmlDate(1983, 7, 20),
        XmlDate(1883, 8, 27),
        XmlDate(1883, 7, 24),
    ]
)
