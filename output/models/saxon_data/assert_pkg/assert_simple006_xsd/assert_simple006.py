from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime


@dataclass
class Value:
    class Meta:
        name = "value"

    value: Optional[Union[XmlDate, XmlDateTime]] = field(default=None)


@dataclass
class Outer:
    class Meta:
        name = "outer"

    value: list[Value] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
