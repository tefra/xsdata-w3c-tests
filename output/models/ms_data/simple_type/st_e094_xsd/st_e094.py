from dataclasses import dataclass, field
from typing import Union
from xml.etree.ElementTree import QName


@dataclass
class Root:
    class Meta:
        name = "root"

    value: list[Union[float, bytes, int, QName]] = field(
        init=False,
        default_factory=lambda: [
            12,
            QName("abcdef"),
            4.0,
            QName("{a}a"),
            QName("{a}b"),
            QName("{b}a"),
            QName("{b}b"),
        ],
        metadata={
            "tokens": True,
        },
    )
