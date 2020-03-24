'''
The kaggle page for this data set had a task to predict cancellations.
I am thinking of using logistic regression due to the binary nature of a cancellation.
'''
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix


def log_reg(df):
    # Countries has some missing values
    #print(df.isnull().sum())

    df.fillna(df.mode().iloc[0], inplace=True)
    # Good to go
    #print(df.isnull().sum())

    # Remove columns I don't need
    df.drop(['hotel',
             'reservation_status_date',
             'reservation_status',
             'adr'], axis=1, inplace=True)

    col_transformer = make_column_transformer((OneHotEncoder(), ['meal',
                                                    'distribution_channel',
                                                    'country',
                                                    'deposit_type',
                                                    'previous_cancellations',
                                                    'previous_bookings_not_canceled',
                                                    'arrival_date_month',
                                                    'market_segment',
                                                    'deposit_type',
                                                    'previous_bookings_not_canceled',
                                                    'previous_cancellations',
                                                    'customer_type',
                                                    'reserved_room_type',
                                                    'is_repeated_guest',
                                                    'assigned_room_type']), remainder='passthrough')

    # Separate is_canceled from rest of columns since that is what I'm predicting

    x = df.iloc[:, 1:]
    y = df.iloc[:, 0]

    X = col_transformer.fit_transform(x).toarray()

    x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)

    sc = StandardScaler()

    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)

    log_model = LogisticRegression()

    log_model.fit(x_train,y_train)

    y_pred = log_model.predict(x_test)

    print(confusion_matrix(y_test, y_pred))

    print(f'Prediction score: {log_model.score(x_test, y_test)*100:.2f}%')


