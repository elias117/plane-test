import os
import pandas as pd
from flask import Flask, request, abort, jsonify
import numpy as np

df = pd.read_csv("./Aircraft Database - Sheet1.csv")
df.dropna(how="all", inplace=True)
cols = df.columns
df[cols] = df[cols].replace({np.nan: "No Value"})


def check_tag_match(tags_data, tags_user_input):
    tags_data = tags_data.split(',')
    tags_data_set = set(tags_data)
    tags_user_input_set = set(tags_user_input)
    tag_over_laps_set = tags_user_input_set & tags_data_set
    return len(tag_over_laps_set) > 0


app = Flask(__name__)
app.config.from_object("config")


@app.route("/api/v1/search", methods=["POST"])
def get_planes_by_model():
    data = request.get_json()
    model_id = data.get("modelId", '')
    weight_class = data.get("weightClass", '')
    tags = data.get("tags", [])

    if model_id == '' and weight_class == '' and tags == []:
        return jsonify({
            'planes': list(df.T.to_dict().values())
        }), 200
    found_results = df[df['Model'].str.contains(model_id, case=False)]
    found_results = found_results[found_results["ATCT Weight Class"].str.contains(
        weight_class, case=False)]
    if tags:
        found_results['Tag Match'] = found_results['Tags'].apply(
            lambda x: check_tag_match(x, tags))
        found_results = found_results[found_results['Tag Match']]
    formatted_results = list(found_results.T.to_dict().values())
    return jsonify({
        "planes": formatted_results
    }), 200


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="localhost", port=port)
