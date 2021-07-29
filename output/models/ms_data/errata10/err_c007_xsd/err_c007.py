from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.tempuri.org"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://www.tempuri.org"

    local_element1: Optional[object] = field(
        default=None,
        metadata={
            "name": "localElement1",
            "type": "Element",
            "namespace": "",
        }
    )
    local_element2: Optional[object] = field(
        default=None,
        metadata={
            "name": "localElement2",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TestContent:
    class Meta:
        name = "testContent"
        namespace = "http://www.tempuri.org"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
