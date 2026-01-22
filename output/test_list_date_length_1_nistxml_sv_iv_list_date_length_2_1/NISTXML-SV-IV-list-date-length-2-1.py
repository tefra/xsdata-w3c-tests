from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_length_2_xsd.nistschema_sv_iv_list_date_length_2 import NistschemaSvIvListDateLength2
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateLength2(
    value=[
        XmlDate(1939, 8, 5),
        XmlDate(1901, 1, 3),
        XmlDate(1960, 9, 7),
        XmlDate(1986, 7, 1),
        XmlDate(1975, 3, 5),
        XmlDate(1938, 6, 1),
    ]
)
