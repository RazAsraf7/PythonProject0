import pandas as pd

df = pd.read_csv("data_car.csv")

# price = int(input("What is the maximum price you want to check? "))
# filtered_df = df['Volume'] <= price

# df['Tax'] = df['Volume'] // 10
# lis = []
# car_list = list(df['Car'])
# for car in df['Car']:
#     if car not in lis:
#         lis.append(car)


df.groupby(['Car'])
print(df)