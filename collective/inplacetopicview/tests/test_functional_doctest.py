import unittest
import doctest

from zope.testing import doctestunit
from Testing import ZopeTestCase as ztc

from collective.inplacetopicview.tests import base

def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above
    """

    return unittest.TestSuite([

        ztc.ZopeDocFileSuite(
            'functional.txt', package='collective.inplacetopicview.tests',
            test_class=base.FunctionalTestCase,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE | 
                        doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS),
        ])
