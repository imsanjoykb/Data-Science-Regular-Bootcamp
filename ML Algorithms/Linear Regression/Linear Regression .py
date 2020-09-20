{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Author : Sanjoy Biswas\n",
    "#### Topic : Linear Regression Tutorial With Project Solving\n",
    "#### Email : sanjoy.eee32@gmail.com"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Linear regression is one of the easiest and most popular Machine Learning algorithms. It is a statistical method that is used for predictive analysis. Linear regression makes predictions for continuous/real or numeric variables such as sales, salary, age, product price, etc.\n",
    "\n",
    "Linear regression algorithm shows a linear relationship between a dependent (y) and one or more independent (y) variables, hence called as linear regression. Since linear regression shows the linear relationship, which means it finds how the value of the dependent variable is changing according to the value of the independent variable."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Import Libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "b22jcm28JSUv"
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from sklearn import linear_model\n",
    "from word2number import w2n\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Import Dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 204
    },
    "colab_type": "code",
    "id": "Gz6jTmWzJuzO",
    "outputId": "1ac75a95-b71a-4bc4-9e9e-b0447709f981"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>experience</th>\n",
       "      <th>test_score(out of 10)</th>\n",
       "      <th>interview_score(out of 10)</th>\n",
       "      <th>salary($)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>8.0</td>\n",
       "      <td>9</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>8.0</td>\n",
       "      <td>6</td>\n",
       "      <td>45000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>five</td>\n",
       "      <td>6.0</td>\n",
       "      <td>7</td>\n",
       "      <td>60000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>two</td>\n",
       "      <td>10.0</td>\n",
       "      <td>10</td>\n",
       "      <td>65000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>seven</td>\n",
       "      <td>9.0</td>\n",
       "      <td>6</td>\n",
       "      <td>70000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  experience  test_score(out of 10)  interview_score(out of 10)  salary($)\n",
       "0        NaN                    8.0                           9      50000\n",
       "1        NaN                    8.0                           6      45000\n",
       "2       five                    6.0                           7      60000\n",
       "3        two                   10.0                          10      65000\n",
       "4      seven                    9.0                           6      70000"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv('F:\\ML Algorithms By Me\\Linear Regression\\hiring.csv')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Preprocessing Datasets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "SWolBulhKdpb"
   },
   "outputs": [],
   "source": [
    "df.experience = df.experience.fillna('Zero')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 297
    },
    "colab_type": "code",
    "id": "cBIeUj5IKqBT",
    "outputId": "9baed6e3-ec38-4c37-9bc9-c3964dd62943"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>experience</th>\n",
       "      <th>test_score(out of 10)</th>\n",
       "      <th>interview_score(out of 10)</th>\n",
       "      <th>salary($)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>Zero</td>\n",
       "      <td>8.0</td>\n",
       "      <td>9</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>Zero</td>\n",
       "      <td>8.0</td>\n",
       "      <td>6</td>\n",
       "      <td>45000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>five</td>\n",
       "      <td>6.0</td>\n",
       "      <td>7</td>\n",
       "      <td>60000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>two</td>\n",
       "      <td>10.0</td>\n",
       "      <td>10</td>\n",
       "      <td>65000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>seven</td>\n",
       "      <td>9.0</td>\n",
       "      <td>6</td>\n",
       "      <td>70000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5</td>\n",
       "      <td>three</td>\n",
       "      <td>7.0</td>\n",
       "      <td>10</td>\n",
       "      <td>62000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>6</td>\n",
       "      <td>ten</td>\n",
       "      <td>NaN</td>\n",
       "      <td>7</td>\n",
       "      <td>72000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>7</td>\n",
       "      <td>eleven</td>\n",
       "      <td>7.0</td>\n",
       "      <td>8</td>\n",
       "      <td>80000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  experience  test_score(out of 10)  interview_score(out of 10)  salary($)\n",
       "0       Zero                    8.0                           9      50000\n",
       "1       Zero                    8.0                           6      45000\n",
       "2       five                    6.0                           7      60000\n",
       "3        two                   10.0                          10      65000\n",
       "4      seven                    9.0                           6      70000\n",
       "5      three                    7.0                          10      62000\n",
       "6        ten                    NaN                           7      72000\n",
       "7     eleven                    7.0                           8      80000"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "KwbkaW6mKw2t"
   },
   "outputs": [],
   "source": [
    "### Apply word_to_num\n",
    "df.experience = df.experience.apply(w2n.word_to_num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 297
    },
    "colab_type": "code",
    "id": "ozL0gUIpLFfV",
    "outputId": "0449cf7f-a37f-4fe2-c190-dc49652e1702"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>experience</th>\n",
       "      <th>test_score(out of 10)</th>\n",
       "      <th>interview_score(out of 10)</th>\n",
       "      <th>salary($)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>8.0</td>\n",
       "      <td>9</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>8.0</td>\n",
       "      <td>6</td>\n",
       "      <td>45000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>6.0</td>\n",
       "      <td>7</td>\n",
       "      <td>60000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>10.0</td>\n",
       "      <td>10</td>\n",
       "      <td>65000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>7</td>\n",
       "      <td>9.0</td>\n",
       "      <td>6</td>\n",
       "      <td>70000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5</td>\n",
       "      <td>3</td>\n",
       "      <td>7.0</td>\n",
       "      <td>10</td>\n",
       "      <td>62000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>6</td>\n",
       "      <td>10</td>\n",
       "      <td>NaN</td>\n",
       "      <td>7</td>\n",
       "      <td>72000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>7</td>\n",
       "      <td>11</td>\n",
       "      <td>7.0</td>\n",
       "      <td>8</td>\n",
       "      <td>80000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   experience  test_score(out of 10)  interview_score(out of 10)  salary($)\n",
       "0           0                    8.0                           9      50000\n",
       "1           0                    8.0                           6      45000\n",
       "2           5                    6.0                           7      60000\n",
       "3           2                   10.0                          10      65000\n",
       "4           7                    9.0                           6      70000\n",
       "5           3                    7.0                          10      62000\n",
       "6          10                    NaN                           7      72000\n",
       "7          11                    7.0                           8      80000"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 34
    },
    "colab_type": "code",
    "id": "QnGiCofdOo0G",
    "outputId": "c6831e1e-6660-43a5-b5dd-b9f8327532ee"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import math\n",
    "median_test_score = math.floor(df['test_score(out of 10)'].mean())\n",
    "median_test_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 34
    },
    "colab_type": "code",
    "id": "tZTarYSFO7h2",
    "outputId": "529325ec-718f-4d5b-eb0b-545a0c889aba"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7.857142857142857"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dff = df['test_score(out of 10)'].mean()\n",
    "dff"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "4lbEXfoVPLZQ"
   },
   "outputs": [],
   "source": [
    "df['test_score(out of 10)'] = df['test_score(out of 10)'].fillna(dff)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 297
    },
    "colab_type": "code",
    "id": "4-u6J-GyPWm3",
    "outputId": "96d8bc1c-22aa-4bf4-a371-2cea9c1aef2b"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>experience</th>\n",
       "      <th>test_score(out of 10)</th>\n",
       "      <th>interview_score(out of 10)</th>\n",
       "      <th>salary($)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>9</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>6</td>\n",
       "      <td>45000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>7</td>\n",
       "      <td>60000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>10</td>\n",
       "      <td>65000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>7</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>6</td>\n",
       "      <td>70000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5</td>\n",
       "      <td>3</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>10</td>\n",
       "      <td>62000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>6</td>\n",
       "      <td>10</td>\n",
       "      <td>7.857143</td>\n",
       "      <td>7</td>\n",
       "      <td>72000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>7</td>\n",
       "      <td>11</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>8</td>\n",
       "      <td>80000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   experience  test_score(out of 10)  interview_score(out of 10)  salary($)\n",
       "0           0               8.000000                           9      50000\n",
       "1           0               8.000000                           6      45000\n",
       "2           5               6.000000                           7      60000\n",
       "3           2              10.000000                          10      65000\n",
       "4           7               9.000000                           6      70000\n",
       "5           3               7.000000                          10      62000\n",
       "6          10               7.857143                           7      72000\n",
       "7          11               7.000000                           8      80000"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 68
    },
    "colab_type": "code",
    "id": "BmVqQm2FMtTv",
    "outputId": "f4ce3e5b-b1c0-4d70-a7ac-87d8c89c3c95"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['experience', 'test_score(out of 10)', 'interview_score(out of 10)',\n",
       "       'salary($)'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "### Show Columns Name\n",
    "df.columns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Features Selection"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "tdndrJAJLPtj"
   },
   "outputs": [],
   "source": [
    "predictors = ['experience', 'test_score(out of 10)', 'interview_score(out of 10)']\n",
    "x = df[predictors]\n",
    "y = df['salary($)']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Split Train and test datasets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "-LZz-gtWM2ca"
   },
   "outputs": [],
   "source": [
    "x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 34
    },
    "colab_type": "code",
    "id": "oAd_31AXNzDY",
    "outputId": "d7191e3c-5b09-420f-acb9-a34ebd32cd74"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((6, 3), (2, 3))"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_train.shape,x_test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 34
    },
    "colab_type": "code",
    "id": "BlIPqPPYONVu",
    "outputId": "7bf6a04a-1d29-4553-be82-da056ffd2d59"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((6,), (2,))"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_train.shape,y_test.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Apply Linear Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "-ZTCNVw4NesU"
   },
   "outputs": [],
   "source": [
    "reg = LinearRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "942k5qaeNsp1"
   },
   "outputs": [],
   "source": [
    "model = reg.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 34
    },
    "colab_type": "code",
    "id": "TZW8g8MfOc0U",
    "outputId": "f63b15a2-1739-4eed-e060-8952943e4db4"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([58355.74491311])"
      ]
     },
     "execution_count": 40,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.predict([[5,6,7]])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Accuracy Score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "LALdSNQdQSkV"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.945171325224806"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.score(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9287916364000984"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.score(x_test,y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "name": "Untitled7.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
