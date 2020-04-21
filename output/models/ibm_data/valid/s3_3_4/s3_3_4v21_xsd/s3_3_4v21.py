from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class Root:
    """
    :ivar value:
    :ivar idref_attr:
    """
    class Meta:
        name = "root"

    value: Optional[Union[int, bool, str]] = field(
        default=None,
    )
    idref_attr: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Wrapper:
    """
    :ivar root:
    """
    class Meta:
        name = "wrapper"

    root: Optional[Root] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
