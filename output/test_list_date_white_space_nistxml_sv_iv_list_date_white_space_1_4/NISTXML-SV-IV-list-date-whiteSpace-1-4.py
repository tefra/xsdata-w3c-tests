from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_white_space_1_xsd.nistschema_sv_iv_list_date_white_space_1 import NistschemaSvIvListDateWhiteSpace1
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateWhiteSpace1(
    value=[
        XmlDate(1970, 1, 1),
        XmlDate(1984, 6, 26),
        XmlDate(2015, 11, 15),
        XmlDate(1973, 7, 21),
        XmlDate(1991, 10, 13),
        XmlDate(1977, 8, 31),
        XmlDate(2030, 12, 31),
    ]
)
