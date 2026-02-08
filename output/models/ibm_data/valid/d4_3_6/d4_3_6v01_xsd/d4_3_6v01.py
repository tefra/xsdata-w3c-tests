from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "http://xstest-tns/schema11"


class DurWhiteSpace(Enum):
    VALUE = ""


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11"

    el_white_space: DurWhiteSpace = field(
        metadata={
            "name": "elWhiteSpace",
            "type": "Element",
            "namespace": "",
        }
    )
