from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_max_length_2_xsd.nistschema_sv_iv_list_date_max_length_2 import NistschemaSvIvListDateMaxLength2
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateMaxLength2(
    value=[
        XmlDate(1998, 12, 26),
        XmlDate(1989, 11, 26),
        XmlDate(1995, 11, 26),
        XmlDate(1916, 10, 16),
        XmlDate(1936, 11, 26),
    ]
)
