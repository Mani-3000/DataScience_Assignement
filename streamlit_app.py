{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1a3ada06-a29c-48a1-995e-f03c7fdf21a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-04-05 12:16:07.924 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\ProgramData\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "import joblib\n",
    "\n",
    "# Load the trained model\n",
    "model = joblib.load(\"logistic_model.pkl\")\n",
    "\n",
    "st.title(\"🚢 Titanic Survival Prediction App\")\n",
    "st.write(\"Enter passenger details to predict survival probability.\")\n",
    "\n",
    "# User Inputs\n",
    "pclass = st.selectbox(\"Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)\", [1, 2, 3])\n",
    "sex = st.selectbox(\"Sex\", [\"male\", \"female\"])\n",
    "age = st.slider(\"Age\", 0, 80, 25)\n",
    "sibsp = st.number_input(\"Number of Siblings/Spouses Aboard\", min_value=0, step=1)\n",
    "parch = st.number_input(\"Number of Parents/Children Aboard\", min_value=0, step=1)\n",
    "fare = st.number_input(\"Fare Paid\", min_value=0.0, step=1.0)\n",
    "embarked = st.selectbox(\"Port of Embarkation\", [\"S\", \"C\", \"Q\"])\n",
    "\n",
    "# Encode inputs (must match training)\n",
    "sex_encoded = 0 if sex == \"female\" else 1\n",
    "embarked_dict = {\"S\": 2, \"C\": 0, \"Q\": 1}\n",
    "embarked_encoded = embarked_dict[embarked]\n",
    "\n",
    "# Format input\n",
    "input_data = np.array([[pclass, sex_encoded, age, sibsp, parch, fare, embarked_encoded]])\n",
    "\n",
    "if st.button(\"Predict\"):\n",
    "    prediction = model.predict(input_data)[0]\n",
    "    prob = model.predict_proba(input_data)[0][1]\n",
    "\n",
    "    if prediction == 1:\n",
    "        st.success(f\"🎉 The passenger is likely to survive! (Probability: {prob:.2f})\")\n",
    "    else:\n",
    "        st.error(f\"❌ The passenger is unlikely to survive. (Probability: {prob:.2f})\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "c7002329-a4a8-4c82-9958-195b7edb08ba",
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
