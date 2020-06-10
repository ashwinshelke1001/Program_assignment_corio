'''This algorithm will generate the longest sequence of each pokemon.
Once a sequence is generated for a pokemon then from the last pokemon it will go back 
to the previous pokemon and check for other available option for sequence.
This way it will genrate longest possible sequence for each pokemon.
And among those sequences it will choose the longest one.'''


def getLongestSeq(pokemonList, pokemon, seq,seqLen, longestSeq):
    seq[seqLen] = pokemon
    seqLen += 1
    if seqLen > len(longestSeq):
        longestSeq[:] = seq[:seqLen]
    #Get the index of pokemonList at which element having list of pokemon starting
    # with last character of current pokemon is present. 
    nextPkmnIndx = ord(pokemon[-1]) - 97
    if nextPkmnIndx >= 0 and nextPkmnIndx < len(pokemonList):
        #Check for unused pokemon in sequence.
        for pkmn in pokemonList[nextPkmnIndx]:
            if pkmn[1]==0:
                pkmn[1] = 1
                #Recursively add the available pokemon in seq.
                getLongestSeq(pokemonList, pkmn[0], seq,seqLen, longestSeq)
                #Make the pokemon available for new sequence.
                pkmn[1] = 0
                 
def main():
    fp=open("Question45.txt")
    pokemonNames=fp.read().split()
    fp.close()
    pokemonList = [[] for i in range(26)]
    for pokemonName in pokemonNames:
        #The pokemonList is a list of list in which each element is a list of pokemon
        # starting with same alphabet. The element is also list of list having a
        # pokemon name and 0 or 1 next to it. 0 indicating pokemon not included in
        # the seq and 1 indicating pokemon included in seq. This will make sure no pokemon
        # is repeated in the seq. 
        pokemonList[ord(pokemonName[0]) - 97].append([pokemonName, 0])
    seq = [None] * len(pokemonNames)
    longestSeq = []
    for pokemons in pokemonList:
        for pokemon in pokemons:
            pokemon[1] = 1
            getLongestSeq(pokemonList, pokemon[0],seq, 0, longestSeq)
            pokemon[1] = 0
    print ("Longest sequence length:", len(longestSeq))
    print ("Longest pokemon sequence:")
    for i in longestSeq:
        print (i,end=" -> ")
    print()
 
main()
