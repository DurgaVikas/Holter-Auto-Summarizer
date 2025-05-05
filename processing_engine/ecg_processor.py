import neurokit2 as nk
import pandas as pd


class ECGProcessor:
    def __init__(self, duration: int, sampling_rate: int):
        """
        Initialize the ECGProcessor.

        Parameters
        ----------
        duration : int
            Duration of the ECG signal in seconds.
        sampling_rate : int
            Sampling rate of the ECG signal in Hz.
        """
        self.duration = duration
        self.sampling_rate = sampling_rate

    def preprocessing_ecg(self, ecg_signal):
        """
        Preprocess the ECG signal.

        Parameters
        ----------
        ecg_signal : array
            The ECG signal to preprocess.

        Returns
        -------
        pd.DataFrame
            Preprocessed ECG signal.
        """
        # Preprocess the ECG signal using NeuroKit2
        signals,info = nk.ecg_process(ecg_signal, sampling_rate=self.sampling_rate)
        ecg_clean = signals["ECG_Clean"]
        return ecg_clean
