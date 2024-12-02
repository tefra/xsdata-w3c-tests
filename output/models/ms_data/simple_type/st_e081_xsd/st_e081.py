from dataclasses import dataclass, field
from typing import Union

from xsdata.models.datatype import XmlPeriod


@dataclass
class Root:
    class Meta:
        name = "root"

    value: list[Union[XmlPeriod, bool, str]] = field(
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
