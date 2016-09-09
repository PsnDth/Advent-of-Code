f = open('day19.txt', 'r')
replacements = f.read().splitlines()
f.close()
#molecule = "HOHOHO"
molecule = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"
#replacements = ["H => HO","H => OH", "O => HH"]
indexed = {}
steps = 0
'''
#part 1
for replacement in replacements:
    replacement = replacement.split(" ")
    if replacement[0] not in indexed:
        indexed[replacement[0]] = []
    indexed[replacement[0]].append(replacement[2])
print indexed

def genreplacements(molecule, index):
    for replacement in index:
        for substr in range(len(molecule) - len(replacement) + 1):
        #molecule.count(replacement) * len(index[replacement]) (amount of total unique replacements)
            if replacement == molecule[substr:substr + len(replacement)]:
                for alternate in index[replacement]:
                    replaced = list(molecule)
                    replaced[substr:substr + len(replacement)] = alternate
                    yield "".join(replaced)
uniqueChanges = len(set(genreplacements(molecule, indexed)))
print uniqueChanges
'''
for replacement in replacements:
    replacement = replacement.split(" ")
    if replacement[0] not in indexed:
        indexed[replacement[-1]] =  replacement[0]

def simplify(substr):
    global steps; steps += molecule.count(substr)
    global molecule;
    molecule = indexed[substr].join(molecule.split(substr))
    #print molecule
def electronify():
    for key in sorted(indexed.keys(), cmp=lambda x,y: cmp(len(x), len(y)), reverse=True):
        if key in molecule:
            simplify(key)
            break
while len(molecule) > 1:
    electronify()
    print steps, len(molecule)
#Never been so proud of a program in my life ...
                
        
