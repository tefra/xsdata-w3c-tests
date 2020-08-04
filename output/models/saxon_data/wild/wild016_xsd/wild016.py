from dataclasses import dataclass, field
from typing import Dict


@dataclass
class B:
    """
    :ivar any_attributes:
    """
    any_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )


@dataclass
class E(B):
    """
    :ivar abel_com_adam_com_attributes:
    """
    abel_com_adam_com_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="http://abel.com/ http://adam.com/"
        )
    )


@dataclass
class Eden(E):
    class Meta:
        name = "eden"
