from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class Zing:
    class Meta:
        name = "zing"

    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass
class RestrictedZing(Zing):
    class Meta:
        name = "restrictedZing"

    any_attributes: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    local_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        },
    )


@dataclass
class Doc(RestrictedZing):
    class Meta:
        name = "doc"
