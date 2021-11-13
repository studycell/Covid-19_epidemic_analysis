import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import scipy
from scipy.integrate import odeint

# 人群感染数据
data = pd.read_csv("/Users/caizhen/Desktop/疫情分析项目/chinadailyconfirm.csv")
data = data[335:]
data.reset_index(inplace=True)
data_confirm = np.array(data["confirm"])

data_heal = np.array(data["heal"])
data_suspect = np.array(data["suspect"])
data = data_confirm
# 定义初始情况，易感染人数设为14亿人，感染人数和治愈人数为数据里的
S0, I0, R0 = 14000000000,data_confirm[0],data_heal[0]
#定义有数据的天数
t = np.linspace(0, len(data_confirm) - 1, len(data_confirm))
def SIR(sir, t, beta, gamma):
    "SIR模型的微分方程"
    S, I, R = sir
    dsdt = - beta * S * I
    didt = beta * S * I - gamma * I
    drdt = gamma * I
    return [dsdt, didt, drdt]
def f(beta, gamma):
    # 求解时序变化
    corr = []
    for a, b in zip(beta, gamma):
        result = odeint(SIR, [S0, I0, R0], t, args=(a, b))
        St, It, Rt = result[:, 0], result[:, 1], result[:, 2]
        corr.append(np.mean((It-data)**2))
    return np.array(corr)
# 定义粒子个数
N = 20
# 定义惯性因子
w = 0.1
# 定义C1，C2
c1, c2 = 2, 2
# 初始化位置
x = np.random.uniform(0, 1, [N, 2])
x[:, 0] *= 0.04
x[:, 1] *= 0.25
# 初始化速度
v = np.random.uniform(0, 1, [N, 2])
v[:, 0] *= 0.04 * 0.03
v[:, 1] *= 0.25 * 0.03
# 个体最佳位置
p_best = np.copy(x)

fitness = f(x[:, 0], x[:, 1])
fitness = np.expand_dims(fitness, 1)
# 群体最佳位置
g_best = p_best[np.argmin(fitness)]
N_step = 100
store = np.zeros([N, N_step, 2])
for step in range(N_step):
    # 计算速度v
    store[:, step, :] = x
    r1, r2 = np.random.random([N, 1]), np.random.random([N, 1])
    v = w * v + (1-w)*(c1 * r1 * (p_best - x) + c2 * r2 * (g_best - x))
    # 更新位置
    x = x + v
    x = np.clip(x, 0, 0.5)
    # 计算适应度
    fitness_new = f(x[:, 0], x[:, 1])
    fitness_new = np.expand_dims(fitness_new, 1)
    fit = np.concatenate([fitness, fitness_new], 1)
    fitness = fitness_new
    # 计算个体最优解
    p_best_for_sel = np.concatenate([
        np.expand_dims(x, 1),
        np.expand_dims(p_best, 1)], 1)
    p_best = p_best_for_sel[[i for i in range(N)], np.argmin(fit, 1), :]
    fit_p = f(p_best[:, 0], p_best[:, 1])
    # 计算全局最优解
    g_best = x[np.argmin(fitness[:, 0])]
    print(g_best)
a, b = g_best
dt = np.linspace(0, 30, 1000)
result = odeint(SIR, [S0, I0, R0], dt, args=(a, b))
St, It, Rt = result[:, 0], result[:, 1], result[:, 2]

x = np.arange(0, len(data), 1)
#print(len(x))
y = np.array(data)
#print(len(y))
z1 = np.polyfit(x, y, 3) # 用3次多项式拟合
p1 = np.poly1d(z1)
#print(p1) # 在屏幕上打印拟合多项式
yvals=p1(x) # 也可以使用yvals=np.polyval(z1,x)

# 绘图
fig, ax1 = plt.subplots()
ax1.plot(x, yvals, 'g',label="real-confirm_nihe")
ax1.plot(t, data, c="b", label="real-confirm")
ax1.plot(dt, It, c="r", linestyle="--", label="pre-confirm")

ax1.set_title("SIR module", fontsize=18)
ax1.set_xlabel("day", fontsize=18)

ax1.set_ylabel("number", fontsize=18)
ax1.legend(fontsize=18)
plt.grid(True)
time = np.linspace(0, 30, 31)

plt.xticks(time)
plt.show()
print(data)

