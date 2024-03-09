from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "MGroup/annotation"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "MGroup/annotation"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TheType:
    class Meta:
        name = "theType"

    c: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
