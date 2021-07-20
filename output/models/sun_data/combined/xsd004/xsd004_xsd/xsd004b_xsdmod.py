from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "zot"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "zot"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class B:
    class Meta:
        name = "b"
        namespace = "zot"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class C:
    class Meta:
        name = "c"
        namespace = "zot"

    value: Optional[str] = field(
        default=None
    )
