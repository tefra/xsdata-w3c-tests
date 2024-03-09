from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "psContents"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "psContents"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Date:
    class Meta:
        name = "date"
        namespace = "psContents"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
