from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from xml.etree.ElementTree import QName

__NAMESPACE__ = "a"


class Type(Enum):
    X = QName("{a}x")


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "a"

    value: Type = field()
