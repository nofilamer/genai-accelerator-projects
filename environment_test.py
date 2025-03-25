import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openai
import tiktoken
import os
from dotenv import load_dotenv

def check_environment():
    print("Environment successfully configured!")
    print(f"Python version: {os.sys.version}")
    print("\nInstalled packages:")
    print(f"- NumPy: {np.__version__}")
    print(f"- Pandas: {pd.__version__}")
    print(f"- Matplotlib: {plt.matplotlib.__version__}")
    print(f"- OpenAI: {openai.__version__}")
    print(f"- Tiktoken: {tiktoken.__version__}")

if __name__ == "__main__":
    check_environment()
