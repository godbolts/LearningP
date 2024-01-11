from random import choice

def mängi(esimene, teine):
    if esimene == 'kivi' and teine == 'kivi':
        vastus = 'viik'
    elif esimene == 'paber' and teine == 'paber':
        vastus = 'viik'
    elif esimene == 'käärid' and teine == 'käärid':
        vastus = 'viik'
    elif esimene == 'käärid' and teine == 'paber':
        vastus = 'esimene'
    elif esimene == 'käärid' and teine == 'kivi':
        vastus = 'teine'
    elif esimene == 'paber' and teine == 'kivi':
        vastus = 'esimene'
    elif esimene == 'paber' and teine == 'käärid':
        vastus = 'teine'
    elif esimene == 'kivi' and teine == 'käärid':
        vastus = 'esimene'
    elif esimene == 'kivi' and teine == 'paber':
        vastus = 'teine'
    return vastus

i = 0
m_skoor = 0
a_skoor = 0

while i < 3:
    mängija = input('Sisesta oma valik: ')
    arvuti = choice(['kivi', 'paber', 'käärid'])
    vastus = mängi(mängija, arvuti)
    i += 1
    if vastus == 'viik':
        print(f'Arvuti valis {arvuti}. Viik! Sina {m_skoor}, arvuti {a_skoor}')
    elif vastus == 'esimene':
        m_skoor += 1
        print(f'Arvuti valis {arvuti}. Sina võitsid! Sina {m_skoor}, arvuti {a_skoor}')
    elif vastus == 'teine':
        a_skoor += 1
        print(f'Arvuti valis {arvuti}. Arvuti võitis! Sina {m_skoor}, arvuti {a_skoor}')

if m_skoor < a_skoor:
    print('Arvuti võitis')
elif m_skoor > a_skoor:
    print('Sina võitsid!')
else:
    print('Viik!')