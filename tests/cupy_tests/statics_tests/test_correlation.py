import unittest

from cupy import testing


@testing.gpu
class TestCorrelation(unittest.TestCase):

    _multiprocess_can_split_ = True

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_corrcoef(self, xp, dtype):
        a = testing.shaped_arange((2, 3), xp, dtype)
        return xp.corrcoef(a)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_corrcoef_y(self, xp, dtype):
        a = testing.shaped_arange((2, 3), xp, dtype)
        y = testing.shaped_arange((2, 3), xp, dtype)
        return xp.corrcoef(a, y=y)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_corrcoef_rowvar(self, xp, dtype):
        a = testing.shaped_arange((2, 3), xp, dtype)
        y = testing.shaped_arange((2, 3), xp, dtype)
        return xp.corrcoef(a, y=y, rowvar=False)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_cov(self, xp, dtype):
        a = testing.shaped_arange((2, 3), xp, dtype)
        return xp.cov(a)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_cov_y(self, xp, dtype):
        a = testing.shaped_arange((2, 3), xp, dtype)
        y = testing.shaped_arange((2, 3), xp, dtype)
        return xp.cov(a, y=y)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_cov_rowvar(self, xp, dtype):
        a = testing.shaped_arange((2, 3), xp, dtype)
        y = testing.shaped_arange((2, 3), xp, dtype)
        return xp.cov(a, y=y, rowvar=False)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_cov_bias(self, xp, dtype):
        a = testing.shaped_arange((2, 3), xp, dtype)
        return xp.cov(a, bias=True)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_cov_ddof(self, xp, dtype):
        a = testing.shaped_arange((2, 3), xp, dtype)
        return xp.cov(a, ddof=2)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_raises()
    def test_cov_invalid_ddof(self, xp, dtype):
        a = testing.shaped_arange((2, 3), xp, dtype)
        return xp.cov(a, ddof=[])

    @testing.for_all_dtypes()
    @testing.numpy_cupy_raises()
    def test_cov_too_much_ndim(self, xp, dtype):
        a = testing.shaped_arange((3, 4, 2), xp, dtype)
        return xp.cov(a)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_raises()
    def test_cov_y_too_much_ndim(self, xp, dtype):
        a = testing.shaped_arange((2, 3), xp, dtype)
        y = testing.shaped_arange((3, 4, 2), xp, dtype)
        return xp.cov(a, y=y)
