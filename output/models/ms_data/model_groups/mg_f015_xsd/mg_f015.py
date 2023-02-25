from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Foo:
    class Meta:
        name = "foo"

    one: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    two: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    three: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    four: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    five_or_five2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "five",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "five2",
                    "type": object,
                    "namespace": "",
                },
            ),
            "max_occurs": 2,
        }
    )
    six_or_six2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "six",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "six2",
                    "type": object,
                    "namespace": "",
                },
            ),
            "max_occurs": 2,
        }
    )
    seven_or_seven2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "seven",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "seven2",
                    "type": object,
                    "namespace": "",
                },
            ),
            "max_occurs": 2,
        }
    )
    eight_or_eight2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "eight",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "eight2",
                    "type": object,
                    "namespace": "",
                },
            ),
            "max_occurs": 2,
        }
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
