from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_min_length_5_xsd.nistschema_sv_iv_list_date_min_length_5 import NistschemaSvIvListDateMinLength5
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateMinLength5(
    value=[
        XmlDate(1979, 5, 21),
        XmlDate(1979, 6, 1),
        XmlDate(2079, 3, 11),
        XmlDate(1979, 3, 11),
        XmlDate(2079, 4, 21),
        XmlDate(2079, 5, 21),
        XmlDate(2079, 5, 21),
        XmlDate(1779, 7, 11),
        XmlDate(2079, 9, 21),
        XmlDate(1979, 6, 11),
    ]
)
