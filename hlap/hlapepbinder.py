import pickle
from sklearn.ensemble import RandomForestClassifier

"""HLAPepBinder"""

# input example
# inp_list = [[41841.86, 70.500, 42170.00, 0.000182, 197983.956993, 174968.552921, 50000.000000, 41375.00, 0.11]]

# load
with open('hlap/HLAPepBinder_model.pkl', 'rb') as f:
    clf = pickle.load(f)


def predict(hla_input):
    return [int(d) for d in clf.predict([hla_input])]
