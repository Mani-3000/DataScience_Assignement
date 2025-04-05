{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "64e74a67-7129-40e5-aba1-33857ed33945",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-04-05 08:56:51.728 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\ProgramData\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "# streamlit_app.py\n",
    "\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import joblib\n",
    "\n",
    "st.set_page_config(page_title=\"Titanic Survival Prediction\", layout=\"centered\")\n",
    "st.title(\"🚢 Titanic Survival Prediction App\")\n",
    "st.markdown(\"Enter passenger details to predict survival.\")\n",
    "\n",
    "# Load trained model\n",
    "model = joblib.load(\"logistic_model.pkl\")\n",
    "\n",
    "# User input\n",
    "pclass = st.selectbox(\"Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)\", [1, 2, 3])\n",
    "sex = st.selectbox(\"Sex\", [\"male\", \"female\"])\n",
    "age = st.slider(\"Age\", 0, 100, 30)\n",
    "sibsp = st.number_input(\"Number of Siblings/Spouses Aboard\", 0, 10, 0)\n",
    "parch = st.number_input(\"Number of Parents/Children Aboard\", 0, 10, 0)\n",
    "fare = st.slider(\"Fare\", 0.0, 600.0, 32.0)\n",
    "embarked = st.selectbox(\"Port of Embarkation\", [\"C\", \"Q\", \"S\"])\n",
    "\n",
    "# Encode inputs\n",
    "sex_encoded = 1 if sex == \"male\" else 0\n",
    "embarked_map = {\"C\": 0, \"Q\": 1, \"S\": 2}\n",
    "embarked_encoded = embarked_map[embarked]\n",
    "\n",
    "# Create input dataframe\n",
    "input_data = pd.DataFrame({\n",
    "    \"Pclass\": [pclass],\n",
    "    \"Sex\": [sex_encoded],\n",
    "    \"Age\": [age],\n",
    "    \"SibSp\": [sibsp],\n",
    "    \"Parch\": [parch],\n",
    "    \"Fare\": [fare],\n",
    "    \"Embarked\": [embarked_encoded],\n",
    "})\n",
    "\n",
    "# Predict\n",
    "if st.button(\"Predict Survival\"):\n",
    "    prediction = model.predict(input_data)[0]\n",
    "    prob = model.predict_proba(input_data)[0][1]\n",
    "    if prediction == 1:\n",
    "        st.success(f\"🎉 The passenger is likely to SURVIVE (Probability: {prob:.2f})\")\n",
    "    else:\n",
    "        st.error(f\"💀 The passenger is likely to NOT survive (Probability: {prob:.2f})\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fc0ca0d6-f168-4265-b6ba-ad3c3d486a69",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
