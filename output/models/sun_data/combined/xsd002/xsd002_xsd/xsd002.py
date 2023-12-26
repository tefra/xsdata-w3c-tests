from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://foo.com"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://foo.com"

    foo_or_bar_or_zot: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "bar",
                    "type": object,
                },
                {
                    "name": "zot",
                    "type": object,
                    "namespace": "",
                },
            ),
        },
    )
