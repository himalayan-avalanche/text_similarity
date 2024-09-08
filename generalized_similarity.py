 def get_generalized_DamerauLevenshtein_similarity(s1,s2):
      """
      Compute the generalized similarity betwee two strings
      """
      
      from itertools import zip_longest
      import rapidfuzz
      if s1=='' or s2=='':
          return 0
      
      s1=s1.lower()
      s2=s2.lower()
      t1=''
      t2=''
      
      simi=0; cnt=0
      for a,b in zip_longest(s1,s2):
          if a:
              t1=t1+a
          if b:
              t2=t2+b
          cnt+=1
          simi+=rapidfuzz.distance.DamerauLevenshtein.normalized_similarity(t1,t2)
          
      return simi/cnt



#### Example 1

 import rapidfuzz, numpy as np
 
 s1='dummy'
 s2='dummies'
 
 print(f'Hamming similarity is :                           {np.round(rapidfuzz.distance.Hamming.normalized_similarity(s1,s2),3)}')
 print(f'Levenshtein similarity is :                       {np.round(rapidfuzz.distance.Levenshtein.normalized_similarity(s1,s2),3)}')
 print(f'Damerau-Levenshtein similairty is :               {np.round(rapidfuzz.distance.DamerauLevenshtein.normalized_similarity(s1,s2),3)}')
 print(f'Generalized Damerau-Levenshtein similairty is :   {np.round(get_generalized_fuzz_dl_norm_simi(s1, s2),3)}\n')
 
 print(f'Jaro Winkler Similairty is :                      {np.round(rapidfuzz.distance.JaroWinkler.normalized_similarity(s1,s2),3)}')
 print(f'Generalized Jaro Winkler Similairty is :          {np.round(get_generalized_jaro_winkler_similarity(s1,s2),3)}')
 
 Hamming similarity is :                           0.571
 Levenshtein similarity is :                       0.571
 Damerau-Levenshtein similairty is :               0.571
 Generalized Damerau-Levenshtein similairty is :   0.863
 
 Jaro Winkler Similairty is :                      0.874
 Generalized Jaro Winkler Similairty is :          0.955      



 #### Example 2


 def get_generalized_DamerauLevenshtein_similarity(s1,s2):
      """
      Compute the generalized similarity betwee two strings
      """
      
      from itertools import zip_longest
      import rapidfuzz
      if s1=='' or s2=='':
          return 0
      
      s1=s1.lower()
      s2=s2.lower()
      t1=''
      t2=''
      
      simi=0; cnt=0
      for a,b in zip_longest(s1,s2):
          if a:
              t1=t1+a
          if b:
              t2=t2+b
          cnt+=1
          simi+=rapidfuzz.distance.DamerauLevenshtein.normalized_similarity(t1,t2)
          