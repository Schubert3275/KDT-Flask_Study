import numpy as np
import pandas as pd
import torch, json, os
from flask import Blueprint, render_template, request

from .models import OilPriceModel, OilPriceDataset

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("")
def main_about():
    return render_template("oil_price.html")


@bp.route("", methods=["POST"])
def main_predict():
    if request.method == "POST":
        select_date = request.form["select_date"]
        if request.form.get("re_predict") is not None:
            predict_price(select_date)
        return print_browser(select_date)
    return render_template("oil_price.html")


def predict_price(select_date="2030-12-31"):
    current_dir = os.path.dirname((os.path.dirname(__file__)))
    priceDF = pd.read_csv(
        os.path.join(current_dir, "oil_data/oil_price.csv"),
        encoding="utf-8",
        parse_dates=["date"],
    )

    device = "cuda" if torch.cuda.is_available() else "cpu"
    step = 1825
    min_data = np.min(priceDF["price"].values)
    max_data = np.max(priceDF["price"].values)
    dataset = OilPriceDataset(
        priceDF[["price"]], min_data=min_data, max_data=max_data, step=step
    )

    start_date = priceDF["date"].max() + pd.DateOffset(days=1)
    end_date = pd.to_datetime(select_date)
    full_date_range = pd.date_range(start=start_date, end=end_date)
    pred_days = len(full_date_range)

    preds = []
    pred_model = OilPriceModel(hidden_size=32, num_layers=2, step=step).to(device)
    pred_model.load_state_dict(
        torch.load(
            os.path.join(current_dir, f"oil_data/oil_price_model_state_{step}_cuda.pt"),
            map_location=device,
        ),
        strict=False,
    )
    pred_model.eval()
    start = dataset[len(dataset.data[step:]) - 1][0]
    with torch.no_grad():
        for i in range(pred_days):
            pred = pred_model(start.unsqueeze(0).to(device))
            start = torch.cat((start[1:].to(device), pred.unsqueeze(0)))
            preds.append(pred.item())

    real_preds = [
        x * (float(max_data) - float(min_data)) + float(min_data) for x in preds
    ]

    pred_priceDF = pd.DataFrame({"date": full_date_range, "price": real_preds})
    pred_priceDF["price"] = pred_priceDF["price"].round(3)

    pred_priceDF.to_csv(
        os.path.join(current_dir, "oil_data/pred_oil_price.csv"),
        index=False,
        encoding="utf-8",
    )


def print_browser(select_date="2030-12-31"):
    output_count = (pd.to_datetime(select_date) - pd.to_datetime("2024-04-12")).days
    file_contents = render_template("oil_price.html")

    # test.csv를 읽은 후, 데이터를 JSON 형식으로 변환
    current_dir = os.path.dirname((os.path.dirname(__file__)))
    oil_priceDF = pd.read_csv(
        os.path.join(current_dir, "oil_data/oil_price.csv"), encoding="utf-8"
    )
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

    return file_contents_with_data
