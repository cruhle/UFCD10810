#PARTE - VIII
#pandas
# 2-2


import pandas as pd

df = pd.DataFrame({"aluno": ["Ana", "Rui", "Marta"],"nota": [16, 9, 14],})

print(df.head())                # primeiras linhas
print(df["nota"].mean())        # 13.0
print(df[df["nota"] >= 10])     # só os aprovados

# 2-2

from sklearn.tree import DecisionTreeClassifier

X = df[["horas_estudo"]]                        # atributos (colunas)
y = df["aprovado"]                              # alvo

modelo = DecisionTreeClassifier(max_depth=3)    # objeto
modelo.fit(X, y)                                # método: treinar
modelo.predict(X)                               # método: prever



