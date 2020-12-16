# SSO
SSO (Simplified Swarm Optimization) is proposed by Yeh in 2009 [1]. It is one of the novel swarm intelligence algorithms. It features simplicity, efficiency and flexibility for modification.

## 自定義資料格式
```python
data = {'Nvar':10} 
```
## 改寫初始解產生方式
```python
def create_particle(num):
    return [random.randint(0,5) for _ in range(data['Nvar'])]
```
## 改寫適應度函數
```python
def cal_fit(solution, data):
    total = 0
    for i in range(data['Nvar']):    
        total+= solution[i]
    return total 
```
## 初始化
```python
sso = SSO(data, 5,100)//SSO(data, 母群體個數, 世代數)
```
## 替代原本function
```python
sso.create_particle = create_particle
sso.cal_fit = cal_fit
```
## 執行
```python
sso.run()
```



