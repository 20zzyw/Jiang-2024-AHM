# Python: 3.9.18
# pickle: 4.0

import pickle

# Please gather:
# (1)this script, 
# (2)model 'Jiang_et_al_RFmodel_fitted.pkl',
# (3)test data (or your own data) 
# into a same folder.
# Then change current work dictionary to this folder using "cd [path]" in your command-line.
# Finally run this script using command "python prediction_with_sample_data.py"
# You should see output like this:
# Predicted p: [[0.34473914 0.65526086]]
# Predicted class: [1]
# Predicted p: [[0.62553872 0.37446128]]
# Predicted class: [0]
# Predicted p: [[0.09459047 0.90540953]]
# Predicted class: [1]
# Predicted p: [[0.08367491 0.91632509]]
# Predicted class: [1]
# Predicted p: [[0.35291522 0.64708478]]
# Predicted class: [1]

# Load fitted model (type: RandomForestClassifier, @sklean) using pickle
model_filename = 'Jiang_et_al_RFmodel_fitted.pkl'
with open(model_filename, 'rb') as f:
    rf_model = pickle.load(f)

# Load sample data (type: ndarray, @numpy)or your own
data_filename = 'sample_data_hcc.dat'
with open(data_filename, 'rb') as f:
    data = pickle.load(f)

# Make predicion
for i in range(data.shape[0]):
    print('Predicted p: {}'.format(rf_model.predict_proba(data[i].reshape(1, -1))))
    print('Predicted class: {}'.format(rf_model.predict(data[i].reshape(1, -1))))