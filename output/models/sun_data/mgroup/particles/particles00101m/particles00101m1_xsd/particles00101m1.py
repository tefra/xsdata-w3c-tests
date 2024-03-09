from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "particles"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "particles"

    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
