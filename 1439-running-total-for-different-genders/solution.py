import pandas as pd

def running_total(scores: pd.DataFrame) -> pd.DataFrame:
    #print(scores)
    #scores = scores.sort_values(by="score_points")
    scores = scores.sort_values(by="day")
    #scores = scores.sort_values(by="gender")
    female = scores[scores["gender"] == "F"]
    female["total"] = female["score_points"].cumsum()
    male = scores[scores["gender"] == "M"]
    male["total"] = male["score_points"].cumsum()
    scores = pd.concat([female, male])
    scores = scores.drop(columns = ["player_name", "score_points"])
    
    return scores
    
