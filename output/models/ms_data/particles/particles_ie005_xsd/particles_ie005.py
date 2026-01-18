from __future__ import annotations

from dataclasses import dataclass

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Base:
    class Meta:
        name = "base"


@dataclass(kw_only=True)
class Testing(Base):
    class Meta:
        name = "testing"


@dataclass(kw_only=True)
class Doc(Testing):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"
