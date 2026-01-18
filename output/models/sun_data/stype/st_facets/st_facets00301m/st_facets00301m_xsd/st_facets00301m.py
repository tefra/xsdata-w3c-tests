from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class TestValue(Enum):
    VALUE_3_14 = "3.14"
    INT = "int"


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"
        namespace = "SType/ST_facets"

    value: TestValue = field()
