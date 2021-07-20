from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class Global1:
    class Meta:
        namespace = "ElemDecl/name"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class Global2:
    class Meta:
        namespace = "ElemDecl/name"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    value: Optional[str] = field(
        default=None
    )
