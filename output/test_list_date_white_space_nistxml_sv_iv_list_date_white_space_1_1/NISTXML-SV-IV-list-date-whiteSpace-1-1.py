from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_white_space_1_xsd.nistschema_sv_iv_list_date_white_space_1 import NistschemaSvIvListDateWhiteSpace1
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateWhiteSpace1(
    value=[
        XmlDate(1970, 1, 1),
        XmlDate(1986, 10, 9),
        XmlDate(2023, 3, 8),
        XmlDate(1996, 7, 28),
        XmlDate(1994, 7, 23),
        XmlDate(2017, 3, 26),
        XmlDate(1997, 12, 23),
        XmlDate(2030, 12, 31),
    ]
)
