from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.schemaTest.org/schema11_S3_2_3"


@dataclass(kw_only=True)
class Type1:
    class Meta:
        name = "type1"

    attr1: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.schemaTest.org/schema11_S3_2_3",
        },
    )
    attr2: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://www.schemaTest.org/schema11_S3_2_3"

    element1: Type1 = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
