from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_white_space_1_xsd.nistschema_sv_iv_list_date_white_space_1 import NistschemaSvIvListDateWhiteSpace1
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateWhiteSpace1(
    value=[
        XmlDate(1970, 1, 1),
        XmlDate(1985, 8, 17),
        XmlDate(2014, 4, 30),
        XmlDate(1975, 12, 28),
        XmlDate(2009, 1, 14),
        XmlDate(2002, 12, 19),
        XmlDate(2030, 12, 31),
    ]
)
