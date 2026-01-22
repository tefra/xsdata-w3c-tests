from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_min_length_1_xsd.nistschema_sv_iv_list_date_min_length_1 import NistschemaSvIvListDateMinLength1
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateMinLength1(
    value=[
        XmlDate(2021, 3, 13),
        XmlDate(1721, 7, 3),
        XmlDate(1921, 7, 13),
        XmlDate(1821, 3, 13),
        XmlDate(1821, 4, 13),
        XmlDate(1921, 8, 23),
    ]
)
