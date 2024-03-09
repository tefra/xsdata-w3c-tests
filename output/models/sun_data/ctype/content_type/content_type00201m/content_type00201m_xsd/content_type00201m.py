from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "contentType"


@dataclass
class A1:
    class Meta:
        name = "A"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class A(A1):
    class Meta:
        name = "a"
        namespace = "contentType"
