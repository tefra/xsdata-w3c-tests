from __future__ import annotations

from dataclasses import dataclass

__NAMESPACE__ = "http://open205x.com/"


@dataclass(kw_only=True)
class BType:
    class Meta:
        name = "bType"
