{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
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
       "      <th>EST</th>\n",
       "      <th>Temperature</th>\n",
       "      <th>DewPoint</th>\n",
       "      <th>Humidity</th>\n",
       "      <th>Sea Level PressureIn</th>\n",
       "      <th>VisibilityMiles</th>\n",
       "      <th>WindSpeedMPH</th>\n",
       "      <th>PrecipitationIn</th>\n",
       "      <th>CloudCover</th>\n",
       "      <th>Events</th>\n",
       "      <th>WindDirDegrees</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1/1/2016</td>\n",
       "      <td>38</td>\n",
       "      <td>23</td>\n",
       "      <td>52</td>\n",
       "      <td>30.03</td>\n",
       "      <td>10</td>\n",
       "      <td>8.0</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>NaN</td>\n",
       "      <td>281</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1/2/2016</td>\n",
       "      <td>36</td>\n",
       "      <td>18</td>\n",
       "      <td>46</td>\n",
       "      <td>30.02</td>\n",
       "      <td>10</td>\n",
       "      <td>7.0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>NaN</td>\n",
       "      <td>275</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1/3/2016</td>\n",
       "      <td>40</td>\n",
       "      <td>21</td>\n",
       "      <td>47</td>\n",
       "      <td>29.86</td>\n",
       "      <td>10</td>\n",
       "      <td>8.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>277</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1/4/2016</td>\n",
       "      <td>25</td>\n",
       "      <td>9</td>\n",
       "      <td>44</td>\n",
       "      <td>30.05</td>\n",
       "      <td>10</td>\n",
       "      <td>9.0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>NaN</td>\n",
       "      <td>345</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1/5/2016</td>\n",
       "      <td>20</td>\n",
       "      <td>-3</td>\n",
       "      <td>41</td>\n",
       "      <td>30.57</td>\n",
       "      <td>10</td>\n",
       "      <td>5.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1/6/2016</td>\n",
       "      <td>33</td>\n",
       "      <td>4</td>\n",
       "      <td>35</td>\n",
       "      <td>30.50</td>\n",
       "      <td>10</td>\n",
       "      <td>4.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>259</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>1/7/2016</td>\n",
       "      <td>39</td>\n",
       "      <td>11</td>\n",
       "      <td>33</td>\n",
       "      <td>30.28</td>\n",
       "      <td>10</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>NaN</td>\n",
       "      <td>293</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>1/8/2016</td>\n",
       "      <td>39</td>\n",
       "      <td>29</td>\n",
       "      <td>64</td>\n",
       "      <td>30.20</td>\n",
       "      <td>10</td>\n",
       "      <td>4.0</td>\n",
       "      <td>0</td>\n",
       "      <td>8</td>\n",
       "      <td>NaN</td>\n",
       "      <td>79</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>1/9/2016</td>\n",
       "      <td>44</td>\n",
       "      <td>38</td>\n",
       "      <td>77</td>\n",
       "      <td>30.16</td>\n",
       "      <td>9</td>\n",
       "      <td>8.0</td>\n",
       "      <td>T</td>\n",
       "      <td>8</td>\n",
       "      <td>Rain</td>\n",
       "      <td>76</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>1/10/2016</td>\n",
       "      <td>50</td>\n",
       "      <td>46</td>\n",
       "      <td>71</td>\n",
       "      <td>29.59</td>\n",
       "      <td>4</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.8</td>\n",
       "      <td>7</td>\n",
       "      <td>Rain</td>\n",
       "      <td>109</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>1/11/2016</td>\n",
       "      <td>33</td>\n",
       "      <td>8</td>\n",
       "      <td>37</td>\n",
       "      <td>29.92</td>\n",
       "      <td>10</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>289</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>1/12/2016</td>\n",
       "      <td>35</td>\n",
       "      <td>15</td>\n",
       "      <td>53</td>\n",
       "      <td>29.85</td>\n",
       "      <td>10</td>\n",
       "      <td>6.0</td>\n",
       "      <td>T</td>\n",
       "      <td>4</td>\n",
       "      <td>NaN</td>\n",
       "      <td>235</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>1/13/2016</td>\n",
       "      <td>26</td>\n",
       "      <td>4</td>\n",
       "      <td>42</td>\n",
       "      <td>29.94</td>\n",
       "      <td>10</td>\n",
       "      <td>10.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>284</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>1/14/2016</td>\n",
       "      <td>30</td>\n",
       "      <td>12</td>\n",
       "      <td>47</td>\n",
       "      <td>29.95</td>\n",
       "      <td>10</td>\n",
       "      <td>5.0</td>\n",
       "      <td>T</td>\n",
       "      <td>7</td>\n",
       "      <td>NaN</td>\n",
       "      <td>266</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>1/15/2016</td>\n",
       "      <td>43</td>\n",
       "      <td>31</td>\n",
       "      <td>62</td>\n",
       "      <td>29.82</td>\n",
       "      <td>9</td>\n",
       "      <td>5.0</td>\n",
       "      <td>T</td>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "      <td>101</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>1/16/2016</td>\n",
       "      <td>47</td>\n",
       "      <td>37</td>\n",
       "      <td>70</td>\n",
       "      <td>29.52</td>\n",
       "      <td>8</td>\n",
       "      <td>7.0</td>\n",
       "      <td>0.24</td>\n",
       "      <td>7</td>\n",
       "      <td>Rain</td>\n",
       "      <td>340</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>1/17/2016</td>\n",
       "      <td>36</td>\n",
       "      <td>23</td>\n",
       "      <td>66</td>\n",
       "      <td>29.78</td>\n",
       "      <td>8</td>\n",
       "      <td>6.0</td>\n",
       "      <td>0.05</td>\n",
       "      <td>6</td>\n",
       "      <td>Fog-Snow</td>\n",
       "      <td>345</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>1/18/2016</td>\n",
       "      <td>25</td>\n",
       "      <td>6</td>\n",
       "      <td>53</td>\n",
       "      <td>29.83</td>\n",
       "      <td>9</td>\n",
       "      <td>12.0</td>\n",
       "      <td>T</td>\n",
       "      <td>2</td>\n",
       "      <td>Snow</td>\n",
       "      <td>293</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>1/19/2016</td>\n",
       "      <td>22</td>\n",
       "      <td>3</td>\n",
       "      <td>42</td>\n",
       "      <td>30.03</td>\n",
       "      <td>10</td>\n",
       "      <td>11.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>293</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>1/20/2016</td>\n",
       "      <td>32</td>\n",
       "      <td>15</td>\n",
       "      <td>49</td>\n",
       "      <td>30.13</td>\n",
       "      <td>10</td>\n",
       "      <td>6.0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "      <td>302</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>1/21/2016</td>\n",
       "      <td>31</td>\n",
       "      <td>11</td>\n",
       "      <td>45</td>\n",
       "      <td>30.15</td>\n",
       "      <td>10</td>\n",
       "      <td>6.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>312</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>1/22/2016</td>\n",
       "      <td>26</td>\n",
       "      <td>6</td>\n",
       "      <td>41</td>\n",
       "      <td>30.21</td>\n",
       "      <td>9</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.01</td>\n",
       "      <td>3</td>\n",
       "      <td>Snow</td>\n",
       "      <td>34</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>1/23/2016</td>\n",
       "      <td>26</td>\n",
       "      <td>21</td>\n",
       "      <td>78</td>\n",
       "      <td>29.77</td>\n",
       "      <td>1</td>\n",
       "      <td>16.0</td>\n",
       "      <td>2.31</td>\n",
       "      <td>8</td>\n",
       "      <td>Fog-Snow</td>\n",
       "      <td>42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>1/24/2016</td>\n",
       "      <td>28</td>\n",
       "      <td>11</td>\n",
       "      <td>53</td>\n",
       "      <td>29.92</td>\n",
       "      <td>8</td>\n",
       "      <td>6.0</td>\n",
       "      <td>T</td>\n",
       "      <td>3</td>\n",
       "      <td>Snow</td>\n",
       "      <td>327</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>1/25/2016</td>\n",
       "      <td>34</td>\n",
       "      <td>18</td>\n",
       "      <td>54</td>\n",
       "      <td>30.25</td>\n",
       "      <td>10</td>\n",
       "      <td>3.0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "      <td>286</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>1/26/2016</td>\n",
       "      <td>43</td>\n",
       "      <td>29</td>\n",
       "      <td>56</td>\n",
       "      <td>30.03</td>\n",
       "      <td>10</td>\n",
       "      <td>7.0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "      <td>244</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>1/27/2016</td>\n",
       "      <td>41</td>\n",
       "      <td>22</td>\n",
       "      <td>45</td>\n",
       "      <td>30.03</td>\n",
       "      <td>10</td>\n",
       "      <td>7.0</td>\n",
       "      <td>T</td>\n",
       "      <td>3</td>\n",
       "      <td>Rain</td>\n",
       "      <td>311</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>1/28/2016</td>\n",
       "      <td>37</td>\n",
       "      <td>20</td>\n",
       "      <td>51</td>\n",
       "      <td>29.90</td>\n",
       "      <td>10</td>\n",
       "      <td>5.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>234</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>1/29/2016</td>\n",
       "      <td>36</td>\n",
       "      <td>21</td>\n",
       "      <td>50</td>\n",
       "      <td>29.58</td>\n",
       "      <td>10</td>\n",
       "      <td>8.0</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>NaN</td>\n",
       "      <td>298</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>1/30/2016</td>\n",
       "      <td>34</td>\n",
       "      <td>16</td>\n",
       "      <td>46</td>\n",
       "      <td>30.01</td>\n",
       "      <td>10</td>\n",
       "      <td>7.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>257</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>1/31/2016</td>\n",
       "      <td>46</td>\n",
       "      <td>28</td>\n",
       "      <td>52</td>\n",
       "      <td>29.90</td>\n",
       "      <td>10</td>\n",
       "      <td>5.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>241</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          EST  Temperature  DewPoint  Humidity  Sea Level PressureIn  \\\n",
       "0    1/1/2016           38        23        52                 30.03   \n",
       "1    1/2/2016           36        18        46                 30.02   \n",
       "2    1/3/2016           40        21        47                 29.86   \n",
       "3    1/4/2016           25         9        44                 30.05   \n",
       "4    1/5/2016           20        -3        41                 30.57   \n",
       "5    1/6/2016           33         4        35                 30.50   \n",
       "6    1/7/2016           39        11        33                 30.28   \n",
       "7    1/8/2016           39        29        64                 30.20   \n",
       "8    1/9/2016           44        38        77                 30.16   \n",
       "9   1/10/2016           50        46        71                 29.59   \n",
       "10  1/11/2016           33         8        37                 29.92   \n",
       "11  1/12/2016           35        15        53                 29.85   \n",
       "12  1/13/2016           26         4        42                 29.94   \n",
       "13  1/14/2016           30        12        47                 29.95   \n",
       "14  1/15/2016           43        31        62                 29.82   \n",
       "15  1/16/2016           47        37        70                 29.52   \n",
       "16  1/17/2016           36        23        66                 29.78   \n",
       "17  1/18/2016           25         6        53                 29.83   \n",
       "18  1/19/2016           22         3        42                 30.03   \n",
       "19  1/20/2016           32        15        49                 30.13   \n",
       "20  1/21/2016           31        11        45                 30.15   \n",
       "21  1/22/2016           26         6        41                 30.21   \n",
       "22  1/23/2016           26        21        78                 29.77   \n",
       "23  1/24/2016           28        11        53                 29.92   \n",
       "24  1/25/2016           34        18        54                 30.25   \n",
       "25  1/26/2016           43        29        56                 30.03   \n",
       "26  1/27/2016           41        22        45                 30.03   \n",
       "27  1/28/2016           37        20        51                 29.90   \n",
       "28  1/29/2016           36        21        50                 29.58   \n",
       "29  1/30/2016           34        16        46                 30.01   \n",
       "30  1/31/2016           46        28        52                 29.90   \n",
       "\n",
       "    VisibilityMiles  WindSpeedMPH PrecipitationIn  CloudCover    Events  \\\n",
       "0                10           8.0               0           5       NaN   \n",
       "1                10           7.0               0           3       NaN   \n",
       "2                10           8.0               0           1       NaN   \n",
       "3                10           9.0               0           3       NaN   \n",
       "4                10           5.0               0           0       NaN   \n",
       "5                10           4.0               0           0       NaN   \n",
       "6                10           2.0               0           3       NaN   \n",
       "7                10           4.0               0           8       NaN   \n",
       "8                 9           8.0               T           8      Rain   \n",
       "9                 4           NaN             1.8           7      Rain   \n",
       "10               10           NaN               0           1       NaN   \n",
       "11               10           6.0               T           4       NaN   \n",
       "12               10          10.0               0           0       NaN   \n",
       "13               10           5.0               T           7       NaN   \n",
       "14                9           5.0               T           2       NaN   \n",
       "15                8           7.0            0.24           7      Rain   \n",
       "16                8           6.0            0.05           6  Fog-Snow   \n",
       "17                9          12.0               T           2      Snow   \n",
       "18               10          11.0               0           1       NaN   \n",
       "19               10           6.0               0           2       NaN   \n",
       "20               10           6.0               0           1       NaN   \n",
       "21                9           NaN            0.01           3      Snow   \n",
       "22                1          16.0            2.31           8  Fog-Snow   \n",
       "23                8           6.0               T           3      Snow   \n",
       "24               10           3.0               0           2       NaN   \n",
       "25               10           7.0               0           2       NaN   \n",
       "26               10           7.0               T           3      Rain   \n",
       "27               10           5.0               0           1       NaN   \n",
       "28               10           8.0               0           4       NaN   \n",
       "29               10           7.0               0           0       NaN   \n",
       "30               10           5.0               0           0       NaN   \n",
       "\n",
       "    WindDirDegrees  \n",
       "0              281  \n",
       "1              275  \n",
       "2              277  \n",
       "3              345  \n",
       "4              333  \n",
       "5              259  \n",
       "6              293  \n",
       "7               79  \n",
       "8               76  \n",
       "9              109  \n",
       "10             289  \n",
       "11             235  \n",
       "12             284  \n",
       "13             266  \n",
       "14             101  \n",
       "15             340  \n",
       "16             345  \n",
       "17             293  \n",
       "18             293  \n",
       "19             302  \n",
       "20             312  \n",
       "21              34  \n",
       "22              42  \n",
       "23             327  \n",
       "24             286  \n",
       "25             244  \n",
       "26             311  \n",
       "27             234  \n",
       "28             298  \n",
       "29             257  \n",
       "30             241  "
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df = pd.read_csv('nyc_weather.csv')\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Temperature'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8      1/9/2016\n",
       "9     1/10/2016\n",
       "15    1/16/2016\n",
       "26    1/27/2016\n",
       "Name: EST, dtype: object"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['EST'][df['Events']== 'Rain']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.fillna(0, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6.225806451612903"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['WindSpeedMPH'].mean()"
   ]
  }
 ],
 "metadata": {
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
