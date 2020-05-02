import pandas as pd
import numpy as np
import random as rd

def cluster_kmeans(df, K):
  m=df.shape[0] #number of training examples
  n=df.shape[1]
  Centroids=np.array([]).reshape(n,0)
  Output={} 
  for i in range(K):
    rand=rd.randint(0,m-1)
    Centroids=np.c_[Centroids,df[rand]]
  for i in range(100):
       #step 2.a
        EuclidianDistance=np.array([]).reshape(m,0)
        for k in range(K):
            tempDist=np.sum((df-Centroids[:,k])**2,axis=1)
            EuclidianDistance=np.c_[EuclidianDistance,tempDist]
        C=np.argmin(EuclidianDistance,axis=1)+1
      
        
      #step 2.b
        Y={}
        for k in range(K):
          Y[k+1]=np.array([]).reshape(n,0)
        for i in range(m):
            Y[C[i]]=np.c_[Y[C[i]],df[i]]
     
        for k in range(K):
            Y[k+1]=Y[k+1].T
    
        for k in range(K):
            Centroids[:,k]=np.mean(Y[k+1],axis=0)
        Output=Y
        g=np.array(C)
        df1=np.c_[df,g]
  a=[]
  for i in range(0,len(EuclidianDistance)):
          a.append(min(EuclidianDistance[i]))
          u=a 
  mindist= pd.DataFrame(u)
  d=pd.DataFrame(C)
  d["min_dist"]=mindist
  return(d)        