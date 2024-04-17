import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset
from torchmetrics.functional.regression import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
import cgi, sys, codecs, json, os
from flask import Blueprint, render_template, request

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("")
def main_about():
    return render_template("oil_price.html")


@bp.route("", methods=["GET", "POST"])
def main_predict():
    if request.method == "POST":
        select_date = [request.form["select_date"]]
        return print_browser(select_date)
    return render_template("oil_price.html")


class OilPriceDataset(Dataset):
    def __init__(self, data, min_data=None, max_data=None, step=365):
        data = data if isinstance(data, np.ndarray) else data.values
        self.min_data = np.min(data) if min_data is None else min_data
        self.max_data = np.max(data) if max_data is None else max_data
        self.data = (data - self.min_data) / (self.max_data - self.min_data)
        self.data = torch.FloatTensor(self.data)
        self.step = step

    def __len__(self):
        return len(self.data) - self.step

    def __getitem__(self, i):
        data = self.data[i : i + self.step]
        label = self.data[i + self.step].squeeze()
        return data, label


class OilPriceModel(nn.Module):
    def __init__(self, hidden_size, num_layers, step):
        super().__init__()
        self.rnn = nn.GRU(
            input_size=1,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
        )
        self.fc1 = nn.Linear(in_features=hidden_size * step, out_features=64)
        self.fc2 = nn.Linear(in_features=64, out_features=1)

    def forward(self, x):
        x, _ = self.rnn(x)
        x = x.reshape(x.shape[0], -1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        return torch.flatten(x)


def print_browser(select_date="2030-12-31"):
    output_count = (pd.to_datetime(select_date) - pd.to_datetime("2024-04-12")).days
    file_contents = render_template("oil_price.html")

    # test.csv를 읽은 후, 데이터를 JSON 형식으로 변환
    # oil_priceDF = pd.read_csv("../oil_data/oil_price.csv", encoding="utf-8")
    current_dir = os.path.dirname((os.path.dirname(__file__)))
    oil_priceDF = pd.read_csv(
        os.path.join(current_dir, "oil_data/oil_price.csv"), encoding="utf-8"
    )
    # oil_pred_priceDF = pd.read_csv(f"../oil_data/pred_oil_price.csv", encoding="utf-8")
    oil_pred_priceDF = pd.read_csv(
        os.path.join(current_dir, "oil_data/pred_oil_price.csv"), encoding="utf-8"
    )
    labels = list(oil_priceDF["date"]) + list(oil_pred_priceDF["date"])[:output_count]
    data1 = list(oil_priceDF["price"]) + list(oil_pred_priceDF["price"])[:output_count]
    data2 = list(oil_priceDF["price"])

    chart_data = json.dumps({"labels": labels, "data1": data1, "data2": data2})
    # 2030년 12월 31일의 예측 유가 : 99.999$/배럴
    chart_date = (
        pd.to_datetime(select_date).strftime("%Y년 %m월 %d일")
        + "의 예측 유가 : "
        + str(data1[-1])
        + "$/배럴"
    )
    file_contents_with_data = file_contents.replace("REPLACE_DATA", chart_data).replace(
        "예측을 원하는 날짜를 선택하세요", chart_date
    )

    return "Content-Type: text/html; charset=utf-8;\n" + file_contents_with_data


# print(os.path.dirname(__file__))
