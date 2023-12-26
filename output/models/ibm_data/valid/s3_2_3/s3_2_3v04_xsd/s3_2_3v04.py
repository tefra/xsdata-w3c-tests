from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.schemaTest.org/schema11_S3_2_3"


@dataclass
class Type1:
    class Meta:
        name = "type1"

    element1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.schemaTest.org/schema11_S3_2_3",
            "required": True,
        },
    )
    element2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Root(Type1):
    class Meta:
        name = "root"
        namespace = "http://www.schemaTest.org/schema11_S3_2_3"
