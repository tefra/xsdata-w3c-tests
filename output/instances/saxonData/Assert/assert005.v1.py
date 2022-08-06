from output.models.saxon_data.assert_pkg.assert005_xsd.assert005 import Inner
from output.models.saxon_data.assert_pkg.assert005_xsd.assert005 import Outer


obj = Outer(
    inner=[
        Inner(
            a=[
                Inner.A(
                    b=[
                        "",
                    ]
                ),
                Inner.A(
                    b=[
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
                    b=[]
                ),
            ],
            x="205",
            y="204"
        ),
    ]
)
