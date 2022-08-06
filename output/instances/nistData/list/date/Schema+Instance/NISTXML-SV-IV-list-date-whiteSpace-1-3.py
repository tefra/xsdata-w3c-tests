from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_white_space_1_xsd.nistschema_sv_iv_list_date_white_space_1 import NistschemaSvIvListDateWhiteSpace1
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateWhiteSpace1(
    value=[
        XmlDate(1970, 1, 1),
        XmlDate(2016, 9, 20),
        XmlDate(2022, 9, 18),
        XmlDate(1970, 10, 2),
        XmlDate(2021, 11, 30),
        XmlDate(2026, 10, 22),
        XmlDate(2019, 4, 11),
        XmlDate(2030, 12, 31),
    ]
)
