import datetime
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gpxtrackposter.exceptions import TrackLoadError
from gpxtrackposter.track import Track


class TrackValidationTest(unittest.TestCase):
    def make_track(self):
        track = Track()
        track.start_time = datetime.datetime(
            2025, 10, 9, 12, 0, tzinfo=datetime.timezone.utc
        )
        track.end_time = datetime.datetime(
            2025, 10, 9, 12, 30, tzinfo=datetime.timezone.utc
        )
        track.start_time_local = datetime.datetime(2025, 10, 9, 20, 0)
        track.end_time_local = datetime.datetime(2025, 10, 9, 20, 30)
        track.moving_dict = {
            "moving_time": datetime.timedelta(minutes=20),
            "elapsed_time": datetime.timedelta(minutes=30),
        }
        return track

    def test_rejects_unreasonable_local_year(self):
        track = self.make_track()
        track.start_time_local = datetime.datetime(7518, 5, 11, 5, 53, 34)

        with self.assertRaises(TrackLoadError):
            track._validate_loaded_track()

    def test_rejects_end_before_start(self):
        track = self.make_track()
        track.end_time = track.start_time - datetime.timedelta(minutes=1)

        with self.assertRaises(TrackLoadError):
            track._validate_loaded_track()

    def test_rejects_negative_moving_time(self):
        track = self.make_track()
        track.moving_dict["moving_time"] = datetime.timedelta(days=-1)

        with self.assertRaises(TrackLoadError):
            track._validate_loaded_track()


if __name__ == "__main__":
    unittest.main()
