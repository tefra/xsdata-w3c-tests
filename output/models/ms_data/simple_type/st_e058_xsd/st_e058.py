from dataclasses import dataclass, field
from typing import Union
from xsdata.models.datatype import Period


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Union[Period, int, bytes, str] = field(
        init=False,
        default=-25,
        metadata={
            "format": "base64",
        }
    )
