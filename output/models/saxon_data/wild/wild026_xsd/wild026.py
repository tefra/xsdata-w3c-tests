from dataclasses import dataclass, field
from typing import Dict


@dataclass
class T:
    """
    :ivar any_attributes:
    :ivar adam_com_eve_com_attributes:
    """
    any_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )
    adam_com_eve_com_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="http://adam.com/ http://eve.com/"
        )
    )


@dataclass
class Eden(T):
    class Meta:
        name = "eden"
