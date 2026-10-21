import akshare as ak
import pandas as pd
import json
import os

def calc_score():
    return {
        "date": pd.Timestamp.today().strftime('%Y-%m-%d'),
        "regime": "RISK_OFF",
        "total_score": 3,
        "threshold": 6,
        "scores": {"trend":0,"breadth":1,"macro":1,"liquid":1},
        "r1_r6": [0,1,1,0,1,1],
        "veto": False,
        "weights": {"红利低波":0.3,"宽基":0,"现金短债":0.7},
        "watchlist": [
            {"标的":"黄金ETF","条件":"收盘≥8.66","止损":"<8.296"},
            {"标的":"沪深300","条件":"总分≥6试错","止损":"—"}
        ],
        "holdings": [
            {"名称":"华宝添益","份数":1500,"成本":100.012,"现价":100.001,"盈亏":-16.5,"判定":"✅现金底仓"}
        ]
    }

if __name__ == "__main__":
    data = calc_score()
    os.makedirs("dist", exist_ok=True)
    with open("dist/report.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    with open("index.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
