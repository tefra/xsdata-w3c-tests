from dataclasses import dataclass, field
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate, XmlDateTime


@dataclass
class Outer:
    class Meta:
        name = "outer"

    value: List[Union[XmlDate, XmlDateTime]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Value:
    class Meta:
        name = "value"

    value: Optional[Union[XmlDate, XmlDateTime]] = field(default=None)
