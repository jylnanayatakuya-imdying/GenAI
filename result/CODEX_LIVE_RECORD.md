# 对照组（Codex CLI）实验结果实时记录

最后更新：2026-11-13 16:41:09

> 每跑完一道题自动重建本文件。代码由 Codex CLI（`codex exec`）生成，
> 评测口径与自研 harness 完全一致：编译结果来自 CODESYS 服务（真实编译），
> 用例结果来自本机仿真器，未通过编译的代码其用例一律计为未通过。
> 模型与 prompt 与实验 3/4 相同；Codex 每题独立空工作区，只拿到 TASK.md。

- model_a：`codex-cli 0.167.2` / wire_api=`responses` (18 题), `(未记录)` / wire_api=`responses` (14 题)
- model_b：`codex-cli 0.44.0` / wire_api=`chat` (32 题)

## 汇总

| 实验 | 模型 | 进度 | 首次编译 | 最终编译 | 用例通过 | held-out 用例 | 整题通过 | tokens (in/out) | 用时 (s) |
|---|---|---|---|---|---|---|---|---|---|
| 实验 1 | deepseek-v4-pro-0813 | 32/32 | 31/32 (96.9%) | 31/32 (96.9%) | 88/116 (75.9%) | 60/84 (71.4%) | 24/32 (75.0%) | 7609239/395037 | 6084 |
| 实验 2 | qwen3-coder-flash | 32/32 | 11/32 (34.4%) | 11/32 (34.4%) | 6/116 (5.2%) | 5/84 (6.0%) | 0/32 (0.0%) | 0/0 | 4104 |

## 实验 1：Codex CLI × deepseek-v4-pro-0813

| 题目 | 名称 | 来源 | 难度 | 编译 | 用例通过 | held-out | 整题通过 | 用时(s) | tokens(in/out) | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|
| E01 | Automated Filling Line Control | public | easy | ✅ | 0/6 | 0/5 | ❌ | 95 | 63486/6106 |  |
| E02 | Dual-Word Edge Detection | public | easy | ✅ | 1/4 | 0/3 | ❌ | 53 | 45453/3151 |  |
| E03 | Alarm Handling | public | easy | ✅ | 5/5 | 4/4 | ✅ | 55 | 55070/2755 |  |
| E04 | Jam Pump Debouncing and Runtime Ma | public | easy | ✅ | 4/4 | 3/3 | ✅ | 223 | 742860/13001 |  |
| E05 | Weld Gap Alarm and Startup Inhibit | public | easy | ✅ | 3/3 | 2/2 | ✅ | 126 | 135695/7598 |  |
| E06 | Aeration Blower Delayed Start | public | easy | ✅ | 3/3 | 2/2 | ✅ | 141 | 73962/8644 |  |
| M01 | Multi-Pump Switching Control Syste | public | medium | ✅ | 3/3 | 2/2 | ✅ | 58 | 32251/3259 |  |
| M02 | Analog Batch Processing | public | medium | ✅ | 3/3 | 2/2 | ✅ | 229 | 455820/14795 |  |
| M03 | Calculate Moving Average | public | medium | ✅ | 0/5 | 0/4 | ❌ | 446 | 763783/29220 |  |
| M04 | Temperature Logic Control | public | medium | ✅ | 4/4 | 3/3 | ✅ | 82 | 34101/5496 |  |
| M05 | Automated Production Line Control | public | medium | ✅ | 2/6 | 1/5 | ❌ | 206 | 145561/14110 |  |
| M06 | Slab Thickness Alarm and Fault His | public | medium | ✅ | 5/5 | 4/4 | ✅ | 526 | 2087901/36895 |  |
| M07 | Office HVAC Multi-mode Energy-Savi | public | medium | ✅ | 3/3 | 2/2 | ✅ | 144 | 113188/8917 |  |
| M08 | IPv4 Parsing with Format and Range | public | medium | ✅ | 4/4 | 3/3 | ✅ | 114 | 61792/7322 |  |
| H01 | Material Proportioning Process Con | public | hard | ✅ | 6/6 | 5/5 | ✅ | 127 | 37686/8314 |  |
| H02 | Flexible Processing Control | public | hard | ✅ | 3/3 | 2/2 | ✅ | 303 | 47624/21430 |  |
| H03 | Recipe Management System | public | hard | ✅ | 3/3 | 2/2 | ✅ | 200 | 429008/13311 |  |
| H04 | FIFO First-In-First-Out Queue | public | hard | ✅ | 0/5 | 0/4 | ❌ | 168 | 48453/11478 |  |
| H05 | Mechanical Arm Control | public | hard | ✅ | 7/7 | 6/6 | ✅ | 188 | 90680/12621 |  |
| H06 | Production Control | public | hard | ✅ | 6/6 | 5/5 | ✅ | 167 | 38908/10698 |  |
| C01 | Product Reject and Filtering Stati | custom | easy | ✅ | 2/2 | 1/1 | ✅ | 177 | 38008/11369 |  |
| C02 | Two-Hand Safety Press | custom | easy | ✅ | 2/2 | 1/1 | ✅ | 55 | 43322/2598 |  |
| C03 | Automatic Barrier Gate | custom | easy | ✅ | 2/2 | 1/1 | ✅ | 80 | 88994/3969 |  |
| C04 | Star-Delta Motor Starter | custom | medium | ✅ | 2/2 | 1/1 | ✅ | 113 | 34430/6977 |  |
| C05 | Car Wash Sequence | custom | medium | ✅ | 2/2 | 1/1 | ✅ | 162 | 73673/10849 |  |
| C06 | Elevator Door Control | custom | medium | ✅ | 3/3 | 2/2 | ✅ | 330 | 233306/21911 |  |
| C07 | Bottle Height Sorting | custom | medium | ✅ | 2/2 | 1/1 | ✅ | 154 | 52498/10088 |  |
| C08 | Greenhouse Irrigation Zones | custom | medium | ✅ | 2/3 | 1/2 | ❌ | 290 | 127759/19117 |  |
| C09 | Conveyor Zone Accumulation | custom | hard | ✅ | 3/3 | 2/2 | ✅ | 93 | 47443/5541 |  |
| C10 | Boiler Purge and Ignition Sequence | custom | hard | ❌ | 0/3 | 0/2 | ❌ | 218 | 67402/14283 | 编译未通过 不能将类型 '未知的类型: '(State = E_C10_STATE#C10_PURGE)'' 转换为类型'BOOL'; 未知 |
| C11 | Palletizer Layer Counting | custom | hard | ✅ | 1/1 | 0/0 | ✅ | 382 | 1137353/23950 |  |
| C12 | Safety Light Curtain Muting | custom | hard | ✅ | 2/3 | 1/2 | ❌ | 380 | 161769/25264 |  |

## 实验 2：Codex CLI × qwen3-coder-flash

| 题目 | 名称 | 来源 | 难度 | 编译 | 用例通过 | held-out | 整题通过 | 用时(s) | tokens(in/out) | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|
| E01 | Automated Filling Line Control | public | easy | ✅ | 0/6 | 0/5 | ❌ | 49 | 0/0 |  |
| E02 | Dual-Word Edge Detection | public | easy | ❌ | 0/4 | 0/3 | ❌ | 51 | 0/0 | 编译未通过 应该用';' 替换'prevValue'; 代码'BEGIN; '不可能执行到.这是有目的的吗？ |
| E03 | Alarm Handling | public | easy | ✅ | 3/5 | 3/4 | ❌ | 62 | 0/0 |  |
| E04 | Jam Pump Debouncing and Runtime Ma | public | easy | ❌ | 0/4 | 0/3 | ❌ | 59 | 0/0 | 编译未通过 应该用';' 替换'IF'; 代码'BEGIN; '不可能执行到.这是有目的的吗？ |
| E05 | Weld Gap Alarm and Startup Inhibit | public | easy | ✅ | 0/3 | 0/2 | ❌ | 74 | 0/0 |  |
| E06 | Aeration Blower Delayed Start | public | easy | ✅ | 0/3 | 0/2 | ❌ | 44 | 0/0 |  |
| M01 | Multi-Pump Switching Control Syste | public | medium | ❌ | 0/3 | 0/2 | ❌ | 60 | 0/0 | 编译未通过 应该用';' 替换'startEdge'; 代码'BEGIN; '不可能执行到.这是有目的的吗？ |
| M02 | Analog Batch Processing | public | medium | ❌ | 0/3 | 0/2 | ❌ | 66 | 0/0 | 编译未通过 应该用';' 替换'FOR'; 代码'BEGIN; '不可能执行到.这是有目的的吗？; 应该用';' 替换')' |
| M03 | Calculate Moving Average | public | medium | ❌ | 0/5 | 0/4 | ❌ | 66 | 0/0 | 编译未通过 未知的类型: 'T_MovingAvg_Buffer'; 应该用表达式代替 '%' |
| M04 | Temperature Logic Control | public | medium | ❌ | 0/4 | 0/3 | ❌ | 40 | 0/0 | 编译未通过 应该用';' 替换'CurrentTemperature'; 代码'BEGIN; '不可能执行到.这是有目的的吗？ |
| M05 | Automated Production Line Control | public | medium | ❌ | 0/6 | 0/5 | ❌ | 72 | 0/0 | 编译未通过 应该用';' 替换'MotorForward'; 代码'BEGIN; '不可能执行到.这是有目的的吗？ |
| M06 | Slab Thickness Alarm and Fault His | public | medium | ❌ | 0/5 | 0/4 | ❌ | 23 | 0/0 | 编译未通过 |
| M07 | Office HVAC Multi-mode Energy-Savi | public | medium | ❌ | 0/3 | 0/2 | ❌ | 118 | 0/0 | 编译未通过 |
| M08 | IPv4 Parsing with Format and Range | public | medium | ❌ | 0/4 | 0/3 | ❌ | 68 | 0/0 | 编译未通过 应该用';' 替换'result'; 代码'BEGIN; '不可能执行到.这是有目的的吗？;  exit没有闭合的循环 |
| H01 | Material Proportioning Process Con | public | hard | ✅ | 2/6 | 1/5 | ❌ | 194 | 0/0 |  |
| H02 | Flexible Processing Control | public | hard | ✅ | 0/3 | 0/2 | ❌ | 81 | 0/0 |  |
| H03 | Recipe Management System | public | hard | ❌ | 0/3 | 0/2 | ❌ | 80 | 0/0 | 编译未通过 应该用';' 替换'recipeAdded'; 代码'BEGIN; '不可能执行到.这是有目的的吗？ |
| H04 | FIFO First-In-First-Out Queue | public | hard | ❌ | 0/5 | 0/4 | ❌ | 208 | 0/0 | 编译未通过 此处需要有类型 'BOOL'的表达式; 未知的类型: 'ARRAY_SIZE(buffer)'; 没有定义标识符'ARRAY_S |
| H05 | Mechanical Arm Control | public | hard | ❌ | 0/7 | 0/6 | ❌ | 479 | 0/0 | 编译未通过 |
| H06 | Production Control | public | hard | ❌ | 0/6 | 0/5 | ❌ | 268 | 0/0 | 编译未通过 |
| C01 | Product Reject and Filtering Stati | custom | easy | ❌ | 0/2 | 0/1 | ❌ | 46 | 0/0 | 编译未通过 应该用';' 替换'partPresent_RisingEdge'; 代码'BEGIN; '不可能执行到.这是有目的的吗？ |
| C02 | Two-Hand Safety Press | custom | easy | ✅ | 0/2 | 0/1 | ❌ | 270 | 0/0 |  |
| C03 | Automatic Barrier Gate | custom | easy | ❌ | 0/2 | 0/1 | ❌ | 64 | 0/0 | 编译未通过 不能将类型 '未知的类型: '(OpenButton AND NOT(OLD(OpenButton)))'' 转换为类型'BOO |
| C04 | Star-Delta Motor Starter | custom | medium | ✅ | 0/2 | 0/1 | ❌ | 115 | 0/0 |  |
| C05 | Car Wash Sequence | custom | medium | ❌ | 0/2 | 0/1 | ❌ | 203 | 0/0 | 编译未通过 |
| C06 | Elevator Door Control | custom | medium | ❌ | 0/3 | 0/2 | ❌ | 410 | 0/0 | 编译未通过 应该用';' 替换'DoorMotorOpen'; 代码'BEGIN; '不可能执行到.这是有目的的吗？ |
| C07 | Bottle Height Sorting | custom | medium | ✅ | 1/2 | 1/1 | ❌ | 95 | 0/0 |  |
| C08 | Greenhouse Irrigation Zones | custom | medium | ❌ | 0/3 | 0/2 | ❌ | 377 | 0/0 | 编译未通过 |
| C09 | Conveyor Zone Accumulation | custom | hard | ❌ | 0/3 | 0/2 | ❌ | 82 | 0/0 | 编译未通过 此处需要有类型 'BOOL'的表达式; 未知的类型: '(Zone1Timer.TON_t > TIME#5s0ms)'; 未知 |
| C10 | Boiler Purge and Ignition Sequence | custom | hard | ✅ | 0/3 | 0/2 | ❌ | 159 | 0/0 |  |
| C11 | Palletizer Layer Counting | custom | hard | ✅ | 0/1 | 0/0 | ❌ | 98 | 0/0 |  |
| C12 | Safety Light Curtain Muting | custom | hard | ❌ | 0/3 | 0/2 | ❌ | 21 | 0/0 | 编译未通过 |
