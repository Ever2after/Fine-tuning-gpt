import gpt
import pandas as pd

questions = [
    "What is the key architecture of dialogue-based image editing model?",
]

df = pd.DataFrame(questions, columns = ["question"])
df["question"] = df.question.apply(lambda x: f"Q: {x}\nA: ")

df["gpt3"] = df.question.apply(gpt.gpt3)
df["ft_gpt"] = df.question.apply(gpt.ft_gpt)

df.to_csv("result.csv")