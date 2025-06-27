# Mencari jumlah berapa anak yang selamat dan tidak selamat
import pandas as pd
data = pd.read_csv('kapal_titanic.csv')
anakAnak = data[data['age'] < 18]
anakSelamat = anakAnak[anakAnak['survived'] == 1].shape[0]
anakTidakSelamat = anakAnak[anakAnak['survived'] == 0].shape[0]
print(anakSelamat)
print(anakTidakSelamat)