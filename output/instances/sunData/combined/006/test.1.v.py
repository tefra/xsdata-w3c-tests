from output.models.sun_data.combined.pkg_006.test_xsd.test import EB
from output.models.sun_data.combined.pkg_006.test_xsd.test import EDe
from output.models.sun_data.combined.pkg_006.test_xsd.test import EDee
from output.models.sun_data.combined.pkg_006.test_xsd.test import EDer
from output.models.sun_data.combined.pkg_006.test_xsd.test import EDr
from output.models.sun_data.combined.pkg_006.test_xsd.test import EDre
from output.models.sun_data.combined.pkg_006.test_xsd.test import EDrr
from output.models.sun_data.combined.pkg_006.test_xsd.test import Empty
from output.models.sun_data.combined.pkg_006.test_xsd.test import Root


obj = Root(
    choice=[
        EB(
            foo=Empty(

            )
        ),
        EDr(
            foo=Empty(

            )
        ),
        EDe(
            foo=Empty(

            )
        ),
        EDrr(
            foo=Empty(

            )
        ),
        EDre(
            foo=Empty(

            )
        ),
        EDer(
            foo=Empty(

            )
        ),
        EDee(
            foo=Empty(

            )
        ),
    ]
)
