import pytest
import numpy as np
from quadrantdetector import detector

axis_size = 1000


@pytest.fixture(scope='session')
def get_detectors():
    """
    Returns a list of 200 detectors with increasingly large gaps, the last
    being gaps larger than the actual detector.
    """
    return [(gap, detector.create_detector(axis_size, 10, gap))
            for gap in np.linspace(1e-14, 1, 50)] \
           + [(gap, detector.create_detector(axis_size, 10, gap))
              for gap in np.linspace(1, 11, 50)]


def test_detector_init(get_detectors):
    for gap, detect in get_detectors:
        assert detect.shape == (axis_size, axis_size)

        axis_0_zeros = 0
        axis_1_zeros = 0
        density = axis_size / 10
        inset = min(int((axis_size // 2) + (gap * density // 2) + 2), axis_size - 1)
        # Use the fact that the detector is NxN for easier checking.
        for i in range(len(detect)):
            # On each gap, there is a minimum of gap - 2 cells on the detector
            # that are 0.
            # The cases are : gap - 2 of 0s, 2 values on either side < 1.
            #                 gap of 0s.
            # We also have to deal with the zeroed out borders of the detector.

            if not detect[i, inset]:
                axis_0_zeros += 1

            if not detect[inset, i]:
                axis_1_zeros += 1

        assert axis_0_zeros >= min(gap * density - 2, axis_size)
        assert axis_1_zeros >= min(gap * density - 2, axis_size)


def test_laser():
    # Test a laser on an empty grid.
    # On our 1000x1000 grid @ 10mm, the sum of a Guassian beam is 10k.
    # In real life, we have a finite grid, so > 9999.
    # Pick a bound for sigma where the majority is visibly on the grid.
    for sigma in np.linspace(1e-2, 1, 50):
        grid = np.ones([1000, 1000])
        laser = detector.laser(grid, 10 / axis_size, 0, 0, sigma)
        assert 10001 > laser.sum() > 9999


def test_compute_signals(get_detectors):
    for gap, detect in get_detectors:
        # get_detectors created a sequence of detectors centered, so all
        # signals should be symmetric.
        sum_signal, lr_signal, tb_signal = detector.compute_signals(detector.laser(detect, 10 / axis_size, 0, 0, 2.0),
                                                                    detect)
        assert sum_signal >= lr_signal and sum_signal >= tb_signal
