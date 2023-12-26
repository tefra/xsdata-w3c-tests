from dataclasses import dataclass, field
from typing import List, Union
from xml.etree.ElementTree import QName


@dataclass
class Root:
    class Meta:
        name = "root"

    value: List[Union[float, bytes, int, QName]] = field(
        init=False,
        default_factory=lambda: [
            12,
            QName("abcdef"),
            4.0,
        ],
        metadata={
            "tokens": True,
        },
    )
