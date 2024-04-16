# Jiang-2024-AHM
Model, pipeline, and sample data for Jiang et al 2024

Most of primary steps in our AI pipeline is provided in 'pipeline.ipynb'

To try our model, please gather following items into a same folder.  

(1)python script 'prediction_with_sample_data.py', 

(2)model 'Jiang_et_al_RFmodel_fitted.pkl',

(3)test data 'sample_data_hcc.dat' or 'sample_data_healthy.dat' (or your own data) 


Then change current work dictionary to this folder using "cd [path]" in your command-line.
Finally run this script using command "python prediction_with_sample_data.py"

You should see output like this:
Predicted p: [[0.34473914 0.65526086]]
Predicted class: [1]
Predicted p: [[0.62553872 0.37446128]]
Predicted class: [0]
Predicted p: [[0.09459047 0.90540953]]
Predicted class: [1]
Predicted p: [[0.08367491 0.91632509]]
Predicted class: [1]
Predicted p: [[0.35291522 0.64708478]]
Predicted class: [1]
