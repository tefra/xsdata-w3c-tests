from dataclasses import dataclass, field
from typing import Optional, Union
from xml.etree.ElementTree import QName
from xsdata.models.datatype import Period


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Optional[Union[Period, QName, int]] = field(
        default=None,
    )
