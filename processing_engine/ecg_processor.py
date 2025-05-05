import neurokit2 as nk
import numpy as np
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

    def hr(self, ecg_signal):
        """
        Calculate the Heart Rate (HR) from the ECG signal.

        Parameters
        ----------
        ecg_signal : array
            The ECG signal to calculate HR.

        Returns
        -------
        float
            Heart rate value.
        """
        # HR
        ecg_clean = self.preprocessing_ecg(ecg_signal)
        signals, info = nk.ecg_peaks(ecg_clean,sampling_rate=self.sampling_rate)
        heart_rate_mean = np.mean(signals["ECG_Rate"])
        hr = round(heart_rate_mean)

        return hr

    def hrv(self , ecg_signal):
        """
        Calculate the Heart Rate Variability (HRV) from the ECG signal.

        Parameters
        ----------
        ecg_signal : array
            The ECG signal to calculate HRV.

        Returns
        -------
        float
            HRV value.
        """
        # HRV
        ecg_clean = self.preprocessing_ecg(ecg_signal)
        signals, info = nk.ecg_peaks(ecg_clean,sampling_rate=self.sampling_rate, correct_artifacts=True)
        hrv_details = nk.hrv(signals, sampling_rate=self.sampling_rate)
        HRV_MeanNN = hrv_details["HRV_MeanNN"].iloc[0]
        hrv = round(HRV_MeanNN)

        return hrv

    def rr(self, ecg_signal):
        """
        Calculate the RR intervals from the ECG signal.

        Parameters
        ----------
        ecg_signal : array
            The ECG signal to calculate RR intervals.

        Returns
        -------
        float
            RR interval value.
        """
        # RR
        ecg_clean = self.preprocessing_ecg(ecg_signal)
        peaks = nk.ecg_peaks(ecg_clean, sampling_rate=self.sampling_rate, correct_artifacts=True)
        ecg_rate = nk.ecg_rate(peaks, sampling_rate=self.sampling_rate, desired_length=len(ecg_clean))
        edr = nk.ecg_rsp(ecg_rate, sampling_rate=self.sampling_rate)
        rr_signals, info = nk.rsp_process(edr, sampling_rate=self.sampling_rate)
        rr_mean = np.mean(rr_signals["RSP_Rate"])
        rr = round(rr_mean)

        return rr
