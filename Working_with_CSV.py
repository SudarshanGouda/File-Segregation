import pandas as pd
import os
import shutil
parse_error = False

for file in os.listdir('Input_CSV/'):
    file_path = f"{'Input_CSV'}\{file}"
    try:
        df = pd.read_csv(file_path)
        if (len(df.columns))==12:
            shutil.copy(file_path, f"{'Output_csv'}\{file}")

    except Exception:
        parse_error=True
        while parse_error:
            shutil.copy(file_path, f"{'Incorrect_csv'}\{file}")
        continue

    # else:
    #     print(f'{file} is incorrect')
    #     shutil.copy(file_path, f"{'Incorrect_csv'}\{file}")
