import unittest
from common.graphs import plot_and_save_ecg_segments
from common.simulate_ecg import simulate_ecg
from processing_engine.ecg_processor import ECGProcessor


class TestECGProcessor(unittest.TestCase):
    def test_preprocessing_ecg(self):
        duration = 10
        sampling_rate = 250  # Hz

        # Simulate ECG signal
        ecg_signal = simulate_ecg(duration=duration, sampling_rate=sampling_rate)

        # Initialize ECGProcessor
        processor = ECGProcessor(duration=duration, sampling_rate=sampling_rate)

        # Preprocess the ECG signal
        ecg_cleaned_df = processor.preprocessing_ecg(ecg_signal)

        # Plot the cleaned ECG signal
        plots = plot_and_save_ecg_segments(ecg_cleaned_df)

        # Assertions
        self.assertIsNotNone(ecg_cleaned_df)
        self.assertIsNotNone(plots)


if __name__ == '__main__':
    unittest.main()