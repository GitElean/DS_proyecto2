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

df = pd.read_csv('datos_bundesliga.csv')

X = df.drop('Pases', axis=1)
y = df['Pases']

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Características numéricas
numeric_features = ['Minuto', 'Segundo']
X_train_numeric = X_train[numeric_features]
X_test_numeric = X_test[numeric_features]

# Escalar características numéricas
scaler = StandardScaler()
X_train_numeric = scaler.fit_transform(X_train_numeric)
X_test_numeric = scaler.transform(X_test_numeric)

# Características categóricas
categorical_features = ['Equipo', 'Posicion_Inicio', 'Fase_del_Partido']
X_train_categorical = X_train[categorical_features]
X_test_categorical = X_test[categorical_features]

X_train_categorical = pd.get_dummies(X_train_categorical)
X_test_categorical = pd.get_dummies(X_test_categorical)

# Ver que las columnas categoricas en los conjuntos de training y test sean las mismas
X_train_categorical, X_test_categorical = X_train_categorical.align(X_test_categorical, join='left', axis=1, fill_value=0)
input_numeric = Input(shape=(X_train_numeric.shape[1],))

# Entradas categóricas
input_categorical = Input(shape=(X_train_categorical.shape[1],))
concatenated = Concatenate()([input_numeric, input_categorical])