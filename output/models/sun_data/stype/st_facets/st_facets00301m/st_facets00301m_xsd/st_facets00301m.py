from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "SType/ST_facets"


@dataclass
class Test:
    class Meta:
        name = "test"
        namespace = "SType/ST_facets"

    value: Optional["Test.Value"] = field(
        default=None,
    )

    class Value(Enum):
        VALUE_3_14 = "3.14"
        INT_VALUE = "int"
