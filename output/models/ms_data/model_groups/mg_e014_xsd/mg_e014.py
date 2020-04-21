from dataclasses import dataclass, field
from typing import Optional


@dataclass
class PersonName:
    """
    :ivar title:
    """
    class Meta:
        name = "personName"

    title: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )


@dataclass
class SimpleName:
    """
    :ivar title:
    """
    class Meta:
        name = "simpleName"

    title: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )


@dataclass
class Who(SimpleName):
    class Meta:
        name = "who"
