from dataclasses import dataclass, field
from typing import Union
from xsdata.models.datatype import XmlPeriod


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Union[XmlPeriod, bytes, int] = field(
        init=False,
        default=b"i\xb7\x1d",
        metadata={
            "format": "base64",
        }
    )
