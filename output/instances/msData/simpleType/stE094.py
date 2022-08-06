from output.models.ms_data.simple_type.st_e094_xsd.st_e094 import Root
from xml.etree.ElementTree import QName


obj = Root(
    value=[
        12,
        QName("abcdef"),
        4.0,
        QName("{a}a"),
        QName("{a}b"),
        QName("{b}a"),
        QName("{b}b"),
    ]
)
