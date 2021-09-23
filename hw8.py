"""
Grace Michael
DS2000: Programming with Data
HW 8
"""


# Step 1
#read the data into the pandas dataframe
import csv
import pandas
import matplotlib.pyplot as plt

column_names = ['id','binflag','mass_jup','radius_jup','period_days',
'semimajor_axis_AU', 'eccentricity', 'periastron',
'longitude', 'ascending_node', 'inclination',
'surface_temp_K','age_Gyr','method','year','last_updated',
'ra','dec','distance_parsec','star_mass','star_radius',
'star_metallicity','star_temp_K','star_age_Gyr','lists']

def read_file(filename):

    # open and read data
    with open(filename, 'r') as file:
        data = pandas.read_csv(file, delimiter=',', header=None)
        # create columns to allow for data access
        data.columns = column_names
        column_list = []
        # make a data frame, accounting for columns
        df = pandas.DataFrame(column_list)
        for column in file:
            column = row.split()
            column_list.append(column)

        return data

# Step 2
# make new columns

def disr_lightyear(data):
    # convert parsec to lightyear
    lightyear_distance = data['distance_parsec'] * 3.26 * 186000
    # add a column
    data['distance_lyr'] = lightyear_distance
    return data


def mass(data):
    # convert mass from jupiter mass to earth mass
    mass_earth = data['mass_jup'] * 1898.6 / 5.97
    # add a column
    data['mass_earth'] = mass_earth
    return data


def radius(data):
    # convert radii from jupiter radii to earth radii
    radius_earth = data['radius_jup'] * 69911 / 6371
    # add a column
    data['radius_earth'] = radius_earth
    return data

def parker_time(data):
    # convert lightyear distance to miles per second
    miles_p_sec = 430000 / 60 / 60
    d_lyr = data['distance_lyr']
    distance = d_lyr / miles_p_sec
    # convert the seconds into years
    years = distance / 60 / 60 / 24 / 365
    # add a column
    data['travel_time_parker'] = years
    return data


# Step 3

# drop columns and summarize your data
keep_columns = ['id','mass_earth','radius_earth','period_days',
'semimajor_axis_AU',
'surface_temp_K','method','year',
'distance_lyr', 'travel_time_parker']

 # see main below

# Step 4

def closest(data):
    # sort from smallest to largest distance
    rank_distance = data.sort_values(by= 'distance_lyr', ascending=True)
    # first 10 smallest distances are closest
    top_planets = rank_distance.head(10)
    return top_planets


# Step 5

def life(data):
    # create new df so planet and its info are shown
    # between the surface temps
    new_df = data[(data['surface_temp_K'] >= 273)]
    new_df = new_df[(new_df['surface_temp_K'] <= 311)]
    # between the masses
    new_df = new_df[(new_df['mass_earth'] >= .5)]
    new_df = new_df[(new_df['mass_earth'] <= 10)]

    return new_df



# Step 6
# Planet mass vs orital axes

def mass_v_orbital(data):

    # differentiate Earth, RV, and transit
    transit_df = data[(data['method'] == 'transit')]
    RV_df = data[(data['method'] == 'RV')]
    earth_df = data[(data['id'] == 'Earth')]
    plt.scatter(transit_df.semimajor_axis_AU, transit_df.mass_earth, color = 'red', s = 1, label = 'Transit Method')
    plt.scatter(RV_df.semimajor_axis_AU, RV_df.mass_earth, color = 'blue', s = 1, label = 'RV Method')
    plt.scatter(earth_df.semimajor_axis_AU, earth_df.mass_earth, marker = 'x', color = 'green', label = 'Earth')

    # labels and styling
    plt.xscale('log')
    plt.yscale('log')
    plt.ylabel('Planet Mass')
    plt.xlabel('Orbital Axes')
    plt.title('Planet Mass vs Orbital Axis')
    plt.grid()
    plt.legend()
    plt.savefig("planet_scatter_plot.pdf", bbox_inches='tight')
    plt.show()


def main():
    # all outputs
    data = read_file('exoplanets.csv')
    disr_lightyear(data)
    mass(data)
    radius(data)
    parker_time(data)
    data2 = data[keep_columns]
    print(closest(data2))
    print(life(data2))
    mass_v_orbital(data)



main()

# Output 3
'''
                 id  binflag  ...              lists  distance_lyr
0       KOI-1843.03        0  ...      Controversial  8.175734e+07
1      Kepler-974 b        0  ...  Confirmed planets  8.175734e+07
2       KOI-1843.02        0  ...      Controversial  8.175734e+07
3        Kepler-9 b        0  ...  Confirmed planets  3.941340e+08
4        Kepler-9 c        0  ...  Confirmed planets  3.941340e+08
...             ...      ...  ...                ...           ...
4440      eta Cet b        0  ...  Confirmed planets  2.303562e+07
4441      eta Cet c        0  ...  Confirmed planets  2.303562e+07
4442    HD 108874 b        0  ...  Confirmed planets  4.153566e+07
4443    HD 108874 c        0  ...  Confirmed planets  4.153566e+07
4444  Kepler-1473 b        0  ...  Confirmed planets  4.030845e+08

[4445 rows x 26 columns]

                 id  binflag  ...  distance_lyr   mass_earth
0       KOI-1843.03        0  ...  8.175734e+07     0.445233
1      Kepler-974 b        0  ...  8.175734e+07          NaN
2       KOI-1843.02        0  ...  8.175734e+07          NaN
3        Kepler-9 b        0  ...  3.941340e+08    79.505863
4        Kepler-9 c        0  ...  3.941340e+08    54.063987
...             ...      ...  ...           ...          ...
4440      eta Cet b        0  ...  2.303562e+07   782.337688
4441      eta Cet c        0  ...  2.303562e+07  1004.954104
4442    HD 108874 b        0  ...  4.153566e+07   432.511893
4443    HD 108874 c        0  ...  4.153566e+07   323.747873
4444  Kepler-1473 b        0  ...  4.030845e+08          NaN

[4445 rows x 27 columns]

                 id  binflag  mass_jup  ...  distance_lyr   mass_earth  radius_earth
0       KOI-1843.03        0    0.0014  ...  8.175734e+07     0.445233      0.592559
1      Kepler-974 b        0       NaN  ...  8.175734e+07          NaN      1.536264
2       KOI-1843.02        0       NaN  ...  8.175734e+07          NaN      0.779105
3        Kepler-9 b        0    0.2500  ...  3.941340e+08    79.505863      9.217586
4        Kepler-9 c        0    0.1700  ...  3.941340e+08    54.063987      8.998120
...             ...      ...       ...  ...           ...          ...           ...
4440      eta Cet b        0    2.4600  ...  2.303562e+07   782.337688           NaN
4441      eta Cet c        0    3.1600  ...  2.303562e+07  1004.954104           NaN
4442    HD 108874 b        0    1.3600  ...  4.153566e+07   432.511893           NaN
4443    HD 108874 c        0    1.0180  ...  4.153566e+07   323.747873           NaN
4444  Kepler-1473 b        0       NaN  ...  4.030845e+08          NaN      1.163172

[4445 rows x 28 columns]

                 id  binflag  ...  radius_earth  travel_time_parker
0       KOI-1843.03        0  ...      0.592559            0.021705
1      Kepler-974 b        0  ...      1.536264            0.021705
2       KOI-1843.02        0  ...      0.779105            0.021705
3        Kepler-9 b        0  ...      9.217586            0.104634
4        Kepler-9 c        0  ...      8.998120            0.104634
...             ...      ...  ...           ...                 ...
4440      eta Cet b        0  ...           NaN            0.006115
4441      eta Cet c        0  ...           NaN            0.006115
4442    HD 108874 b        0  ...           NaN            0.011027
4443    HD 108874 c        0  ...           NaN            0.011027
4444  Kepler-1473 b        0  ...      1.163172            0.107010

[4445 rows x 29 columns]

'''

# Output 4
'''
                      id   mass_earth  ...  distance_lyr  travel_time_parker
2445  Proxima Centauri d     0.290196  ...    785236.200            0.000208
2447  Alpha Centauri B c          NaN  ...    785236.200            0.000208
2446  Alpha Centauri B b     1.132163  ...    785236.200            0.000208
2443  Proxima Centauri b     1.173825  ...    785236.200            0.000208
2444  Proxima Centauri c     7.004148  ...    785236.200            0.000208
3583      WISE 0855-0714  1908.140704  ...   1400691.600            0.000372
2468     Lalande 21185 b     3.816281  ...   1546218.000            0.000410
1605       eps Eridani b   205.125126  ...   1950114.396            0.000518
4316            GJ 887 c     7.603941  ...   1994924.400            0.000530
4315            GJ 887 b     4.201090  ...   1994924.400            0.000530

[10 rows x 10 columns]
'''

# Output 5
'''
                id  mass_earth  ...  distance_lyr  travel_time_parker
506          Earth    1.000407  ...           NaN                 NaN
1185     GJ 1132 c    2.642775  ...     7652263.2            0.002032
1313  Gliese 163 c    6.802840  ...     9095400.0            0.002415
4380    HD 85512 b    3.498258  ...     6760914.0            0.001795

[4 rows x 10 columns]
'''
