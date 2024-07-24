'''
   @Author: manoj kr
   @Date: 2024-07-19 16:05
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-19 15:56
   @Title : Check Whether an Alphabet is Vowel or Consonant

'''
def vowel_consonant(alphabet):
    '''
    Description: 
               To check Alphabet is Vowel or Consonant  
    Parameters:
               str(alphabet): Alphabet need to check
    Returns:
             str: return "Vowel" or "Consonant"
    '''
    vowel="aeiouAEIOU"
    if(vowel.find(alphabet)== -1):
        return "consonant"
    else:
        return "Vowel"

def main():
    alphabet =input("give the Alphabet: ")
    print(vowel_consonant(alphabet))

if __name__=="__main__":
    main()
