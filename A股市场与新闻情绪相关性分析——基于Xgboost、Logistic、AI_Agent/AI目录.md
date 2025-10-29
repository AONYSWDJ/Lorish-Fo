# 📊 A股市场文本情绪分析与行情验证报告  
**项目名称：结合 AI Agent 与 XGBoost 的文本情感预测**  
**作者：FU Shoahua**  
**日期：2025年10月**  
**作用：此报告主体内容为AI生成，充当目录使用，能够让您快速了解整体项目内容**  

-----

## 一、研究背景与目标

在金融市场中，新闻情绪往往能显著影响投资者预期与市场波动。然而，针对中文金融新闻的高质量标注语料稀缺，传统的监督学习方法难以直接应用。

本研究旨在通过 **结合大语言模型 Agent 与 XGBoost 预训练模型**，在有限人工标注条件下完成 **半监督情感识别任务**，进而量化新闻文本对 A 股市场行情的潜在影响。

研究目标包括：

1. 建立一套 **自动化文本情绪识别流程**，兼具可解释性与可扩展性；
2. 利用 AI Agent 提升伪标签质量，将无监督问题转化为半监督问题；
3. 结合行情数据验证情绪信号与市场走势的相关性。

---

## 二、研究方法与技术框架

### 1. 模型整体流程

1. **文本清洗与特征提取**
   - 对原始 JSON 数据进行清洗，去除全角符号（如 `\u3000`），并通过 `jieba` 提取“文章来源”字段；
   - 构造 `source`（新闻来源）和 `insert_time`（时间）两个新特征，用于后续特征增强。

2. **XGBoost 初步情绪预测**
   - 使用 WeiboSentiment 预训练模型（XGBoost）预测新闻文本情感；
   - 提取高置信度语料（预测概率 > 0.9 或 < 0.1）作为伪标签样本。

3. **AI Agent 标签复核**
   - 基于 LangChain 的 Agent 批量判定高置信度语料；
   - 保留模型与 Agent 一致判定的样本作为验证集；
   - 形成半监督学习框架。

4. **特征增强与半监督迭代**
   - 新增特征：
     - `Day`：从时间字段提取天数并标准化；
     - `freq`：新闻来源出现**频率编码**；
   - 采用 Logistic 回归与 KNN 半监督迭代模型进行对比对未标注数据进行伪标签传播；
   - 采用迭代方式优化模型结果；
   - 使用 Accuracy 与 F1-score 作为主要评价指标。

---

## 三、实验过程与结果分析

### 1. 初步 XGBoost 预测结果

| 指标 | 数值 |
|------|------|
| 样本总数 | 52,303 |
| 高置信度样本 | 1,187 |
| 预测标签分布 | 正类约 51%，负类约 49% |

---

### 2. KNN 半监督伪标签初始结果

| 模型 | Accuracy | F1-score |
|------|-----------|----------|
| KNN 半监督模型 | 0.617 | 0.615 |

KNN 模型能在高维稀疏特征下完成初步伪标签生成，但对数据分布敏感。

---

### 3. Logistic 迭代伪标签结果

| 迭代轮次 | 样本数 | Accuracy | F1-score |
|-----------|---------|-----------|-----------|
| 第 1 轮 | 2588 | 0.7136 | 0.7094 |
| 第 2~4 轮 | 2611 | 0.7136 | 0.7094 |
| 提前终止 | — | 模型收敛 | — |

最终 F1-score 达 **0.7094**，模型成功收敛，说明特征增强与伪标签机制有效。

---

## 四、A股行情验证（2025年3月15日–19日）

### 1. 新闻情绪均值走势

| 日期 | 平均情绪值 |
|------|-------------|
| 15日 | 0.1718 |
| 16日 | 0.2845 |
| 17日 | 0.3519 |
| 18日 | 0.3469 |
| 19日 | 0.3523 |

> 整体情绪略有上升，但波动较平缓。

---

### 2. 市场实际表现（上证指数）

| 日期 | 收盘波动 | 涨跌幅 | 成交变化 |
|------|-----------|--------|-----------|
| 17日 | -17.0 | 下跌 | -2503 |
| 18日 | -1.6 | 小跌 | -1484 |
| 19日 | +11.8 | 小涨 | -910 |

与情绪结果对比，市场未能在正向情绪增长阶段显著上涨。  
**结论：** 短期内新闻情绪与市场价格波动未形成显著共振。

---

## 五、创新点与方法优势

1. **AI Agent 与传统机器学习结合**  
   - Agent 辅助伪标签，显著提升无监督数据利用率；
   - 减少人工标注需求，提升可扩展性。

2. **多特征融合机制**  
   - 引入时间与新闻来源频率特征；
   - Logistic 模型可解释性强、计算效率高。

3. **多阶段验证体系**  
   - XGBoost → Agent → Logistic 半监督 → 市场验证；
   - 保证情绪结果具备统计与金融逻辑一致性。

---

## 六、改进方向与后续计划

1. **轻量化 Agent 替代方案**
   - 使用本地模型（如 **Ollama** 或 **FinanceMCP**）；
   - 降低 Token 成本并提升响应速度。

2. **特征工程深化**
   - 引入时间衰减权重；
   - 构建 CAPM 模型中的新闻情绪加权因子。

3. **量化分析扩展**
   - 将情绪信号与持仓量（Open Interest）结合；
   - 构建多因子交易信号或风险监测指标。

---

## 七、结论

本研究通过“**XGBoost + AI Agent + Logistic 半监督**”的混合框架，  
实现了从无标注金融新闻到可解释情绪预测的完整流程。

结论如下：

- 模型在半监督条件下可达 **F1 ≈ 0.71**；
- 新闻情绪与短期行情相关性有限；
- 框架具备良好的扩展性，可用于更广泛的情感驱动研究。

该方法为 **金融情绪量化与事件驱动型市场研究** 提供了一条高性价比、可复现的路径。

---  

## 八、代码框架
本项目整体由六个部分组成，通过面对对象的方式构建代码的健壮性，为后续嵌入其他项目打下良好基础整体代码框架如下：

- **agent**
  - csv读取保存工具  
  - Agent
- **data**  
  - 任务一与任务二所有改造后的数据
- **半监督模型**
  - 面对对象的KNN模型
  - 同样封装好的Logistic模型  
- **笔试内容**
  - 原始要求以及原始数据
- **预训练模型模型**
  - githubrequest 只使用了其中的xgboost模型以及停词
- **代码notebook**
  - 代码内容
  - 详细步骤的markdown

----
*报告完*
# 📊 A-Share Market Sentiment Analysis and Market Validation Report  
**Project Title:** Text Sentiment Prediction Combining AI Agent and XGBoost  
**Author:** FU Shoahua  
**Date:** October 2025  
**Note:** This report is AI-generated and serves as a structured overview to help readers quickly grasp the core content of the project.  

---

## I. Research Background and Objectives  

In financial markets, news sentiment often exerts a significant influence on investor expectations and market volatility. However, due to the scarcity of high-quality labelled Chinese financial news data, traditional supervised learning approaches are difficult to apply directly.

This study aims to complete a **semi-supervised sentiment recognition task** by **integrating a Large Language Model (AI Agent) with a pretrained XGBoost model**, under limited human annotation. It further quantifies the potential impact of news sentiment on the A-share market.  

**Objectives:**  
1. Develop an **automated sentiment recognition pipeline** with interpretability and scalability;  
2. Enhance pseudo-label quality using an AI Agent to transform an unsupervised task into a semi-supervised framework;  
3. Validate the correlation between sentiment signals and market movements using historical trading data.  

---

## II. Methodology and Technical Framework  

### 1. Overall Workflow  

1. **Text Cleaning and Feature Extraction**  
   - Cleaned raw JSON data, removed full-width symbols (e.g. `\u3000`), and extracted the *source* field using `jieba`;  
   - Constructed two new features: `source` (news origin) and `insert_time` (timestamp) for feature enhancement.  

2. **Initial XGBoost Sentiment Prediction**  
   - Applied a pretrained WeiboSentiment XGBoost model for sentiment inference;  
   - Extracted high-confidence samples (prediction probability > 0.9 or < 0.1) as pseudo-labelled data.  

3. **AI Agent Label Verification**  
   - Utilised a LangChain-based Agent to verify high-confidence samples;  
   - Retained samples with consistent decisions between the Agent and XGBoost as the validation set;  
   - Formed a semi-supervised learning pipeline.  

4. **Feature Enhancement and Semi-Supervised Iteration**  
   - Added new features:  
     - `Day`: normalised day extracted from timestamps;  
     - `freq`: frequency encoding of news sources;  
   - Compared Logistic Regression and KNN-based semi-supervised iterative models for pseudo-label propagation;  
   - Evaluated models using **Accuracy** and **F1-score** metrics.  

---

## III. Experimental Process and Results  

### 1. Initial XGBoost Results  

| Metric | Value |
|---------|--------|
| Total Samples | 52,303 |
| High-Confidence Samples | 1,187 |
| Label Distribution | Positive ~51%, Negative ~49% |

---

### 2. KNN Semi-Supervised Results  

| Model | Accuracy | F1-score |
|--------|-----------|----------|
| KNN Semi-Supervised | 0.617 | 0.615 |

The KNN model generated preliminary pseudo-labels under high-dimensional sparse features but showed sensitivity to data distribution.  

---

### 3. Logistic Iterative Results  

| Iteration | Sample Size | Accuracy | F1-score |
|------------|--------------|-----------|-----------|
| Round 1 | 2,588 | 0.7136 | 0.7094 |
| Rounds 2–4 | 2,611 | 0.7136 | 0.7094 |
| Early Stop | — | Model Converged | — |

The final **F1-score reached 0.7094**, indicating effective feature enhancement and pseudo-labelling mechanisms.  

---

## IV. Market Validation (15–19 March 2025)  

### 1. Average Sentiment Trend  

| Date | Average Sentiment |
|------|--------------------|
| 15 Mar | 0.1718 |
| 16 Mar | 0.2845 |
| 17 Mar | 0.3519 |
| 18 Mar | 0.3469 |
| 19 Mar | 0.3523 |

> Sentiment rose slightly overall, though volatility remained limited.  

---

### 2. Actual Market Performance (Shanghai Composite Index)  

| Date | Closing Movement | Change | Turnover Variation |
|------|-------------------|--------|--------------------|
| 17 Mar | -17.0 | Decline | -2503 |
| 18 Mar | -1.6 | Slight Drop | -1484 |
| 19 Mar | +11.8 | Mild Rise | -910 |

Comparing sentiment with market data, no significant short-term resonance between rising sentiment and market performance was observed.  
**Conclusion:** Short-term sentiment changes did not produce a statistically significant market response.  

---

## V. Innovation and Advantages  

1. **Hybrid Framework of AI Agent and Traditional ML**  
   - AI Agent-assisted pseudo-labelling significantly improves the use of unlabelled data;  
   - Reduces manual annotation costs while maintaining scalability.  

2. **Multi-Feature Fusion Mechanism**  
   - Introduced temporal and source-frequency features;  
   - Logistic model ensures interpretability and computational efficiency.  

3. **Multi-Stage Validation System**  
   - Pipeline: XGBoost → Agent → Semi-supervised Logistic → Market Validation;  
   - Ensures consistency between statistical and financial logic.  

---

## VI. Future Improvements and Extensions  

1. **Lightweight Agent Alternatives**  
   - Integrate local models (e.g. **Ollama** or **FinanceMCP**) to reduce token costs and improve response speed.  

2. **Enhanced Feature Engineering**  
   - Introduce time-decay weighting;  
   - Construct CAPM-style sentiment-weighted factors.  

3. **Quantitative Extension**  
   - Combine sentiment signals with Open Interest;  
   - Develop multi-factor trading signals or risk-monitoring indicators.  

---

## VII. Conclusion  

This study establishes a complete pipeline for interpretable sentiment prediction based on the **XGBoost + AI Agent + Semi-supervised Logistic** framework.  

**Key Findings:**  
- Achieved F1 ≈ **0.71** under semi-supervised conditions;  
- Limited short-term correlation between news sentiment and market returns;  
- Framework demonstrates strong scalability for sentiment-driven financial analysis.  

The methodology provides a **cost-efficient and reproducible** path for **quantitative sentiment analysis and event-driven market research**.  

---

## VIII. Code Framework  

The project is modular and object-oriented, ensuring robustness and flexibility for integration into other research pipelines.  

- **agent/**
  - CSV reading and saving utilities  
  - Agent core logic  
- **data/**
  - All modified datasets for Task 1 and Task 2  
- **semi_supervised_models/**
  - Object-oriented KNN implementation  
  - Encapsulated Logistic model  
- **exam/**
  - Original problem statements and raw data  
- **pretrained_models/**
  - `githubrequest` library using only XGBoost and stopwords modules  
- **notebooks/**
  - Core code and step-by-step Markdown documentation  

---

*End of Report*
