import neurokit2 as nk


def simulate_ecg(duration:int, sampling_rate:int,heart_rate:int=None):
    """
    Simulate an ECG signal.

    Parameters
    ----------
    duration : int
        Duration of the ECG signal in seconds.
    sampling_rate : int
        Sampling rate of the ECG signal in Hz.
    heart_rate : int, optional
        Heart rate in beats per minute (bpm). If None, a default heart rate will be used.

    Returns
    -------
    ecg_signal : array
        Simulated ECG signal.
        :param duration:
        :param sampling_rate:
        :param heart_rate:
    """
    # Simulate an ECG signal using NeuroKit2
    if heart_rate is None:
        ecg_signal = nk.ecg_simulate(duration=duration, sampling_rate=sampling_rate)
    else:
        ecg_signal = nk.ecg_simulate(duration=duration, sampling_rate=sampling_rate, heart_rate=heart_rate)

    return ecg_signal