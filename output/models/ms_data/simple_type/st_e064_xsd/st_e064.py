from dataclasses import dataclass, field
from typing import Union
from xml.etree.ElementTree import QName
from xsdata.models.datatype import Period


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Union[Period, str, QName] = field(
        init=False,
        default=QName("abcd edfgh"),
    )
