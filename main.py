# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:32:47 2020

@author: Roy Tseng
"""

from SSO.SSO import SSO
import random


#改寫初始解產生方式
def create_particle(data):
    return [random.randint(0,data['UB']) for _ in range(data['Nvar'])]

#改寫適應度函數
def cal_fit(solution, data):
    total = 0
    for i in range(data['Nvar']):    
        total+= solution[i]
    return total 

#自行設定資料格式
data = {'Nvar':10, 'UB':7} 
#SSO(data, 母群體個數, 世代數)
sso = SSO(data, 5,100)
#替代原本function
sso.create_particle = create_particle
sso.cal_fit = cal_fit
sso.run()

        
    