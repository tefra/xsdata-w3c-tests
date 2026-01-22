from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_length_2_xsd.nistschema_sv_iv_list_date_length_2 import NistschemaSvIvListDateLength2
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateLength2(
    value=[
        XmlDate(1983, 3, 22),
        XmlDate(1952, 3, 22),
        XmlDate(1929, 3, 21),
        XmlDate(1941, 3, 26),
        XmlDate(1998, 3, 25),
        XmlDate(1933, 3, 24),
    ]
)
