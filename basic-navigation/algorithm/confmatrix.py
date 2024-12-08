import pandas as pd
from shared import df
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import accuracy_score, confusion_matrix

#####FIXME: file is hardcoded. make it possible for automated algorithms for any new similar file 

encoder = OneHotEncoder(sparse_output=False)
categorical_columns = ['Direction', 'Shot Type', 'Stroke']
categorical_data = encoder.fit_transform(df[categorical_columns])

#add one hot encoded columns to dataframe
categorical_df = pd.DataFrame(categorical_data, columns=encoder.get_feature_names_out(categorical_columns))
df = pd.concat([df, categorical_df], axis=1)

#drop old and show new columns
df = df.drop(columns=categorical_columns)
df = df.drop(columns=['Player Name', 'Video Time','Rally #', 'Shot # of Rally','Point #'])

#define the binary target variable
df['FAULT_BINARY'] = df['Context'].apply(lambda x: 1 if x in ['FAULT', 'DOUBLE_FAULT'] else 0)

df = df.drop(columns=['Context'])

from sklearn.preprocessing import LabelEncoder, StandardScaler

imputer = SimpleImputer(strategy='mean')
le = LabelEncoder()
#split data
X = df.drop(columns=['Outcome', 'FAULT_BINARY'])
X_imputed = imputer.fit_transform(X)

y = df['FAULT_BINARY']
y = le.fit_transform(y)


X_train, X_test, y_train, y_test = train_test_split(X_imputed, y,stratify=y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

log_reg_model = LogisticRegression()
log_reg_model.fit(X_train, y_train)

# make predictions on the test set
y_pred = log_reg_model.predict(X_test)

# evaluate
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# SVR model
svr_model = SVR (kernel ='linear')
svr_model.fit(X_train,y_train)

y_pred_svr = svr_model.predict(X_test)
SVR_mse = mean_squared_error(y_test, y_pred_svr)
SVR_mae = mean_absolute_error(y_test, y_pred_svr)
SVR_r2 = r2_score(y_test, y_pred_svr)

#RFR
rf_model = RandomForestRegressor(n_estimators=100, random_state= 42)
rf_model.fit(X_train,y_train)
y_pred_rf = rf_model.predict(X_test)

RFR_mse = mean_squared_error(y_test, y_pred_rf)
RFR_mae = mean_absolute_error(y_test, y_pred_rf)
RFR_r2 = r2_score(y_test, y_pred_rf)






