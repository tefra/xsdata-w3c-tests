from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_length_2_xsd.nistschema_sv_iv_list_date_length_2 import NistschemaSvIvListDateLength2
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateLength2(
    value=[
        XmlDate(2013, 6, 8),
        XmlDate(1913, 4, 28),
        XmlDate(2013, 3, 8),
        XmlDate(1713, 4, 28),
        XmlDate(1913, 5, 8),
        XmlDate(2013, 5, 18),
    ]
)
