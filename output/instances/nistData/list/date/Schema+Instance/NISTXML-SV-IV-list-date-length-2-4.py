from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_length_2_xsd.nistschema_sv_iv_list_date_length_2 import NistschemaSvIvListDateLength2
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateLength2(
    value=[
        XmlDate(1910, 12, 10),
        XmlDate(1910, 11, 10),
        XmlDate(2010, 10, 10),
        XmlDate(2010, 11, 10),
        XmlDate(1910, 12, 20),
        XmlDate(1910, 10, 10),
    ]
)
