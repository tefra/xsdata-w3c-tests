from output.models.ms_data.simple_type.st_e093_xsd.st_e093 import Root
from xml.etree.ElementTree import QName


obj = Root(
    value=[
        12,
        QName("abcdef"),
        4.0,
    ]
)
