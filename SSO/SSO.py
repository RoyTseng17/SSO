# -*- coding: utf-8 -*-
"""
Title: Job Shop Scheduling Module
Version: 0.1
Author: Kuan-Chen Tseng k.c.tseng@ie.nthu.edu.tw
Copyright: Belongs to DAlab Solutions x Associates Co.,Ltd.
"""
import random
import copy
from Algorithm.Tools import Tools 
from Algorithm.Particle import Particle

class SSO():
    def __init__(self, data, Nsol, Ngen):
        self.data = data
        self.Nsol = Nsol
        self.Ngen = Ngen
        self.Cp = 0.3
        self.Cg = 0.8
        self.Cw = 0.9
        self.X = []
        self.pX = []
        self.gbest_sol = None

    def run(self):
        self.init()
        self.gFs, self.gbest = self.update()
        self.output()
        
    def init(self):
        self.X = []
        for i in range(self.Nsol):
            solution = self.create_particle(self.data)
            fitness = self.cal_fit(solution, self.data)
            self.X.append(Particle(solution, fitness))    
        self.pX = copy.deepcopy(self.X)
        self.gbest_sol = Tools.find_best(self.X)
        
    def create_particle(self, data):
        return [random.randint(0,5) for _ in range(data['Nvar'])]
    
    def cal_fit(self, solution, data):
        total = 0
        for i in range(data['Nvar']):    
            total+= solution[i]*solution[i]
        return total
    
    def step_wise_function(self, x, px, gbest, Cp, Cg, Cw):
        for var, value in enumerate(x):
            rnd_dot = random.random()
            if(rnd_dot < Cp):
                x[var] = px[var]
            if(rnd_dot < Cg):
                x[var] = gbest[var]
            elif(rnd_dot < Cw):
                continue
            else:
               x[var] = random.randint(0,5)
        return x
    
    def __create_solutions(self):
        for sol in range(self.Nsol):
            self.X[sol] = self.create_particle(self.data)
    
    def update(self):
        gBest_value_list = []
        for gen in range(self.Ngen):
            for sol in range(self.Nsol):
                x = self.X[sol]
                px = self.pX[sol]
                gbest = self.pX[self.gbest_sol]
                x = self.step_wise_function(x, px, gbest, self.Cp, self.Cg, self.Cw)
                x.F = self.cal_fit(x, self.data)
                if(Tools.compareTo(x.F,px.F)):
                    px.F = x.F
                    for var in range(len(px)):
                        px[var] =x[var]
                    if (Tools.compareTo(x.F,gbest.F)):
                        self.gbest_sol = sol
            gBest_value_list.append(gbest.F)
            print("Gen :{}".format(gen)," Gvalue:{}".format(gbest.F))       
        return gBest_value_list, self.pX[self.gbest_sol]
    def output(self):
        print('最佳解',self.gbest)



# =============================================================================
# 測試區
# =============================================================================
