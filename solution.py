import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    x = np.log(x - 163)
    return x.mean() # Ваш ответ
