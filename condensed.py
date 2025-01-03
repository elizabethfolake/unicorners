{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e93a1b5c-2b71-447f-a2c0-2af2aca9c3ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "import pickle\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import accuracy_score\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "df = pd.read_csv('train.csv')\n",
    "\n",
    "def get_title(name):\n",
    "    if '.' in name:\n",
    "        return name.split(',')[1].split('.')[0].strip()\n",
    "    else:\n",
    "        'Not found'\n",
    "\n",
    "title = set([x for x in df['Name'].map(lambda x:get_title(x) )])\n",
    "print(title)\n",
    "\n",
    "def shorter_titles(x):\n",
    "    title = x['Title']\n",
    "    if title in ['Capt', 'Col', 'Major']:\n",
    "        return 'Officer'\n",
    "    elif title in ['Jonkheer', 'Don','the Countess','Don','Lady','Sir']:\n",
    "        return 'Royalty'\n",
    "    elif title == 'Mme':\n",
    "        return 'Mrs'\n",
    "    elif title in ['Miss', 'Ms']:\n",
    "        return 'Miss'\n",
    "    else:\n",
    "        return title\n",
    "\n",
    "df['Title'] = df['Name'].map(lambda x:get_title(x))\n",
    "df['Title'] = df.apply(shorter_titles, axis=1)\n",
    "df.fillna({'Age': 22}, inplace=True)\n",
    "df.fillna({'Embarked': 'S'}, inplace=True)\n",
    "df.drop({'Name', 'Ticket', 'Cabin'}, inplace=True, axis=1)\n",
    "df['Sex'].replace(('male', 'female'), (0,1), inplace=True)\n",
    "df.Embarked.replace(('C','S', 'Q'), (0,1,2), inplace=True)\n",
    "df.Title.replace(('Miss', 'Mlle', 'Mr', 'Mrs', 'Master', 'Officer', 'Dr','Rev', 'Royalty'), (0,1,2,3,4,5,6,7,8), inplace=True)\n",
    "\n",
    "y = df['Survived']\n",
    "x = df.drop(['Survived', 'PassengerId'], axis=1)\n",
    "x_train, x_val, y_train, y_val = train_test_split(predictors,target, test_size=0.22, random_state=0)\n",
    "\n",
    "randomforest = RandomForestClassifier()\n",
    "randomforest.fit(x_train, y_train)\n",
    "y_pred=randomforest.predict(x_val)\n",
    "\n",
    "print(acc_randomforest)\n",
    "filename ='titanic_model.sav'\n",
    "pickle.dump(randomforest, open(filename, 'wb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0b171a30-71e0-4e12-9f8f-e7f3cbd61a90",
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
   "version": "3.13.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
