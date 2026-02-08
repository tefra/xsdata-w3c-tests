from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.tempuri.org"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://www.tempuri.org"

    local_element1: None | object = field(
        default=None,
        metadata={
            "name": "localElement1",
            "type": "Element",
            "namespace": "",
        },
    )
    local_element2: None | object = field(
        default=None,
        metadata={
            "name": "localElement2",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class TestContent:
    class Meta:
        name = "testContent"
        namespace = "http://www.tempuri.org"

    value: int = field()
