from __future__ import annotations

from dataclasses import dataclass

from output.models.ms_data.complex_type.ct_e019_a_xsd.ct_e019_b import FooType

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class Doc(FooType):
    class Meta:
        name = "doc"
        namespace = "a"
