from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.schemaTest.org/schema11_S3_2_3"


@dataclass(kw_only=True)
class Type1:
    class Meta:
        name = "type1"

    element1: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.schemaTest.org/schema11_S3_2_3",
            "required": True,
        }
    )
    element2: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Root(Type1):
    class Meta:
        name = "root"
        namespace = "http://www.schemaTest.org/schema11_S3_2_3"
