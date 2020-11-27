from dataclasses import dataclass, field
from typing import List, Union

__NAMESPACE__ = "http://foo.com"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://foo.com"

    child1_or_child2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "child1",
                    "type": List[str],
                    "min_length": 5,
                    "tokens": True,
                },
                {
                    "name": "child2",
                    "type": Union[bool, str],
                    "min_length": 5,
                },
            ),
        }
    )
