from config import *

ma = 'mass'
cg = 'Code Guess'

atomic_mass_set = list(atomic_mass.keys())
#atomic_mass_set.reverse()

df = pd.read_excel('./PeakList.xlsx', sheet_name=None)

for sheet in df:
    df[sheet][cg] = np.nan
    masses        = list(df[sheet][ma].values)
    tmp           = df[sheet]
    for mass in masses:
        guess         = []
        j             = 0
        dum = tmp.loc[tmp[ma]==mass]
        for x in get_mols(atomic_mass_set, mass, 0.1):
            molecule = ''
            for y in atomic_mass_set:
                if x.count(y) == 0:
                    continue
                if x.count(y) == 1:
                    molecule += atomic_mass[y]
                else:
                    molecule += atomic_mass[y] + '_{' + str(x.count(y)) + '}'
            if molecule not in guess:
                guess.append(molecule)
            if len(guess) > 50:
                break
        dum[cg] = ','.join(guess)
        tmp.update(dum)
        tmp.to_excel('./'+sheet+'.xlsx')
    df[sheet].update(tmp)
    tmp.to_excel('./'+sheet+'.xlsx')
