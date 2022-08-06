from output.models.nist_data.list_pkg.date.schema_instance.nistschema_sv_iv_list_date_min_length_5_xsd.nistschema_sv_iv_list_date_min_length_5 import NistschemaSvIvListDateMinLength5
from xsdata.models.datatype import XmlDate


obj = NistschemaSvIvListDateMinLength5(
    value=[
        XmlDate(1786, 10, 11),
        XmlDate(1886, 11, 1),
        XmlDate(1886, 11, 11),
        XmlDate(1886, 11, 11),
        XmlDate(1786, 10, 11),
        XmlDate(1886, 11, 1),
        XmlDate(1986, 11, 11),
        XmlDate(1986, 11, 11),
        XmlDate(1786, 12, 21),
        XmlDate(1986, 10, 11),
    ]
)
