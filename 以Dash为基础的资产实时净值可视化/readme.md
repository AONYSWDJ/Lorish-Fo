# **DashingAutomaticRefreshingDiagram**

## **Introduction**  
This project presents a **real-time asset net value visualisation dashboard**, built with Dash and Plotly.  
It employs **multithreading** to synchronise data fetching, saving, and caching, while supporting real-time updates and interactive display.  

---

## **Architecture and Core Functions**

1. **Multithreading for Data Handling**  
   - Implements concurrent data fetching and processing via multiple threads.  
   - API login and data retrieval are executed in parallel, boosting efficiency.  
   - Uses `lock` mechanisms to ensure thread-safe file reading and saving.  

2. **Data Caching**  
   - A dedicated `cache` directory stores daily data.  
   - Old data is automatically removed using `os` system checks.  

3. **Frontend Visualisation**  
   - Built with **Dash** and **Plotly** to visualise:  
     - Historical net asset value (NAV)  
     - Intraday real-time NAV  
     - Historical NAV rate of change  
   - Supports interactive range sliders and zooming.  

4. **Dynamic Data Update and Persistence**  
   - Supports multiple APIs for data fetching and login, including **Akshare**, **Tushare**, and **XTtrader**.  

5. **Framework-oriented Design**  
   - Designed with a **stacked functional structure** for flexible maintenance.  
   - Modular interfaces allow easy modification of plotting logic and login endpoints.  

6. **Trading-hour Detection**  
   - Automatically pauses updates during non-trading hours and resumes when markets open.  
   - Automatically backfills missing data upon restart.  

7. **Time Window Interaction**  
   - Allows sliding through specific time ranges to analyse selected product NAVs.  
   - Automatically computes rate of change relative to the earliest date in the window.  

---

## **Usage Guide**

1. Clone the repository.  
2. Fill in the login credentials for your chosen API.  
3. Modify the `login` function in the main thread to match your interface requirements.  
4. Adjust data-fetching and chart-rendering logic as needed.  
5. This project is recommended for **server-side deployment**.  
   - XTtrader **does not support virtual machine logins**.  
   - Other data sources can run on virtualised environments.  
6. On first run, initialise and save your local dataset following the provided file naming rules to ensure proper execution.  

---

## **Code Logic Overview**

### **FAQ & Design Philosophy**
- **Why dual sub-thread architecture (Main + Sub)?**  
  Because symmetry is elegant — one handles data updates, the other manages plotting.
- **Why global dictionaries instead of queues?**  
  Queues can become empty upon consumption; global dicts allow persistent access.  
- **Why functional programming instead of classes?**  
  This is a standalone script rather than a full project — classes add unnecessary verbosity (`self` fatigue included).  
  Still, a class-based rewrite would indeed be more robust.

### **Execution Logic**
- **Main Thread:** Initialises login, performs the first plot to ensure the dashboard displays before updates start.  
  - **Sub-thread 1:**  
    `while True → fetch data → clean/transform → save locally → update global dictionary`  
  - **Sub-thread 2:**  
    Reads from shared data → processes timestamps → refreshes plots through `callback` loops.  

---

## **Important Notes**
1. The **XTtrader API** supports up to **Python 3.8** (most stable on **3.6**), hence the project is developed under **Python 3.6**.  
2. The `code` directory contains essential runtime files (`.pyi`) required by XTtrader.  
   - Missing them or lacking an account will cause runtime errors.  
3. The `ProjectDemo` file is the integrated, stable version.  
   - For quick reproduction, use `ProjectTrail`.  
   - Although less maintainable, it runs effectively (until I decided to delete it for sanity reasons 😄).  

---

# **实时资产净值可视化系统：DashingAutomaticRefreshingDiagram**

## **项目介绍**  
本项目实现了一个 **实时更新资产净值的可视化系统**，  
通过 **Dash + Plotly** 构建前端展示，并利用 **多线程** 技术实现数据获取、保存与缓存的同步执行。  
同时支持对实时数据的读取、展示与交互操作。  

---

## **系统架构与核心功能**

1. **多线程并行处理**  
   - 通过多线程实现数据的并行获取与处理。  
   - API 登录与数据读取同步进行，提高效率。  
   - 使用 `lock` 对文件读写进行锁定，确保线程安全。  

2. **数据缓存机制**  
   - 脚本内设有 `cache` 文件夹保存当日数据。  
   - 通过 `os` 模块自动检测并删除过期缓存。  

3. **前端可视化展示**  
   - 使用 **Dash** 与 **Plotly** 实现：  
     - 历史资产净值曲线  
     - 当日实时净值曲线  
     - 历史净值涨跌幅曲线  
   - 支持 `rangeslider` 时间滑动交互。  

4. **数据动态更新与存储**  
   - 支持多 API 登录与数据获取，目前包括 **Akshare**、**Tushare**、**XTtrader**。  

5. **框架化接口设计**  
   - 采用堆叠式函数逻辑，保留灵活接口，便于后续维护与扩展。  

6. **开盘时间智能判断**  
   - 在非交易时段自动暂停更新；  
   - 开盘时自动恢复并补全缺失数据。  

7. **滑动时间窗口研究**  
   - 可通过时间滑块研究特定区间内的产品净值表现；  
   - 自动以时间窗口最早日期为基准计算涨跌幅。  

---

## **使用说明**

1. 克隆项目仓库；  
2. 填写登录接口与账户信息；  
3. 修改主线程中的 `login` 函数；  
4. 根据自身需求调整数据源或绘图逻辑；  
5. 建议在服务器上运行；  
   - **XTtrader 不支持虚拟机登录**；  
   - 其他数据端口可在虚拟机运行；  
6. 初次运行时，请根据注释要求完成第一次数据录入并命名文件。  

---

## **代码逻辑拆解**

### **FAQ 与设计理念**
- **为什么采用主线程 + 子线程？**  
  因为我喜欢对称之美 —— 一个线程抓数据，一个线程画图。  
- **为什么不用 queue？**  
  因为 queue 消费后会为空，而全局字典可以持久化共享数据。  
- **为什么不用类？**  
  因为这只是脚本，不是完整项目。类写起来太累了 (`self` 满天飞)。  
  不过要更健壮的话，确实类更好。  

### **逻辑说明**
- **主线程：** 初始化登录，进行第一次绘图以确保图像加载。  
  - **子线程1：**  
    `while True → 获取数据 → 清洗 → 保存本地 → 更新全局变量`  
  - **子线程2：**  
    读取共享数据 → 时间判断与整理 → 绘图与 callback 刷新。  

---

## **注意事项**
1. **XTtrader** 最高仅支持 **Python 3.8**，最稳定版本为 **3.6**，因此本项目基于 **Python 3.6**。  
2. `code` 目录中以 `.pyi` 结尾的文件为 **XTtrader** 必要运行文件，缺失会报错。  
   - 同时须拥有有效账户，否则无法运行。  
3. `ProjectDemo` 为集成功能的主文件；  
   - 若仅需复现结果，可使用 `ProjectTrail`，代码虽略显凌乱，但功能完整。  
   - （不过维护起来确实“难亿点点”，所以我最终删了它 😆）  
