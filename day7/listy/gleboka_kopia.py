# kopia wartości a nie referencji (adresy w pamięci)
import copy



nabial = ['jajka','mleko','twaróg']
chemia = ['domestos',"płyn do naczyń", 'proszek do prania']

zakupy_listopad = [nabial, chemia]

zakupy_grudzien = copy.deepcopy(zakupy_listopad)

print(f)