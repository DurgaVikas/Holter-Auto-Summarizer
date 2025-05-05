import math
import matplotlib.pyplot as plt


def plot_and_save_ecg_segments(ecg_cleaned_df, base_filename="ecg_segment"):
    """
    Plot and save segments of the ECG signal.
    :param ecg_cleaned_df: DataFrame containing the cleaned ECG signal.
    :param ecg_cleaned_df:
    :param base_filename:
    :return:
    """
    segment_size = 800
    num_segments = math.ceil(len(ecg_cleaned_df) / segment_size)

    filenames = []

    for i in range(num_segments):
        start = i * segment_size
        end = start + segment_size
        segment = ecg_cleaned_df[start:end]

        plt.figure(figsize=(10, 4))
        plt.plot(segment, label=f"Segment {i + 1}", color="blue")
        plt.title(f"ECG Segment {i + 1}")
        plt.xlabel("Time (samples)")
        plt.ylabel("Amplitude")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        filename = f"{base_filename}_{i + 1}.png"
        plt.savefig(filename)
        plt.close()

        filenames.append(filename)

    return filenames