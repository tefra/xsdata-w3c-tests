from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "a"


@dataclass
class Nametest:
    choice: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "_ele",
                    "type": str,
                    "namespace": "a",
                },
                {
                    "name": "_-",
                    "type": str,
                    "namespace": "a",
                },
                {
                    "name": "_.",
                    "type": str,
                    "namespace": "a",
                },
                {
                    "name": "_9",
                    "type": str,
                    "namespace": "a",
                },
                {
                    "name": "___",
                    "type": str,
                    "namespace": "a",
                },
                {
                    "name": "a_a",
                    "type": str,
                    "namespace": "a",
                },
                {
                    "name": "a.a",
                    "type": str,
                    "namespace": "a",
                },
                {
                    "name": "ele",
                    "type": str,
                    "namespace": "a",
                },
            ),
        }
    )


@dataclass
class Root(Nametest):
    class Meta:
        name = "root"
        namespace = "a"
