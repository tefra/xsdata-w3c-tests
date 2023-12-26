from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/schema11"


class DurWhiteSpace(Enum):
    VALUE = ""


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11"

    el_white_space: Optional[DurWhiteSpace] = field(
        default=None,
        metadata={
            "name": "elWhiteSpace",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
