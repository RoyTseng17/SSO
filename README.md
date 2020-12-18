# SSO
SSO (Simplified Swarm Optimization) is proposed by Yeh in 2009 [1]. It is one of the novel swarm intelligence algorithms. It features simplicity, efficiency and flexibility for modification.

## SSO 更新機制
![](https://i.imgur.com/pbuRHga.png)

[1] Yeh, W.-C. (2009). A two-stage discrete particle swarm optimization for the problem of multiple multi-level redundancy allocation in series systems. Expert Systems with Applications, 36(5), 9192–9200. 

## 自定義資料格式
```python
data = {'Nvar':10, 'UB':5} 
```
## 改寫初始解產生方式
```python
def create_particle(data):
    return [random.randint(0,data['UB']) for _ in range(data['Nvar'])]
```
## 改寫適應度函數
```python
def cal_fit(solution, data):
    total = 0
    for i in range(data['Nvar']):    
        total+= solution[i]
    return total 
```
## 改寫更新機制
```python
def step_wise_function(data, x, px, gbest, Cp, Cg, Cw):
    for var, value in enumerate(x):
        rnd_dot = random.random()
        if(rnd_dot < Cp):
            x[var] = px[var]
        if(rnd_dot < Cg):
            x[var] = gbest[var]
        elif(rnd_dot < Cw):
            continue
        else:
           x[var] = random.randint(0,data['UB'])
    return x
```
## 初始化
```python
#SSO(data, 母群體個數, 世代數)
sso = SSO(data, 5,100)
```
## 替代原本function
```python
sso.create_particle = create_particle
sso.cal_fit = cal_fit
sso.step_wise_function = step_wise_function
```
## 執行
```python
sso.run()
```

## Just copy this and run!

```python
from SSO.SSO import SSO
import random
import numpy as np #矩陣運算

#改寫初始解產生方式
def create_particle(data):
    return [random.randint(0,data['Nmc']-1) for _ in range(data['Ntask'])]

#改寫適應度函數
def cal_fit(x, data):
    time=[[0]] * data['Nmc']
    for i, mc_idx in enumerate(x):
        time[mc_idx]+=data['timeMatrix'][mc_idx,i]
    return 1/max(time)

#自行設定資料格式
def step_wise_function(data, x, px, gbest, Cp, Cg, Cw):
    for var, value in enumerate(x):
        rnd_dot = random.random()
        if(rnd_dot < Cp):
            x[var] = px[var]
        if(rnd_dot < Cg):
            x[var] = gbest[var]
        elif(rnd_dot < Cw):
            continue
        else:
           x[var] = random.randint(0,data['Nmc']-1)
    return x
timeMatrix = np.random.randint(100,500, size = (30, 100))
data = {'Nvar':10, 'timeMatrix':timeMatrix, 'Nmc':30, 'Ntask':100} 

#SSO(data, 母群體個數, 世代數)
sso = SSO(data, 10,200)
#替代原本function
sso.create_particle = create_particle
sso.cal_fit = cal_fit
sso.step_wise_function = step_wise_function
sso.run()

```



