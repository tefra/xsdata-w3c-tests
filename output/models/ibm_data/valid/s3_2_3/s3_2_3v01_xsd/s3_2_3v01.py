from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.schemaTest.org/schema11_S3_2_3"


@dataclass
class Type1:
    """
    :ivar attr1:
    :ivar attr2:
    """
    class Meta:
        name = "type1"

    attr1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.schemaTest.org/schema11_S3_2_3",
        }
    )
    attr2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root:
    """
    :ivar element1:
    """
    class Meta:
        name = "root"
        namespace = "http://www.schemaTest.org/schema11_S3_2_3"

    element1: Optional[Type1] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
