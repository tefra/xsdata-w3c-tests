from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class A:
    a: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        }
    )


@dataclass
class B:
    b: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        }
    )


@dataclass
class Base:
    """
    Documentation documentation bar.
    """
    class Meta:
        name = "base"

    e1_or_e2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": A,
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "e2",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
            ),
        }
    )


@dataclass
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"
