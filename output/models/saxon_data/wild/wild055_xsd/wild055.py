from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Zing:
    """
    :ivar any_attributes:
    """
    class Meta:
        name = "zing"

    any_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )


@dataclass
class RestrictedZing(Zing):
    """
    :ivar local_attributes:
    """
    class Meta:
        name = "restrictedZing"

    local_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        }
    )


@dataclass
class Doc(RestrictedZing):
    class Meta:
        name = "doc"
