from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "contentType"


@dataclass(kw_only=True)
class A1:
    class Meta:
        name = "A"

    value: XmlDate = field()


@dataclass(kw_only=True)
class A(A1):
    class Meta:
        name = "a"
        namespace = "contentType"
