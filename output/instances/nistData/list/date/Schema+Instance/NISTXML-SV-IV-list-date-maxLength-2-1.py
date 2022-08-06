from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_max_length_2_xsd.nistschema_sv_iv_list_date_max_length_2 import NistschemaSvIvListDateMaxLength2
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateMaxLength2(
    value=[
        XmlDate(1932, 1, 5),
        XmlDate(1939, 5, 6),
        XmlDate(1913, 3, 5),
        XmlDate(1918, 5, 6),
        XmlDate(1932, 6, 7),
    ]
)
