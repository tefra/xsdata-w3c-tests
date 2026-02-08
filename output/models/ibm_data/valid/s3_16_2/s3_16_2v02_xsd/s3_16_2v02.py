from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xstest-tns/IBMd3_16v02"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/IBMd3_16v02"

    elflt_union_c: str = field(
        metadata={
            "name": "elfltUnionC",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9][0-9]",
        }
    )
