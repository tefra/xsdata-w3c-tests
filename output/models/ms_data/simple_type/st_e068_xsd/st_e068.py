from dataclasses import dataclass, field
from typing import Union
from xsdata.models.datatype import XmlPeriod


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Union[XmlPeriod, str, int] = field(
        init=False,
        default="a"
    )
