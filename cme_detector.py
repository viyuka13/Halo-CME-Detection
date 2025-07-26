import pandas as pd

def detect_cme(df):
    try:
        # Ensure required columns are present
        if 'obs_time' not in df.columns or 'peak_det_counts' not in df.columns:
            return "Required columns not found in the file.", False

        # Convert timestamp
        df['datetime'] = pd.to_datetime(df['obs_time'], unit='s')
        df['peak_det_counts'] = pd.to_numeric(df['peak_det_counts'], errors='coerce')
        df = df.dropna(subset=['peak_det_counts'])

        # Basic threshold-based detection
        threshold = df['peak_det_counts'].mean() + 2 * df['peak_det_counts'].std()
        potential_cmes = df[df['peak_det_counts'] > threshold]

        if len(potential_cmes) > 0:
            return f"⚠️ CME Warning! {len(potential_cmes)} potential event(s) detected.", True
        else:
            return "✅ No CME activity detected.", False

    except Exception as e:
        return f"An error occurred: {e}", False
