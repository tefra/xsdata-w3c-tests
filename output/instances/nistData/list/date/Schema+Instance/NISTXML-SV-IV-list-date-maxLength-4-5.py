from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_max_length_4_xsd.nistschema_sv_iv_list_date_max_length_4 import NistschemaSvIvListDateMaxLength4
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateMaxLength4(
    value=[
        XmlDate(1917, 10, 21),
        XmlDate(2017, 10, 27),
        XmlDate(1717, 10, 24),
        XmlDate(2017, 10, 24),
        XmlDate(1917, 10, 22),
        XmlDate(1917, 10, 25),
    ]
)
