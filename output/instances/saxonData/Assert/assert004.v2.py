from output.models.saxon_data.assert_pkg.assert004_xsd.assert004 import Inner
from output.models.saxon_data.assert_pkg.assert004_xsd.assert004 import Outer


obj = Outer(
    inner=[
        Inner(
            a=[
                Inner.A(
                    b=[
                        "",
                        "",
                    ]
                ),
                Inner.A(
                    b=[
                        "",
                        "",
                    ]
                ),
            ],
            x="205",
            y="204"
        ),
        Inner(
            a=[
                Inner.A(
                    b=[
                        "",
                        "",
                    ]
                ),
                Inner.A(
                    b=[
                        "",
                        "",
                    ]
                ),
            ],
            x="205",
            y="204"
        ),
    ]
)
