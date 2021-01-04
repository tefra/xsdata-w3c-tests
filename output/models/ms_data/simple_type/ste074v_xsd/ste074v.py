from dataclasses import dataclass, field
from typing import Union
from xsdata.models.datatype import Period


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Union[Period, bytes, int] = field(
        init=False,
        default=b"i\xb7\x1d",
        metadata={
            "format": "base64",
        }
    )
