from dataclasses import dataclass, field
from typing import List, Union
from xsdata.models.datatype import XmlPeriod


@dataclass
class Root:
    class Meta:
        name = "root"

    value: List[Union[XmlPeriod, bool, str]] = field(
        init=False,
        default_factory=lambda: [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
        ],
        metadata={
            "tokens": True,
        },
    )
