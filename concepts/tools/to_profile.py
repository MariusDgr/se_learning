
import pandas as pd
import numpy as np

from memory_profiler import profile

def do_some_processing(df):
    df = df.copy()
    for col in df.columns:
        df[col] = df[col] + 1
    return df

@profile
def main():
    cols = ["a", "b", "c", "d", "e"]
    data_dict = {}
    for key in cols:
        data_dict[key] = np.random.normal(size=100000)
        
    # print(data_dict)
    df = pd.DataFrame(data_dict)
    # print(df)

    df = do_some_processing(df)

    df_c = do_some_processing(df)

    print("end")

if __name__ == "__main__":
    main()