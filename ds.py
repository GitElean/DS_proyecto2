import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from tensorflow.keras.models import Sequential
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from tensorflow.keras.layers import Input, Dense, Concatenate
from tensorflow.keras.models import Model

# Cargar datos
df = pd.read_csv('datos_bundesliga.csv')

# Separar características y etiquetas
X = df.drop('Pases', axis=1)
y = df['Pases']




