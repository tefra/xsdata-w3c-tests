from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_length_3_xsd.nistschema_sv_iv_list_date_length_3 import NistschemaSvIvListDateLength3
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateLength3(
    value=[
        XmlDate(1926, 4, 15),
        XmlDate(1995, 4, 11),
        XmlDate(1949, 4, 18),
        XmlDate(1971, 4, 17),
        XmlDate(1933, 4, 17),
        XmlDate(1989, 4, 11),
        XmlDate(1962, 4, 11),
    ]
)
