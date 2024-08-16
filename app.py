from flask import Flask, request, render_template
import pickle
import numpy as np


pickle_in = open('Mushroom.pkl', 'rb')
model = pickle.load(pickle_in)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Extract feature values from the form
        cap_shape = float(request.form['cap_shape'])
        cap_surface = float(request.form['cap_surface'])
        cap_color = float(request.form['cap_color'])
        bruises = float(request.form['bruises'])
        odor = float(request.form['odor'])
        gill_attachment = float(request.form['gill_attachment'])
        gill_spacing = float(request.form['gill_spacing'])
        gill_size = float(request.form['gill_size'])
        gill_color = float(request.form['gill_color'])
        stalk_shape = float(request.form['stalk_shape'])
        stalk_root = float(request.form['stalk_root'])
        stalk_surface_above_ring = float(request.form['stalk_surface_above_ring'])
        stalk_surface_below_ring = float(request.form['stalk_surface_below_ring'])
        stalk_color_above_ring = float(request.form['stalk_color_above_ring'])
        stalk_color_below_ring = float(request.form['stalk_color_below_ring'])
        veil_type = float(request.form['veil_type'])
        veil_color = float(request.form['veil_color'])
        ring_number = float(request.form['ring_number'])
        ring_type = float(request.form['ring_type'])
        spore_print_color = float(request.form['spore_print_color'])
        population = float(request.form['population'])
        habitat = float(request.form['habitat'])

        
        features = np.array([[cap_shape, cap_surface, cap_color, bruises, odor, gill_attachment,
                              gill_spacing, gill_size, gill_color, stalk_shape, stalk_root,
                              stalk_surface_above_ring, stalk_surface_below_ring, stalk_color_above_ring,
                              stalk_color_below_ring, veil_type, veil_color, ring_number, ring_type,
                              spore_print_color, population, habitat]])

       
        prediction = model.predict(features)

        if prediction == 0:
            result = "Edible"
        else:
            result = "Poisonous"

        return render_template('index.html', prediction_text=f'The mushroom is {result}')

if __name__ == "__main__":
    app.run(debug=True)
