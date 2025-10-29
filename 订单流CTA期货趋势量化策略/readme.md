# **Futures Trend Quantitative Strategy: Order Flow–Based Detection and Trend Following**

## Project Overview  
This project presents a CTA (Commodity Trading Advisor) trend-following strategy that relies on **real-time order flow data** to identify dominant market participants and lock in optimal price levels.  
It demonstrates how high-frequency data can be used to capture directional bias and enhance short-term decision-making precision.  

- **Strategy Type:** Trend Following  
- **Underlying Assets:** Commodity Futures  
- **Trading Frequency:** Minute-level (1-minute bars)  

---

## Core Signal Logic  

1. **Delta Accumulation Analysis:**  
   Determines the market’s dominant side (bullish or bearish) based on the cumulative delta factor, revealing where the major participants are building positions.  

2. **Volume Cluster Locking:**  
   Uses volume accumulation zones (“stacking bands”) to identify dominant price levels and optimal entry timing.  

3. **Profit Range Estimation:**  
   Employs a simple linear regression model to predict the upper profit boundary and assist in take-profit decision-making.  

4. **Micro-order and POC (Point of Control) Reversal Detection:**  
   Analyses micro-level order flow and POC shifts to capture potential reversal tendencies and ideal exit moments.  

---

# **期货趋势量化策略：基于订单流信号的主力判断与趋势跟随**

## 简要说明  
本项目展示了一个同样依赖数据实时更新的 **CTA 趋势跟随策略**，  
通过对 **实时订单流数据** 的分析，实现了对市场主力方向的识别与价位锁定。  
该策略旨在利用高频数据特征捕捉市场趋势，并在主力资金运动中寻求入场与出场的最佳时机。  

- **策略类型：** 趋势跟随  
- **标的资产：** 商品期货  
- **交易周期：** 分钟级别（1min）  

---

## 信号逻辑  

1. **累计 Delta 因子识别主力方向：**  
   通过对累计 delta 的计算，判断多空主力的持仓变化与方向偏移，识别主力进场位置。  

2. **堆积带锁定主力价位与入场时机：**  
   利用成交量堆积区间（Volume Cluster）确定主力建仓价带与最优入场节点。  

3. **线性回归预测盈利上限：**  
   通过简单线性回归模型，对可能的利润区间进行预测，辅助止盈决策。  

4. **微单与 POC 反转信号监测：**  
   结合微单成交与控制价位（POC）的动态变化，识别市场反转迹象与最佳出场时机。  


