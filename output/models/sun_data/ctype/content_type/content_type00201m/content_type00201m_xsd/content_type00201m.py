from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "contentType"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "contentType"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
