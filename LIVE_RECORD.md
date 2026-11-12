# 实验结果实时记录（自研 Agent harness）

最后更新：2026-11-12 23:29:39

> 每跑完一道题自动重建本文件。评测口径与 `evaluate.py` 一致：
> 编译结果来自 CODESYS 服务（真实编译），用例结果来自本机仿真器
> `codesys_service/st_sim.py`，所有框架使用同一套用例和判定标准；
> 未通过编译的代码，其用例一律计为未通过。
> 修复阶段 Agent 只能看到每题第 1 个用例（反馈用例），其余为 held-out 用例，仅用于打分。

## 汇总

| 实验 | 模型 | 进度 | 首次编译通过率 | 最终编译通过率 | 用例通过率 | held-out 用例通过率 | 整题通过率 | tokens (in/out) | 用时 (s) |
|---|---|---|---|---|---|---|---|---|---|
| 实验 3 | deepseek-v4-pro-0813 | 29/32 | 26/29 (89.7%) | 27/29 (93.1%) | 95/109 (87.2%) | 68/80 (85.0%) | 22/29 (75.9%) | 57189/447552 | 7315 |
| 实验 4 | qwen3-coder-flash | 32/32 | 10/32 (31.2%) | 20/32 (62.5%) | 21/116 (18.1%) | 13/84 (15.5%) | 3/32 (9.4%) | 163666/59577 | 2182 |

## 实验 3：自研 harness × deepseek-v4-pro-0813

| 题目 | 名称 | 来源 | 难度 | 首次编译 | 最终编译 | 编译修复轮次 | LLM 调用 | 用例通过 | 整题通过 | 用时(s) | tokens(in/out) | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E01 | Automated Filling Line Control | public | easy | ✅ | ✅ | 0 | 2 | 5/6 | ❌ | 289 | 3145/9922 |  |
| E02 | Dual-Word Edge Detection | public | easy | ✅ | ✅ | 0 | 1 | 4/4 | ✅ | 153 | 910/7230 |  |
| E03 | Alarm Handling | public | easy | ✅ | ✅ | 0 | 1 | 5/5 | ✅ | 125 | 921/6168 |  |
| E04 | Jam Pump Debouncing and Runtime Ma | public | easy | ✅ | ✅ | 0 | 1 | 3/4 | ❌ | 340 | 1028/22163 |  |
| E05 | Weld Gap Alarm and Startup Inhibit | public | easy | ✅ | ✅ | 0 | 1 | 3/3 | ✅ | 131 | 942/6823 |  |
| E06 | Aeration Blower Delayed Start | public | easy | ✅ | ✅ | 0 | 1 | 3/3 | ✅ | 77 | 894/3168 |  |
| M01 | Multi-Pump Switching Control Syste | public | medium | ✅ | ✅ | 0 | 1 | 3/3 | ✅ | 129 | 959/6381 |  |
| M02 | Analog Batch Processing | public | medium | ✅ | ✅ | 0 | 1 | 3/3 | ✅ | 108 | 1301/5367 |  |
| M03 | Calculate Moving Average | public | medium | ✅ | ✅ | 0 | 1 | 5/5 | ✅ | 186 | 999/11242 |  |
| M04 | Temperature Logic Control | public | medium | ✅ | ✅ | 0 | 1 | 4/4 | ✅ | 195 | 955/12571 |  |
| M05 | Automated Production Line Control | public | medium | ✅ | ✅ | 0 | 1 | 4/6 | ❌ | 317 | 1221/13920 |  |
| M06 | Slab Thickness Alarm and Fault His | public | medium | ✅ | ✅ | 0 | 1 | 2/5 | ❌ | 440 | 1205/28728 |  |
| M07 | Office HVAC Multi-mode Energy-Savi | public | medium | ❌ | ❌ | – | 4 | 0/3 | ❌ | 501 | 7420/31564 | 编译未通过 期望 ':='，实际是 'SUPPLY_FAN_RUN' |
| M08 | IPv4 Parsing with Format and Range | public | medium | ❌ | ✅ | 2 | 3 | 4/4 | ✅ | 253 | 4074/16697 |  |
| H01 | Material Proportioning Process Con | public | hard | ✅ | ✅ | 0 | 1 | 6/6 | ✅ | 302 | 1376/19685 |  |
| H02 | Flexible Processing Control | public | hard | ❌ | ❌ | – | 4 | 0/3 | ❌ | 638 | 12150/41410 | 编译未通过 期望 ':='，实际是 'edgeStart' |
| H03 | Recipe Management System | public | hard | ✅ | ✅ | 0 | 1 | 3/3 | ✅ | 185 | 1635/10987 |  |
| H04 | FIFO First-In-First-Out Queue | public | hard | ✅ | ✅ | 0 | 2 | 5/5 | ✅ | 216 | 3072/13057 |  |
| H05 | Mechanical Arm Control | public | hard | ✅ | ✅ | 0 | 1 | 7/7 | ✅ | 285 | 1768/19222 |  |
| H06 | Production Control | public | hard | ✅ | ✅ | 0 | 1 | 6/6 | ✅ | 238 | 1561/15830 |  |
| C01 | Product Reject and Filtering Stati | custom | easy | ✅ | ✅ | 0 | 1 | 2/2 | ✅ | 271 | 979/18654 |  |
| C02 | Two-Hand Safety Press | custom | easy | ✅ | ✅ | 0 | 1 | 2/2 | ✅ | 153 | 870/9332 |  |
| C03 | Automatic Barrier Gate | custom | easy | ✅ | ✅ | 0 | 2 | 2/2 | ✅ | 208 | 1993/11105 |  |
| C04 | Star-Delta Motor Starter | custom | medium | ✅ | ✅ | 0 | 1 | 2/2 | ✅ | 147 | 889/9020 |  |
| C05 | Car Wash Sequence | custom | medium | ✅ | ✅ | 0 | 1 | 2/2 | ✅ | 306 | 953/21471 |  |
| C06 | Elevator Door Control | custom | medium | ✅ | ✅ | 0 | 1 | 3/3 | ✅ | 250 | 990/16644 |  |
| C07 | Bottle Height Sorting | custom | medium | ✅ | ✅ | 0 | 1 | 2/2 | ✅ | 370 | 950/25040 |  |
| C08 | Greenhouse Irrigation Zones | custom | medium | ✅ | ✅ | 0 | 1 | 2/3 | ❌ | 286 | 971/19925 |  |
| C09 | Conveyor Zone Accumulation | custom | hard | ✅ | ✅ | 0 | 1 | 3/3 | ✅ | 216 | 1058/14226 |  |
| C10 | Boiler Purge and Ignition Sequence | custom | hard | | | | | | ⏳ 未运行 | | | |
| C11 | Palletizer Layer Counting | custom | hard | | | | | | ⏳ 未运行 | | | |
| C12 | Safety Light Curtain Muting | custom | hard | | | | | | ⏳ 未运行 | | | |

## 实验 4：自研 harness × qwen3-coder-flash

| 题目 | 名称 | 来源 | 难度 | 首次编译 | 最终编译 | 编译修复轮次 | LLM 调用 | 用例通过 | 整题通过 | 用时(s) | tokens(in/out) | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E01 | Automated Filling Line Control | public | easy | ❌ | ✅ | 1 | 3 | 0/6 | ❌ | 76 | 5572/2133 |  |
| E02 | Dual-Word Edge Detection | public | easy | ❌ | ❌ | – | 4 | 0/4 | ❌ | 82 | 6413/1686 | 编译未通过 无法解析的表达式片段 '<' |
| E03 | Alarm Handling | public | easy | ❌ | ✅ | 2 | 4 | 3/5 | ❌ | 81 | 6099/1438 |  |
| E04 | Jam Pump Debouncing and Runtime Ma | public | easy | ✅ | ✅ | 0 | 4 | 0/4 | ❌ | 104 | 6789/1516 |  |
| E05 | Weld Gap Alarm and Startup Inhibit | public | easy | ✅ | ✅ | 0 | 1 | 3/3 | ✅ | 26 | 830/276 |  |
| E06 | Aeration Blower Delayed Start | public | easy | ✅ | ✅ | 0 | 1 | 3/3 | ✅ | 25 | 781/275 |  |
| M01 | Multi-Pump Switching Control Syste | public | medium | ❌ | ❌ | – | 3 | 0/3 | ❌ | 72 | 4675/1661 | 编译未通过 期望 ':='，实际是 'bStartRisingEdge' |
| M02 | Analog Batch Processing | public | medium | ❌ | ❌ | – | 3 | 0/3 | ❌ | 40 | 6122/1840 | 编译未通过 期望 ':='，实际是 'FOR' |
| M03 | Calculate Moving Average | public | medium | ❌ | ❌ | – | 4 | 0/5 | ❌ | 103 | 8271/2468 | 编译未通过  |
| M04 | Temperature Logic Control | public | medium | ❌ | ✅ | 2 | 3 | 3/4 | ❌ | 87 | 4596/1644 |  |
| M05 | Automated Production Line Control | public | medium | ✅ | ✅ | 0 | 4 | 1/6 | ❌ | 100 | 10637/3489 |  |
| M06 | Slab Thickness Alarm and Fault His | public | medium | ❌ | ❌ | – | 4 | 0/5 | ❌ | 90 | 9020/2308 | 编译未通过  |
| M07 | Office HVAC Multi-mode Energy-Savi | public | medium | ❌ | ❌ | – | 2 | 0/3 | ❌ | 37 | 2499/1178 | 编译未通过 期望 ':='，实际是 'IF' |
| M08 | IPv4 Parsing with Format and Range | public | medium | ❌ | ❌ | – | 4 | 0/4 | ❌ | 115 | 7534/2657 | 编译未通过 TypeError: '>=' not supported between instances of 'in |
| H01 | Material Proportioning Process Con | public | hard | ❌ | ✅ | 1 | 3 | 1/6 | ❌ | 111 | 8067/4053 |  |
| H02 | Flexible Processing Control | public | hard | ❌ | ✅ | 1 | 2 | 1/3 | ❌ | 59 | 3262/1602 |  |
| H03 | Recipe Management System | public | hard | ✅ | ✅ | 0 | 1 | 3/3 | ✅ | 30 | 1550/815 |  |
| H04 | FIFO First-In-First-Out Queue | public | hard | ❌ | ❌ | – | 2 | 0/5 | ❌ | 30 | 2749/782 | 编译未通过 期望 ':='，实际是 'IF' |
| H05 | Mechanical Arm Control | public | hard | ❌ | ❌ | – | 2 | 0/7 | ❌ | 35 | 5163/3600 | 编译未通过 控制结构缺少结束标记 ELSE/ELSIF/END_IF |
| H06 | Production Control | public | hard | ✅ | ✅ | 0 | 1 | 1/6 | ❌ | 33 | 1481/1177 |  |
| C01 | Product Reject and Filtering Stati | custom | easy | ❌ | ✅ | 1 | 4 | 0/2 | ❌ | 121 | 6444/1595 |  |
| C02 | Two-Hand Safety Press | custom | easy | ❌ | ✅ | 1 | 4 | 1/2 | ❌ | 104 | 6985/2159 |  |
| C03 | Automatic Barrier Gate | custom | easy | ✅ | ✅ | 0 | 4 | 0/2 | ❌ | 83 | 6446/1834 |  |
| C04 | Star-Delta Motor Starter | custom | medium | ❌ | ❌ | – | 2 | 0/2 | ❌ | 38 | 2217/1074 | 编译未通过 期望 ':='，实际是 'startRisingEdge' |
| C05 | Car Wash Sequence | custom | medium | ✅ | ✅ | 0 | 3 | 0/2 | ❌ | 82 | 5075/2143 |  |
| C06 | Elevator Door Control | custom | medium | ❌ | ✅ | 1 | 4 | 0/3 | ❌ | 101 | 9692/3640 |  |
| C07 | Bottle Height Sorting | custom | medium | ❌ | ❌ | – | 3 | 0/2 | ❌ | 62 | 4459/1634 | 编译未通过  |
| C08 | Greenhouse Irrigation Zones | custom | medium | ❌ | ✅ | 1 | 4 | 0/3 | ❌ | 94 | 9440/3004 |  |
| C09 | Conveyor Zone Accumulation | custom | hard | ❌ | ❌ | – | 2 | 0/3 | ❌ | 22 | 2893/1828 | 编译未通过 期望 ':='，实际是 'MAX_RUN_TIME' |
| C10 | Boiler Purge and Ignition Sequence | custom | hard | ✅ | ✅ | 0 | 2 | 0/3 | ❌ | 43 | 3064/2236 |  |
| C11 | Palletizer Layer Counting | custom | hard | ❌ | ✅ | 1 | 3 | 0/1 | ❌ | 57 | 3987/1365 |  |
| C12 | Safety Light Curtain Muting | custom | hard | ✅ | ✅ | 0 | 1 | 1/3 | ❌ | 42 | 854/467 |  |
