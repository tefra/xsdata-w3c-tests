from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_length_3_xsd.nistschema_sv_iv_list_date_length_3 import NistschemaSvIvListDateLength3
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateLength3(
    value=[
        XmlDate(1907, 12, 13),
        XmlDate(1918, 11, 13),
        XmlDate(1930, 12, 13),
        XmlDate(1994, 11, 13),
        XmlDate(1951, 11, 13),
        XmlDate(1910, 10, 13),
        XmlDate(1953, 10, 13),
    ]
)
