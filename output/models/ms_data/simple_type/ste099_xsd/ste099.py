from dataclasses import dataclass, field
from typing import List, Union
from xsdata.models.datatype import Period


@dataclass
class Root:
    class Meta:
        name = "root"

    value: List[Union[Period, bytes]] = field(
        init=False,
        default_factory=lambda: [
            b"i\xb7\x1dy\xf6\x9b",
        ],
        metadata={
            "tokens": True,
            "format": "base64",
        }
    )
