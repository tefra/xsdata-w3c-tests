from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "SType/ST_facets"


@dataclass
class Test:
    """
    :ivar value:
    """
    class Meta:
        name = "test"
        namespace = "SType/ST_facets"

    value: Optional["Test.Value"] = field(
        default=None,
    )

    class Value(Enum):
        """
        :cvar VALUE_3_14:
        :cvar INT_VALUE:
        """
        VALUE_3_14 = "3.14"
        INT_VALUE = "int"
