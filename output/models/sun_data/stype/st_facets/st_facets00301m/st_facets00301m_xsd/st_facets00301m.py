from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum

__NAMESPACE__ = "SType/ST_facets"


class TestValue(StrEnum):
    VALUE_3_14 = "3.14"
    INT = "int"


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"
        namespace = "SType/ST_facets"

    value: TestValue = field()
