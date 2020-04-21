from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict


@dataclass
class Zing:
    """
    :ivar any_attributes:
    """
    class Meta:
        name = "zing"

    any_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )


@dataclass
class RestrictedZing(Zing):
    """
    :ivar local_attributes:
    """
    class Meta:
        name = "restrictedZing"

    local_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##local"
        )
    )


@dataclass
class Doc(RestrictedZing):
    class Meta:
        name = "doc"
