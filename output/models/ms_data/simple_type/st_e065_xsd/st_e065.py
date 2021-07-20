from dataclasses import dataclass, field
from typing import Union
from xml.etree.ElementTree import QName
from xsdata.models.datatype import XmlPeriod


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Union[XmlPeriod, str, QName] = field(
        init=False,
        default="abcd edfgh "
    )
