from dataclasses import dataclass, field
from typing import List, Union
from xsdata.models.datatype import XmlPeriod


@dataclass
class Root:
    class Meta:
        name = "root"

    value: List[Union[XmlPeriod, str, int]] = field(
        init=False,
        default_factory=lambda: [
            "a",
            "b",
        ],
        metadata={
            "tokens": True,
        },
    )
