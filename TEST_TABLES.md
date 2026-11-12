# 测试用例执行记录（按《测试用例模板与示例》）

最后更新：2026-11-12 23:29:39

> 每个用例给出：用例名称、所属题目、初始状态、覆盖内容，以及逐扫描周期的
> 输入、预期输出、**实际输出**和判定结果。同一题在不同模型下使用完全相同的用例与判定标准。

# deepseek-v4-pro-0813（model_a）

## E01 Automated Filling Line Control（`E01_Filling`）

- 编译：通过；用例通过 5/6；整题未通过

### TC01 Full production cycle

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Full production cycle |
| 所属题目 | E01 Automated Filling Line Control（`E01_Filling`） |
| 初始状态 | power-up, all inputs FALSE, all outputs FALSE |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | power-up idle, every step transition, exactly one actuator active per step, outputs stay latched after the trigger is released, light reset by finishedButton |
| 实际输出及结果 | ✅ 通过 |

| 周期 | bottleSensor | cleaningConfirmButton | fillingConfirmButton | cappingConfirmButton | packingConfirmButton | finishedButton | 预期 Pump_Motor | 预期 Filling_Valve | 预期 Capping_Machine | 预期 Packing_Machine | 预期 Completion_Light | 实际 Pump_Motor | 实际 Filling_Valve | 实际 Capping_Machine | 实际 Packing_Machine | 实际 Completion_Light | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | idle: all outputs OFF | PASS |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | bottle detected -> pump ON | PASS |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | sensor released, pump keeps running | PASS |
| 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | cleaning confirmed -> pump OFF, valve ON | PASS |
| 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | button released, valve stays ON | PASS |
| 5 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | filling confirmed -> valve OFF, capping ON | PASS |
| 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | capping stays ON | PASS |
| 7 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | capping confirmed -> capping OFF, packing ON | PASS |
| 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | packing stays ON | PASS |
| 9 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | packing confirmed -> packing OFF, light ON | PASS |
| 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | light stays ON while waiting for pickup | PASS |
| 11 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | finishedButton -> light OFF, back to idle | PASS |
| 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | idle again, all OFF | PASS |

### TC02 Second cycle after reset

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Second cycle after reset |
| 所属题目 | E01 Automated Filling Line Control（`E01_Filling`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | the line is ready for the next bottle after finishedButton |
| 实际输出及结果 | ✅ 通过 |

| 周期 | bottleSensor | cleaningConfirmButton | fillingConfirmButton | cappingConfirmButton | packingConfirmButton | finishedButton | 预期 Pump_Motor | 预期 Filling_Valve | 预期 Capping_Machine | 预期 Packing_Machine | 预期 Completion_Light | 实际 Pump_Motor | 实际 Filling_Valve | 实际 Capping_Machine | 实际 Packing_Machine | 实际 Completion_Light | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | cycle 1: pump ON | PASS |
| 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | to filling | PASS |
| 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | to capping | PASS |
| 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | to packing | PASS |
| 4 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | to done | PASS |
| 5 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | reset | PASS |
| 6 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | cycle 2: next bottle starts the pump again | PASS |
| 7 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | cycle 2 continues normally | PASS |

### TC03 Out-of-sequence buttons are ignored

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Out-of-sequence buttons are ignored |
| 所属题目 | E01 Automated Filling Line Control（`E01_Filling`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | confirm buttons only act in their own step; finishedButton has no effect before completion; no actuator starts in idle without a bottle |
| 实际输出及结果 | ✅ 通过 |

| 周期 | bottleSensor | cleaningConfirmButton | fillingConfirmButton | cappingConfirmButton | packingConfirmButton | finishedButton | 预期 Pump_Motor | 预期 Filling_Valve | 预期 Capping_Machine | 预期 Packing_Machine | 预期 Completion_Light | 实际 Pump_Motor | 实际 Filling_Valve | 实际 Capping_Machine | 实际 Packing_Machine | 实际 Completion_Light | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | idle: buttons without a bottle do nothing | PASS |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | bottle -> cleaning | PASS |
| 2 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | fillingConfirm during cleaning is ignored | PASS |
| 3 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | packingConfirm during cleaning is ignored | PASS |
| 4 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | finishedButton during cleaning is ignored | PASS |
| 5 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | correct button advances to filling | PASS |
| 6 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | repeated cleaningConfirm in filling is ignored | PASS |
| 7 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | cappingConfirm during filling is ignored | PASS |
| 8 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | correct button advances to capping | PASS |

### TC04 Completion light waits for pickup

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Completion light waits for pickup |
| 所属题目 | E01 Automated Filling Line Control（`E01_Filling`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | light stays ON until finishedButton; a new bottle signal or other buttons do not clear it |
| 实际输出及结果 | ✅ 通过 |

| 周期 | bottleSensor | cleaningConfirmButton | fillingConfirmButton | cappingConfirmButton | packingConfirmButton | finishedButton | 预期 Pump_Motor | 预期 Filling_Valve | 预期 Capping_Machine | 预期 Packing_Machine | 预期 Completion_Light | 实际 Pump_Motor | 实际 Filling_Valve | 实际 Capping_Machine | 实际 Packing_Machine | 实际 Completion_Light | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | start | PASS |
| 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |  | PASS |
| 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |  | PASS |
| 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |  | PASS |
| 4 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | light ON | PASS |
| 5 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | packingConfirm held: light stays ON | PASS |
| 6 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | other confirm buttons do not clear the light | PASS |
| 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | still ON | PASS |
| 8 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | only finishedButton clears the light | PASS |

### TC05 A confirm button held in advance does not skip a step

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC05 A confirm button held in advance does not skip a step |
| 所属题目 | E01 Automated Filling Line Control（`E01_Filling`） |
| 初始状态 | power-up: step 0, all actuators off |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | edge-triggered confirmation: a button already held when its step is reached must not advance it; a fresh rising edge is required |
| 实际输出及结果 | ✅ 通过 |

| 周期 | bottleSensor | cleaningConfirmButton | fillingConfirmButton | cappingConfirmButton | packingConfirmButton | finishedButton | 预期 Pump_Motor | 预期 Filling_Valve | 预期 Capping_Machine | 预期 Packing_Machine | 预期 Completion_Light | 实际 Pump_Motor | 实际 Filling_Valve | 实际 Capping_Machine | 实际 Packing_Machine | 实际 Completion_Light | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | confirm pressed early, no bottle yet: nothing happens | PASS |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |  |  |  | 1 | 0 |  |  |  | DECISIVE: bottle arrives while the confirm button is already held. The cleaning step must be entered and must NOT be confirmed in the same scan, because the button has no rising edge | PASS |
| 2 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |  |  |  | 1 | 0 |  |  |  | still held: still cleaning | PASS |
| 3 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  | 1 |  |  |  |  | released: still cleaning | PASS |
| 4 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  | 0 | 1 |  |  |  | a fresh rising edge confirms cleaning -> filling | PASS |
| 5 | 1 | 1 | 0 | 0 | 0 | 0 |  | 1 | 0 |  |  |  | 1 | 0 |  |  | held again: filling is not confirmed by the stale press | PASS |

### TC06 A bottle that stays under the sensor does not restart the line

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC06 A bottle that stays under the sensor does not restart the line |
| 所属题目 | E01 Automated Filling Line Control（`E01_Filling`） |
| 初始状态 | power-up: idle, all actuators off |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | sensor held TRUE for many cycles: the latch must survive, the sensor must not re-trigger cleaning after the bottle has been processed, and a second bottle arriving later starts a new cycle |
| 实际输出及结果 | ❌ 不通过；周期 9：Pump_Motor 预期 0，实际 True；周期 10：Pump_Motor 预期 0，实际 True |

| 周期 | bottleSensor | cleaningConfirmButton | fillingConfirmButton | cappingConfirmButton | packingConfirmButton | finishedButton | 预期 Pump_Motor | 预期 Filling_Valve | 预期 Capping_Machine | 预期 Packing_Machine | 预期 Completion_Light | 实际 Pump_Motor | 实际 Filling_Valve | 实际 Capping_Machine | 实际 Packing_Machine | 实际 Completion_Light | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  | 1 |  |  |  |  | bottle arrives -> cleaning starts | PASS |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  | 1 |  |  |  |  | sensor still TRUE: the latch holds, no repeated start | PASS |
| 2 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  | 1 |  |  |  |  | sensor still TRUE: still the same cleaning step | PASS |
| 3 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  | 0 | 1 |  |  |  | cleaning confirmed while the bottle is still under the sensor | PASS |
| 4 | 1 | 0 | 0 | 0 | 0 | 0 |  | 1 |  |  |  |  | 1 |  |  |  | sensor still TRUE and cleaning is over: the line must NOT go back to cleaning, the bottle is the same one | PASS |
| 5 | 1 | 0 | 1 | 0 | 0 | 0 |  | 0 | 1 |  |  |  | 0 | 1 |  |  | filling confirmed | PASS |
| 6 | 1 | 0 | 0 | 1 | 0 | 0 |  |  | 0 | 1 |  |  |  | 0 | 1 |  | capping confirmed | PASS |
| 7 | 1 | 0 | 0 | 0 | 1 | 0 |  |  |  | 0 | 1 |  |  |  | 0 | 1 | packing confirmed | PASS |
| 8 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |  |  |  | 0 | 0 |  |  |  | 0 | bottle picked up while the sensor still reads TRUE: back to idle and the stale sensor level must not start a new cycle, because there is no rising edge | PASS |
| 9 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  | 1 |  |  |  |  | sensor still TRUE, idle: nothing starts without a new rising edge | FAIL |
| 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  | 1 |  |  |  |  | bottle removed: sensor FALSE | FAIL |
| 11 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  | 1 |  |  |  |  | a second bottle gives a fresh rising edge: a new cycle starts | PASS |


## E02 Dual-Word Edge Detection（`E02_DualEdge`）

- 编译：通过；用例通过 4/4；整题通过

### TC01 Single-bit rising and falling edges

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Single-bit rising and falling edges |
| 所属题目 | E02 Dual-Word Edge Detection（`E02_DualEdge`） |
| 初始状态 | power-up, previous value treated as 0 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | first invocation, one bit set, one bit cleared, no change |
| 实际输出及结果 | ✅ 通过 |

| 周期 | value | 预期 hasChanged | 预期 hasRisingEdges | 预期 risingBits | 预期 noOfRisingBits | 预期 hasFallingEdges | 预期 fallingBits | 预期 noOfFallingBits | 实际 hasChanged | 实际 hasRisingEdges | 实际 risingBits | 实际 noOfRisingBits | 实际 hasFallingEdges | 实际 fallingBits | 实际 noOfFallingBits | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | no change from the initial zero value | PASS |
| 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | bit0 rises | PASS |
| 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | unchanged -> no edges | PASS |
| 3 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | bit0 falls | PASS |
| 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | unchanged | PASS |

### TC02 Multiple simultaneous edges

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Multiple simultaneous edges |
| 所属题目 | E02 Dual-Word Edge Detection（`E02_DualEdge`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | several bits rise and fall in the same cycle, counts are correct |
| 实际输出及结果 | ✅ 通过 |

| 周期 | value | 预期 hasChanged | 预期 hasRisingEdges | 预期 risingBits | 预期 noOfRisingBits | 预期 hasFallingEdges | 预期 fallingBits | 预期 noOfFallingBits | 实际 hasChanged | 实际 hasRisingEdges | 实际 risingBits | 实际 noOfRisingBits | 实际 hasFallingEdges | 实际 fallingBits | 实际 noOfFallingBits | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 15 | 1 | 1 | 15 | 4 | 0 | 0 | 0 | 1 | 1 | 15 | 4 | 0 | 0 | 0 | four bits rise at once | PASS |
| 1 | 240 | 1 | 1 | 240 | 4 | 1 | 15 | 4 | 1 | 1 | 240 | 4 | 1 | 15 | 4 | four rise and four fall in the same cycle | PASS |
| 2 | 255 | 1 | 1 | 15 | 4 | 0 | 0 | 0 | 1 | 1 | 15 | 4 | 0 | 0 | 0 | four more rise, none fall | PASS |
| 3 | 0 | 1 | 0 | 0 | 0 | 1 | 255 | 8 | 1 | 0 | 0 | 0 | 1 | 255 | 8 | all eight fall | PASS |

### TC03 Boundary bits and full word

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Boundary bits and full word |
| 所属题目 | E02 Dual-Word Edge Detection（`E02_DualEdge`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | bit31 (most significant), all 32 bits at once, maximum counts |
| 实际输出及结果 | ✅ 通过 |

| 周期 | value | 预期 hasChanged | 预期 hasRisingEdges | 预期 risingBits | 预期 noOfRisingBits | 预期 hasFallingEdges | 预期 fallingBits | 预期 noOfFallingBits | 实际 hasChanged | 实际 hasRisingEdges | 实际 risingBits | 实际 noOfRisingBits | 实际 hasFallingEdges | 实际 fallingBits | 实际 noOfFallingBits | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 2147483648 | 1 | 1 | 2147483648 | 1 | 0 | 0 | 0 | 1 | 1 | 2147483648 | 1 | 0 | 0 | 0 | bit31 rises | PASS |
| 1 | 4294967295 | 1 | 1 | 2147483647 | 31 | 0 | 0 | 0 | 1 | 1 | 2147483647 | 31 | 0 | 0 | 0 | the remaining 31 bits rise, count 31 | PASS |
| 2 | 4294967295 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | unchanged | PASS |
| 3 | 0 | 1 | 0 | 0 | 0 | 1 | 4294967295 | 32 | 1 | 0 | 0 | 0 | 1 | 4294967295 | 32 | all 32 bits fall, count 32 | PASS |
| 4 | 4294967295 | 1 | 1 | 4294967295 | 32 | 0 | 0 | 0 | 1 | 1 | 4294967295 | 32 | 0 | 0 | 0 | all 32 bits rise, count 32 | PASS |

### TC04 Alternating patterns

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Alternating patterns |
| 所属题目 | E02 Dual-Word Edge Detection（`E02_DualEdge`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | interleaved bit patterns, rising and falling masks are disjoint |
| 实际输出及结果 | ✅ 通过 |

| 周期 | value | 预期 hasChanged | 预期 hasRisingEdges | 预期 risingBits | 预期 noOfRisingBits | 预期 hasFallingEdges | 预期 fallingBits | 预期 noOfFallingBits | 实际 hasChanged | 实际 hasRisingEdges | 实际 risingBits | 实际 noOfRisingBits | 实际 hasFallingEdges | 实际 fallingBits | 实际 noOfFallingBits | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 2863311530 | 1 | 1 | 2863311530 | 16 | 0 | 0 | 0 | 1 | 1 | 2863311530 | 16 | 0 | 0 | 0 | 16 odd bits rise | PASS |
| 1 | 1431655765 | 1 | 1 | 1431655765 | 16 | 1 | 2863311530 | 16 | 1 | 1 | 1431655765 | 16 | 1 | 2863311530 | 16 | 16 rise, 16 fall simultaneously | PASS |
| 2 | 1431655765 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | unchanged | PASS |
| 3 | 1431633920 | 1 | 0 | 0 | 0 | 1 | 21845 | 8 | 1 | 0 | 0 | 0 | 1 | 21845 | 8 | upper half kept, lower half falls | PASS |


## E03 Alarm Handling（`E03_Hysteresis`）

- 编译：通过；用例通过 5/5；整题通过

### TC01 High alarm with hysteresis

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 High alarm with hysteresis |
| 所属题目 | E03 Alarm Handling（`E03_Hysteresis`） |
| 初始状态 | power-up, all outputs FALSE/0; hiLevel=80, loLevel=20, hystWindow=5 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | trigger above hiLevel, hold inside window, boundary Value=hiLevel-hystWindow, release, Value=hiLevel does not trigger |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Value | hiLevel | loLevel | hystWindow | 预期 hiAlarm | 预期 loAlarm | 预期 error | 预期 status | 实际 hiAlarm | 实际 loAlarm | 实际 error | 实际 status | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 50 | 80 | 20 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | normal range, no alarm | PASS |
| 1 | 85 | 80 | 20 | 5 | 1 | 0 |  |  | 1 | 0 |  |  | Value>hiLevel triggers hiAlarm | PASS |
| 2 | 78 | 80 | 20 | 5 | 1 |  |  |  | 1 |  |  |  | inside hysteresis window, alarm held | PASS |
| 3 | 75 | 80 | 20 | 5 | 1 |  |  |  | 1 |  |  |  | Value=hiLevel-hystWindow is not < 75, alarm held | PASS |
| 4 | 74 | 80 | 20 | 5 | 0 |  |  |  | 0 |  |  |  | Value<hiLevel-hystWindow releases hiAlarm | PASS |
| 5 | 80 | 80 | 20 | 5 | 0 |  |  |  | 0 |  |  |  | Value=hiLevel is not > hiLevel, no re-trigger | PASS |
| 6 | 81 | 80 | 20 | 5 | 1 |  |  |  | 1 |  |  |  | Value>hiLevel re-triggers | PASS |

### TC02 Low alarm with hysteresis

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Low alarm with hysteresis |
| 所属题目 | E03 Alarm Handling（`E03_Hysteresis`） |
| 初始状态 | power-up; hiLevel=80, loLevel=20, hystWindow=5 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | trigger below loLevel, hold inside window, boundary Value=loLevel+hystWindow, release, Value=loLevel does not trigger |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Value | hiLevel | loLevel | hystWindow | 预期 hiAlarm | 预期 loAlarm | 预期 error | 预期 status | 实际 hiAlarm | 实际 loAlarm | 实际 error | 实际 status | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 50 | 80 | 20 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | normal range | PASS |
| 1 | 15 | 80 | 20 | 5 | 0 | 1 |  |  | 0 | 1 |  |  | Value<loLevel triggers loAlarm | PASS |
| 2 | 22 | 80 | 20 | 5 |  | 1 |  |  |  | 1 |  |  | inside window, alarm held | PASS |
| 3 | 25 | 80 | 20 | 5 |  | 1 |  |  |  | 1 |  |  | Value=loLevel+hystWindow is not > 25, alarm held | PASS |
| 4 | 26 | 80 | 20 | 5 |  | 0 |  |  |  | 0 |  |  | Value>loLevel+hystWindow releases loAlarm | PASS |
| 5 | 20 | 80 | 20 | 5 |  | 0 |  |  |  | 0 |  |  | Value=loLevel is not < loLevel, no re-trigger | PASS |
| 6 | 19 | 80 | 20 | 5 |  | 1 |  |  |  | 1 |  |  | Value<loLevel re-triggers | PASS |

### TC03 Error 16#8001: loLevel >= hiLevel

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Error 16#8001: loLevel >= hiLevel |
| 所属题目 | E03 Alarm Handling（`E03_Hysteresis`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | loLevel>hiLevel, loLevel=hiLevel boundary, 8001 has priority over 8002 |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Value | hiLevel | loLevel | hystWindow | 预期 error | 预期 status | 实际 error | 实际 status | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 50 | 20 | 80 | 5 | 1 | 32769 | 1 | 32769 | loLevel>hiLevel -> 16#8001 | PASS |
| 1 | 50 | 50 | 50 | 5 | 1 | 32769 | 1 | 32769 | loLevel=hiLevel -> 16#8001 | PASS |
| 2 | 50 | 20 | 80 | 100 | 1 | 32769 | 1 | 32769 | both conditions violated: 16#8001 takes priority | PASS |

### TC04 Error 16#8002: hysteresis window too large

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Error 16#8002: hysteresis window too large |
| 所属题目 | E03 Alarm Handling（`E03_Hysteresis`） |
| 初始状态 | power-up; hiLevel=80, loLevel=20 (range 60) |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | hystWindow > range, hystWindow = range boundary, hystWindow just below range is valid |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Value | hiLevel | loLevel | hystWindow | 预期 error | 预期 status | 实际 error | 实际 status | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 50 | 80 | 20 | 70 | 1 | 32770 | 1 | 32770 | hystWindow>60 -> 16#8002 | PASS |
| 1 | 50 | 80 | 20 | 60 | 1 | 32770 | 1 | 32770 | hystWindow=60 (boundary) -> 16#8002 | PASS |
| 2 | 50 | 80 | 20 | 59 | 0 | 0 | 0 | 0 | hystWindow=59 is valid | PASS |

### TC05 Recovery after parameter error

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC05 Recovery after parameter error |
| 所属题目 | E03 Alarm Handling（`E03_Hysteresis`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | error clears when parameters are corrected, alarm logic works again |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Value | hiLevel | loLevel | hystWindow | 预期 error | 预期 status | 预期 hiAlarm | 预期 loAlarm | 实际 error | 实际 status | 实际 hiAlarm | 实际 loAlarm | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 50 | 20 | 80 | 5 | 1 | 32769 |  |  | 1 | 32769 |  |  | invalid limits | PASS |
| 1 | 50 | 80 | 20 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | limits corrected, error cleared | PASS |
| 2 | 90 | 80 | 20 | 5 | 0 | 0 | 1 |  | 0 | 0 | 1 |  | alarm logic active again | PASS |


## E04 Jam Pump Debouncing and Runtime Maintenance（`E04_JamPump`）

- 编译：通过；用例通过 3/4；整题未通过

### TC01 Debounce before the pump may run

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Debounce before the pump may run |
| 所属题目 | E04 Jam Pump Debouncing and Runtime Maintenance（`E04_JamPump`） |
| 初始状态 | power-up: VFD_RUN FALSE, runtime 0, maintenance FALSE; DebounceTime=1000ms |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | power-up state, viscosity held shorter than DebounceTime, run after the full debounce |
| 实际输出及结果 | ✅ 通过 |

| 周期 | VISCOSITY_OK | PASTE_E_STOP_NC | DebounceTime | CycleTime | 预期 VFD_RUN | 预期 PUMP_MAINT_DUE | 预期 PUMP_RUNTIME_ACC | 实际 VFD_RUN | 实际 PUMP_MAINT_DUE | 实际 PUMP_RUNTIME_ACC | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 1000 | 100 | 0 | 0 | 0 | 0 | 0 | 0 | power-up: everything off | PASS |
| 1（保持 800 ms） | 1 | 1 | 1000 | 100 | 0 |  |  | 0 |  |  | viscosity valid, debounce running | PASS |
| 2（保持 400 ms） | 1 | 1 | 1000 | 100 | 1 |  |  | 1 |  |  | full DebounceTime elapsed -> pump runs | PASS |
| 3（保持 200 ms） | 1 | 1 | 1000 | 100 | 1 |  |  | 1 |  |  | keeps running | PASS |

### TC02 Viscosity loss stops the pump and clears timing

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Viscosity loss stops the pump and clears timing |
| 所属题目 | E04 Jam Pump Debouncing and Runtime Maintenance（`E04_JamPump`） |
| 初始状态 | power-up; DebounceTime=1000ms |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | FALSE stops the pump immediately, debounce restarts from zero |
| 实际输出及结果 | ✅ 通过 |

| 周期 | VISCOSITY_OK | PASTE_E_STOP_NC | DebounceTime | CycleTime | 预期 VFD_RUN | 实际 VFD_RUN | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|
| 0（保持 1200 ms） | 1 | 1 | 1000 | 100 | 1 | 1 | running after the debounce | PASS |
| 1 | 0 | 1 | 1000 | 100 | 0 | 0 | viscosity lost -> stop immediately | PASS |
| 2（保持 500 ms） | 1 | 1 | 1000 | 100 | 0 | 0 | new demand: not yet debounced | PASS |
| 3（保持 600 ms） | 1 | 1 | 1000 | 100 | 1 | 1 | full debounce again -> running | PASS |

### TC03 Emergency stop has priority and clears debounce timing

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Emergency stop has priority and clears debounce timing |
| 所属题目 | E04 Jam Pump Debouncing and Runtime Maintenance（`E04_JamPump`） |
| 初始状态 | power-up; DebounceTime=1000ms |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | e-stop stops the pump, blocks starting, requires a full debounce after release |
| 实际输出及结果 | ❌ 不通过；周期 3：VFD_RUN 预期 0，实际 True |

| 周期 | VISCOSITY_OK | PASTE_E_STOP_NC | DebounceTime | CycleTime | 预期 VFD_RUN | 实际 VFD_RUN | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|
| 0（保持 1200 ms） | 1 | 1 | 1000 | 100 | 1 | 1 | running | PASS |
| 1 | 1 | 0 | 1000 | 100 | 0 | 0 | E-STOP -> stop immediately | PASS |
| 2（保持 1500 ms） | 1 | 0 | 1000 | 100 | 0 | 0 | cannot start while the e-stop is active | PASS |
| 3 | 1 | 1 | 1000 | 100 | 0 | 1 | released: debounce was cleared | FAIL |
| 4（保持 1100 ms） | 1 | 1 | 1000 | 100 | 1 | 1 | full debounce -> running again | PASS |

### TC04 Runtime accumulation and the maintenance indication

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Runtime accumulation and the maintenance indication |
| 所属题目 | E04 Jam Pump Debouncing and Runtime Maintenance（`E04_JamPump`） |
| 初始状态 | power-up; DebounceTime=0ms, CycleTime=100h per invocation |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | runtime accumulates only while running, preserved while stopped, flag at 500 h, flag does not affect the pump |
| 实际输出及结果 | ✅ 通过 |

| 周期 | VISCOSITY_OK | PASTE_E_STOP_NC | DebounceTime | CycleTime | 预期 VFD_RUN | 预期 PUMP_RUNTIME_ACC | 预期 PUMP_MAINT_DUE | 实际 VFD_RUN | 实际 PUMP_RUNTIME_ACC | 实际 PUMP_MAINT_DUE | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 360000000 | 1 | 360000000 | 0 | 1 | 360000000 | 0 | 100h | PASS |
| 1 | 1 | 1 | 0 | 360000000 |  | 720000000 | 0 |  | 720000000 | 0 | 200h | PASS |
| 2 | 0 | 1 | 0 | 360000000 | 0 | 720000000 |  | 0 | 720000000 |  | stopped -> runtime preserved | PASS |
| 3 | 1 | 1 | 0 | 360000000 | 1 | 1080000000 |  | 1 | 1080000000 |  | 300h | PASS |
| 4 | 1 | 1 | 0 | 360000000 |  | 1440000000 | 0 |  | 1440000000 | 0 | 400h: still below | PASS |
| 5 | 1 | 1 | 0 | 360000000 |  | 1800000000 | 1 |  | 1800000000 | 1 | 500h -> maintenance due | PASS |
| 6 | 1 | 1 | 0 | 360000000 | 1 |  | 1 | 1 |  | 1 | flag does not affect the pump | PASS |


## E05 Weld Gap Alarm and Startup Inhibition（`E05_WeldGap`）

- 编译：通过；用例通过 3/3；整题通过

### TC01 Power-up inhibition period

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Power-up inhibition period |
| 所属题目 | E05 Weld Gap Alarm and Startup Inhibition（`E05_WeldGap`） |
| 初始状态 | power-up, Weld_E_Stop_NC=1, DebounceTime=200ms |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | soft-start active for 5s, alarm suppressed during inhibition, debounce does not accumulate, monitoring resumes afterwards |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Gap_Exceeded | Weld_E_Stop_NC | DebounceTime | 预期 Operator_Alert | 预期 Weld_Soft_Start_Active | 实际 Operator_Alert | 实际 Weld_Soft_Start_Active | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 200 | 0 | 1 | 0 | 1 | power-up: inhibition active | PASS |
| 1（保持 3000 ms） | 1 | 1 | 200 | 0 | 1 | 0 | 1 | gap during inhibition: no alarm | PASS |
| 2 | 1 | 1 | 200 | 0 | 1 | 0 | 1 | 3s elapsed: still inhibited, debounce not accumulating | PASS |
| 3（保持 2100 ms） | 1 | 1 | 200 | 0 | 0 | 0 | 0 | 5s elapsed: inhibition ends; debounce starts now from zero | PASS |
| 4（保持 300 ms） | 1 | 1 | 200 | 1 | 0 | 1 | 0 | gap held for DebounceTime after init -> alarm | PASS |

### TC02 Debounce during normal monitoring

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Debounce during normal monitoring |
| 所属题目 | E05 Weld Gap Alarm and Startup Inhibition（`E05_WeldGap`） |
| 初始状态 | after the 5s inhibition, DebounceTime=500ms |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | alarm only after DebounceTime, short gap ignored, signal FALSE clears alarm and timing |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Gap_Exceeded | Weld_E_Stop_NC | DebounceTime | 预期 Operator_Alert | 预期 Weld_Soft_Start_Active | 实际 Operator_Alert | 实际 Weld_Soft_Start_Active | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|
| 0（保持 5200 ms） | 0 | 1 | 500 | 0 | 0 | 0 | 0 | initialisation finished | PASS |
| 1（保持 300 ms） | 1 | 1 | 500 | 0 |  | 0 |  | gap appears, debounce running | PASS |
| 2 | 0 | 1 | 500 | 0 |  | 0 |  | gap disappears before 500ms -> no alarm, timing cleared | PASS |
| 3（保持 300 ms） | 1 | 1 | 500 | 0 |  | 0 |  | new gap: full debounce required again | PASS |
| 4（保持 300 ms） | 1 | 1 | 500 | 1 |  | 1 |  | 500ms reached -> alarm | PASS |
| 5（保持 500 ms） | 1 | 1 | 500 | 1 |  | 1 |  | alarm held while gap persists | PASS |
| 6 | 0 | 1 | 500 | 0 |  | 0 |  | gap cleared -> alarm off immediately | PASS |

### TC03 Emergency stop priority

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Emergency stop priority |
| 所属题目 | E05 Weld Gap Alarm and Startup Inhibition（`E05_WeldGap`） |
| 初始状态 | after initialisation, DebounceTime=400ms |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | estop clears alarm immediately, blocks alarm during inhibition and monitoring, debounce cleared, full debounce after release |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Gap_Exceeded | Weld_E_Stop_NC | DebounceTime | 预期 Operator_Alert | 预期 Weld_Soft_Start_Active | 实际 Operator_Alert | 实际 Weld_Soft_Start_Active | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|
| 0（保持 5200 ms） | 0 | 1 | 400 | 0 | 0 | 0 | 0 | ready | PASS |
| 1（保持 500 ms） | 1 | 1 | 400 | 1 |  | 1 |  | alarm active | PASS |
| 2 | 1 | 0 | 400 | 0 |  | 0 |  | E-STOP -> alarm off immediately | PASS |
| 3（保持 1000 ms） | 1 | 0 | 400 | 0 |  | 0 |  | alarm stays off while e-stop active | PASS |
| 4 | 1 | 1 | 400 | 0 |  | 0 |  | released: debounce was cleared, not yet alarming | PASS |
| 5（保持 500 ms） | 1 | 1 | 400 | 1 |  | 1 |  | after a full DebounceTime -> alarm again | PASS |


## E06 Aeration Blower Delayed Start（`E06_Blower`）

- 编译：通过；用例通过 3/3；整题通过

### TC01 5-second start delay

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 5-second start delay |
| 所属题目 | E06 Aeration Blower Delayed Start（`E06_Blower`） |
| 初始状态 | power-up: BLOWER_RUN FALSE, count 0 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | power-up state, no run before 5s, run after 5s, count incremented once |
| 实际输出及结果 | ✅ 通过 |

| 周期 | DO_LOW | AERATION_E_STOP_NC | 预期 BLOWER_RUN | 预期 AERATION_BLOWER_CYCLE_COUNT | 实际 BLOWER_RUN | 实际 AERATION_BLOWER_CYCLE_COUNT | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 0 | 0 | power-up | PASS |
| 1（保持 3000 ms） | 1 | 1 | 0 | 0 | 0 | 0 | demand starts the delay | PASS |
| 2（保持 1900 ms） | 1 | 1 | 0 | 0 | 0 | 0 | 3s: still waiting | PASS |
| 3（保持 200 ms） | 1 | 1 | 1 | 1 | 1 | 1 | 5s reached -> blower runs, count 1 | PASS |
| 4（保持 3000 ms） | 1 | 1 | 1 | 1 | 1 | 1 | continuous running does not increment the count | PASS |

### TC02 Demand loss resets the delay

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Demand loss resets the delay |
| 所属题目 | E06 Aeration Blower Delayed Start（`E06_Blower`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | DO_LOW FALSE stops immediately, partial timing discarded, full 5s required again |
| 实际输出及结果 | ✅ 通过 |

| 周期 | DO_LOW | AERATION_E_STOP_NC | 预期 BLOWER_RUN | 预期 AERATION_BLOWER_CYCLE_COUNT | 实际 BLOWER_RUN | 实际 AERATION_BLOWER_CYCLE_COUNT | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|
| 0（保持 3000 ms） | 1 | 1 | 0 |  | 0 |  | delay running | PASS |
| 1 | 0 | 1 | 0 |  | 0 |  | demand lost at 3s -> timer reset | PASS |
| 2（保持 3000 ms） | 1 | 1 | 0 |  | 0 |  | new demand: 3s is not enough because timing restarted | PASS |
| 3（保持 1900 ms） | 1 | 1 | 0 |  | 0 |  | still below 5s | PASS |
| 4（保持 200 ms） | 1 | 1 | 1 | 1 | 1 | 1 | 5s of continuous demand -> run | PASS |
| 5 | 0 | 1 | 0 | 1 | 0 | 1 | demand lost while running -> stop immediately | PASS |
| 6（保持 4900 ms） | 1 | 1 | 0 | 1 | 0 | 1 | restart requires the full 5s again | PASS |
| 7（保持 200 ms） | 1 | 1 | 1 | 2 | 1 | 2 | second start -> count 2 | PASS |

### TC03 Emergency stop priority

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Emergency stop priority |
| 所属题目 | E06 Aeration Blower Delayed Start（`E06_Blower`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | estop stops the blower, blocks starting, resets timing, count unchanged by estop |
| 实际输出及结果 | ✅ 通过 |

| 周期 | DO_LOW | AERATION_E_STOP_NC | 预期 BLOWER_RUN | 预期 AERATION_BLOWER_CYCLE_COUNT | 实际 BLOWER_RUN | 实际 AERATION_BLOWER_CYCLE_COUNT | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|
| 0（保持 5200 ms） | 1 | 1 | 1 | 1 | 1 | 1 | demand held for 5 s -> blower running, first start counted | PASS |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | still running | PASS |
| 2 | 1 | 0 | 0 | 1 | 0 | 1 | E-STOP -> stop immediately, count unchanged | PASS |
| 3（保持 6000 ms） | 1 | 0 | 0 | 1 | 0 | 1 | cannot start during e-stop | PASS |
| 4 | 1 | 1 | 0 | 1 | 0 | 1 | released: timing restarted, not running yet | PASS |
| 5（保持 5200 ms） | 1 | 1 | 1 | 2 | 1 | 2 | after a full 5s -> running, count 2 | PASS |


## M01 Multi-Pump Switching Control System（`M01_PumpSwitch`）

- 编译：通过；用例通过 3/3；整题通过

### TC01 Manual mode runs the selected pumps

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Manual mode runs the selected pumps |
| 所属题目 | M01 Multi-Pump Switching Control System（`M01_PumpSwitch`） |
| 初始状态 | power-up, mode=0 (manual), no pump running |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | start runs selected pumps, selection changes are followed, stop stops all |
| 实际输出及结果 | ✅ 通过 |

| 周期 | mode | start | stop | pumpGroup[1].priority | pumpGroup[1].selection | pumpGroup[2].priority | pumpGroup[2].selection | pumpGroup[3].priority | pumpGroup[3].selection | pumpGroup[4].priority | pumpGroup[4].selection | pumpGroup[5].priority | pumpGroup[5].selection | 预期 pumpGroup[1].RunComd | 预期 pumpGroup[2].RunComd | 预期 pumpGroup[3].RunComd | 预期 pumpGroup[4].RunComd | 预期 pumpGroup[5].RunComd | 实际 pumpGroup[1].RunComd | 实际 pumpGroup[2].RunComd | 实际 pumpGroup[3].RunComd | 实际 pumpGroup[4].RunComd | 实际 pumpGroup[5].RunComd | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | not started yet -> all stopped | PASS |
| 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | start -> selected pumps 1 and 3 run | PASS |
| 2 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | button released -> still running | PASS |
| 3 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | selection changed -> pumps follow | PASS |
| 4 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | stop -> all pumps stop | PASS |
| 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | stays stopped until start | PASS |

### TC02 Automatic mode runs the three highest priorities

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Automatic mode runs the three highest priorities |
| 所属题目 | M01 Multi-Pump Switching Control System（`M01_PumpSwitch`） |
| 初始状态 | power-up, mode=1 (automatic) |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | 3 duty / 2 standby selection, priority ranking, selection ignored in auto |
| 实际输出及结果 | ✅ 通过 |

| 周期 | mode | start | stop | pumpGroup[1].priority | pumpGroup[1].selection | pumpGroup[2].priority | pumpGroup[2].selection | pumpGroup[3].priority | pumpGroup[3].selection | pumpGroup[4].priority | pumpGroup[4].selection | pumpGroup[5].priority | pumpGroup[5].selection | 预期 pumpGroup[1].RunComd | 预期 pumpGroup[2].RunComd | 预期 pumpGroup[3].RunComd | 预期 pumpGroup[4].RunComd | 预期 pumpGroup[5].RunComd | 实际 pumpGroup[1].RunComd | 实际 pumpGroup[2].RunComd | 实际 pumpGroup[3].RunComd | 实际 pumpGroup[4].RunComd | 实际 pumpGroup[5].RunComd | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 10 | 0 | 50 | 0 | 30 | 0 | 40 | 0 | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | not started yet | PASS |
| 1 | 1 | 1 | 0 | 10 | 0 | 50 | 0 | 30 | 0 | 40 | 0 | 20 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | top three priorities (50,40,30) = pumps 2,4,3 | PASS |
| 2 | 1 | 1 | 0 | 10 | 1 | 50 | 0 | 30 | 0 | 40 | 0 | 20 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | manual selection ignored in automatic mode | PASS |
| 3 | 1 | 1 | 0 | 90 | 0 | 10 | 0 | 20 | 0 | 30 | 0 | 40 | 0 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | priorities changed -> pumps 1,5,4 run | PASS |
| 4 | 1 | 0 | 1 | 90 | 0 | 10 | 0 | 20 | 0 | 30 | 0 | 40 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | stop -> all stop | PASS |

### TC03 Mode switching and priority ties

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Mode switching and priority ties |
| 所属题目 | M01 Multi-Pump Switching Control System（`M01_PumpSwitch`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | switching between manual and automatic, equal priorities still select exactly three pumps |
| 实际输出及结果 | ✅ 通过 |

| 周期 | mode | start | stop | pumpGroup[1].priority | pumpGroup[1].selection | pumpGroup[2].priority | pumpGroup[2].selection | pumpGroup[3].priority | pumpGroup[3].selection | pumpGroup[4].priority | pumpGroup[4].selection | pumpGroup[5].priority | pumpGroup[5].selection | 预期 pumpGroup[1].RunComd | 预期 pumpGroup[2].RunComd | 预期 pumpGroup[3].RunComd | 预期 pumpGroup[4].RunComd | 预期 pumpGroup[5].RunComd | 实际 pumpGroup[1].RunComd | 实际 pumpGroup[2].RunComd | 实际 pumpGroup[3].RunComd | 实际 pumpGroup[4].RunComd | 实际 pumpGroup[5].RunComd | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | manual: two selected pumps | PASS |
| 1 | 1 | 1 | 0 | 5 | 1 | 4 | 1 | 3 | 0 | 2 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | switch to automatic -> top three (5,4,3) | PASS |
| 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | back to manual -> only the selected pump | PASS |
| 3 | 1 | 1 | 0 | 7 | 0 | 7 | 0 | 7 | 0 | 7 | 0 | 7 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | all priorities equal -> exactly three pumps run | PASS |


## M02 Analog Batch Processing（`M02_AnalogBatch`）

- 编译：通过；用例通过 3/3；整题通过

### TC01 Unipolar and bipolar linear scaling (mode 0)

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Unipolar and bipolar linear scaling (mode 0) |
| 所属题目 | M02 Analog Batch Processing（`M02_AnalogBatch`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | raw 0, mid and full scale mapped to the engineering range, bipolar negative range |
| 实际输出及结果 | ✅ 通过 |

| 周期 | count | analogValues[1] | channels[1].enable | channels[1].hiLIM | channels[1].loLIM | channels[1].bipolar | channels[1].measuringMode | analogValues[2] | channels[2].enable | channels[2].hiLIM | channels[2].loLIM | channels[2].bipolar | channels[2].measuringMode | 预期 channels[1].outputValue | 预期 channels[1].retVal | 预期 channels[2].outputValue | 预期 channels[2].retVal | 实际 channels[1].outputValue | 实际 channels[1].retVal | 实际 channels[2].outputValue | 实际 channels[2].retVal | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 2 | 0 | 1 | 100.0 | 0.0 | 0 | 0 | 27648 | 1 | 100.0 | 0.0 | 0 | 0 | 0.0 | 0 | 100.0 | 0 | 0.0 | 0 | 100.0 | 0 | unipolar: 0 -> loLIM, 27648 -> hiLIM | PASS |
| 1 | 2 | 13824 | 1 | 100.0 | 0.0 | 0 | 0 | 13824 | 1 | 200.0 | 100.0 | 0 | 0 | 50.0 | 0 | 150.0 | 0 | 50.0 | 0 | 150.0 | 0 | unipolar mid scale | PASS |
| 2 | 2 | -27648 | 1 | 100.0 | -100.0 | 1 | 0 | 27648 | 1 | 100.0 | -100.0 | 1 | 0 | -100.0 | 0 | 100.0 | 0 | -100.0 | 0 | 100.0 | 0 | bipolar: -27648 -> loLIM, 27648 -> hiLIM | PASS |
| 3 | 1 | 0 | 1 | 100.0 | -100.0 | 1 | 0 |  |  |  |  |  |  | 0.0 | 0 |  |  | 0.0 | 0 |  |  | bipolar zero -> midpoint of the range | PASS |

### TC02 Temperature conversions (modes 1 and 2)

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Temperature conversions (modes 1 and 2) |
| 所属题目 | M02 Analog Batch Processing（`M02_AnalogBatch`） |
| 初始状态 | power-up; limits set to a valid range (the limit check applies to every mode) |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | standard temperature = raw/10, climatic temperature = raw/100, negative values |
| 实际输出及结果 | ✅ 通过 |

| 周期 | count | analogValues[1] | channels[1].enable | channels[1].hiLIM | channels[1].loLIM | channels[1].bipolar | channels[1].measuringMode | analogValues[2] | channels[2].enable | channels[2].hiLIM | channels[2].loLIM | channels[2].bipolar | channels[2].measuringMode | 预期 channels[1].outputValue | 预期 channels[1].retVal | 预期 channels[2].outputValue | 预期 channels[2].retVal | 实际 channels[1].outputValue | 实际 channels[1].retVal | 实际 channels[2].outputValue | 实际 channels[2].retVal | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 2 | 250 | 1 | 100.0 | 0.0 | 0 | 1 | 2500 | 1 | 100.0 | 0.0 | 0 | 2 | 25.0 | 0 | 25.0 | 0 | 25.0 | 0 | 25.0 | 0 | mode 1: 250 -> 25.0; mode 2: 2500 -> 25.0 | PASS |
| 1 | 2 | -125 | 1 | 100.0 | 0.0 | 0 | 1 | -1250 | 1 | 100.0 | 0.0 | 0 | 2 | -12.5 | 0 | -12.5 | 0 | -12.5 | 0 | -12.5 | 0 | negative temperatures | PASS |
| 2 | 1 | 0 | 1 | 100.0 | 0.0 | 0 | 1 |  |  |  |  |  |  | 0.0 | 0 |  |  | 0.0 | 0 |  |  | zero raw value | PASS |

### TC03 Error handling and enable flag

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Error handling and enable flag |
| 所属题目 | M02 Analog Batch Processing（`M02_AnalogBatch`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | invalid mode -> 16#8001, hiLIM <= loLIM -> 16#8002, disabled channels are skipped, count limits processing |
| 实际输出及结果 | ✅ 通过 |

| 周期 | count | analogValues[1] | channels[1].enable | channels[1].hiLIM | channels[1].loLIM | channels[1].bipolar | channels[1].measuringMode | analogValues[2] | channels[2].enable | channels[2].hiLIM | channels[2].loLIM | channels[2].bipolar | channels[2].measuringMode | 预期 channels[1].retVal | 预期 channels[2].outputValue | 预期 channels[2].retVal | 预期 channels[1].outputValue | 实际 channels[1].retVal | 实际 channels[2].outputValue | 实际 channels[2].retVal | 实际 channels[1].outputValue | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 2 | 13824 | 1 | 100.0 | 0.0 | 0 | 5 | 13824 | 1 | 100.0 | 0.0 | 0 | 0 | 32769 | 50.0 | 0 |  | 32769 | 50.0 | 0 |  | channel 1 invalid mode -> 16#8001, channel 2 still converted | PASS |
| 1 | 2 | 13824 | 1 | 0.0 | 100.0 | 0 | 0 | 13824 | 1 | 50.0 | 50.0 | 0 | 0 | 32770 |  | 32770 |  | 32770 |  | 32770 |  | hiLIM < loLIM and hiLIM = loLIM -> 16#8002 | PASS |
| 2 | 2 | 13824 | 0 | 100.0 | 0.0 | 0 | 0 | 13824 | 1 | 100.0 | 0.0 | 0 | 0 |  | 50.0 | 0 |  |  | 50.0 | 0 |  | disabled channel is skipped | PASS |
| 3 | 1 | 13824 | 1 | 100.0 | 0.0 | 0 | 0 | 13824 | 1 | 100.0 | 0.0 | 0 | 0 | 0 |  |  | 50.0 | 0 |  |  | 50.0 | count=1: only the first channel is processed | PASS |


## M03 Calculate Moving Average（`M03_MovingAvg`）

- 编译：通过；用例通过 5/5；整题通过

### TC01 Cyclic moving average with window 3

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Cyclic moving average with window 3 |
| 所属题目 | M03 Calculate Moving Average（`M03_MovingAvg`） |
| 初始状态 | power-up, windowSize=3, cyclicExecution=TRUE |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | average over a partially filled window, window reached, oldest value replaced |
| 实际输出及结果 | ✅ 通过 |

| 周期 | cyclicExecution | trigger | value | windowSize | reset | 预期 average | 预期 windowSizeReached | 预期 error | 预期 status | 实际 average | 实际 windowSizeReached | 实际 error | 实际 status | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 10.0 | 3 | 0 | 10.0 | 0 | 0 | 0 | 10.0 | 0 | 0 | 0 | first value: average = 10 | PASS |
| 1 | 1 | 0 | 20.0 | 3 | 0 | 15.0 | 0 |  |  | 15.0 | 0 |  |  | two values: (10+20)/2 = 15 | PASS |
| 2 | 1 | 0 | 30.0 | 3 | 0 | 20.0 | 1 |  |  | 20.0 | 1 |  |  | three values: (10+20+30)/3 = 20, window reached | PASS |
| 3 | 1 | 0 | 60.0 | 3 | 0 | 36.666666666666664 | 1 |  |  | 36.666666666666664 | 1 |  |  | oldest (10) dropped: (20+30+60)/3 | PASS |
| 4 | 1 | 0 | 90.0 | 3 | 0 | 60.0 | 1 |  |  | 60.0 | 1 |  |  | (30+60+90)/3 = 60 | PASS |

### TC02 Trigger mode reads only on a rising edge

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Trigger mode reads only on a rising edge |
| 所属题目 | M03 Calculate Moving Average（`M03_MovingAvg`） |
| 初始状态 | power-up, windowSize=2, cyclicExecution=FALSE |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | no read without a trigger, one read per rising edge, held trigger does not read again |
| 实际输出及结果 | ✅ 通过 |

| 周期 | cyclicExecution | trigger | value | windowSize | reset | 预期 average | 预期 windowSizeReached | 实际 average | 实际 windowSizeReached | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 10.0 | 2 | 0 | 0.0 | 0 | 0.0 | 0 | no trigger -> nothing read | PASS |
| 1 | 0 | 1 | 10.0 | 2 | 0 | 10.0 |  | 10.0 |  | rising edge -> value read | PASS |
| 2 | 0 | 1 | 99.0 | 2 | 0 | 10.0 |  | 10.0 |  | trigger held -> no new read | PASS |
| 3 | 0 | 0 | 99.0 | 2 | 0 | 10.0 |  | 10.0 |  | trigger released -> no read | PASS |
| 4 | 0 | 1 | 30.0 | 2 | 0 | 20.0 | 1 | 20.0 | 1 | new rising edge -> (10+30)/2 = 20 | PASS |

### TC03 cyclicExecution overrides the trigger

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 cyclicExecution overrides the trigger |
| 所属题目 | M03 Calculate Moving Average（`M03_MovingAvg`） |
| 初始状态 | power-up, windowSize=2, cyclicExecution=TRUE |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | with cyclicExecution TRUE a value is read every cycle regardless of the trigger |
| 实际输出及结果 | ✅ 通过 |

| 周期 | cyclicExecution | trigger | value | windowSize | reset | 预期 average | 预期 windowSizeReached | 实际 average | 实际 windowSizeReached | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 4.0 | 2 | 0 | 4.0 |  | 4.0 |  | read without a trigger | PASS |
| 1 | 1 | 0 | 8.0 | 2 | 0 | 6.0 | 1 | 6.0 | 1 | read again: (4+8)/2 = 6 | PASS |
| 2 | 1 | 1 | 12.0 | 2 | 0 | 10.0 |  | 10.0 |  | trigger has no additional effect: (8+12)/2 = 10 | PASS |

### TC04 Reset clears the calculation

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Reset clears the calculation |
| 所属题目 | M03 Calculate Moving Average（`M03_MovingAvg`） |
| 初始状态 | power-up, windowSize=3, cyclicExecution=TRUE |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | reset zeroes the average and the window, new values start from scratch |
| 实际输出及结果 | ✅ 通过 |

| 周期 | cyclicExecution | trigger | value | windowSize | reset | 预期 average | 预期 windowSizeReached | 预期 error | 实际 average | 实际 windowSizeReached | 实际 error | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 10.0 | 3 | 0 | 10.0 |  |  | 10.0 |  |  | first value | PASS |
| 1 | 1 | 0 | 20.0 | 3 | 0 | 15.0 |  |  | 15.0 |  |  | second | PASS |
| 2 | 1 | 0 | 30.0 | 3 | 0 | 20.0 | 1 |  | 20.0 | 1 |  | window reached | PASS |
| 3 | 1 | 0 | 99.0 | 3 | 1 | 0.0 | 0 | 0 | 0.0 | 0 | 0 | reset -> average 0, window not reached | PASS |
| 4 | 1 | 0 | 50.0 | 3 | 0 | 50.0 | 0 |  | 50.0 | 0 |  | restart: only the new value counts | PASS |

### TC05 Window-size errors

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC05 Window-size errors |
| 所属题目 | M03 Calculate Moving Average（`M03_MovingAvg`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | windowSize 0 and 101 produce 16#8200, boundaries 1 and 100 are valid, recovery after a valid size |
| 实际输出及结果 | ✅ 通过 |

| 周期 | cyclicExecution | trigger | value | windowSize | reset | 预期 error | 预期 status | 预期 average | 预期 windowSizeReached | 实际 error | 实际 status | 实际 average | 实际 windowSizeReached | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 10.0 | 0 | 0 | 1 | 33280 |  |  | 1 | 33280 |  |  | windowSize 0 -> error 16#8200 | PASS |
| 1 | 1 | 0 | 10.0 | 101 | 0 | 1 | 33280 |  |  | 1 | 33280 |  |  | windowSize 101 -> error | PASS |
| 2 | 1 | 0 | 10.0 | -5 | 0 | 1 | 33280 |  |  | 1 | 33280 |  |  | negative window -> error | PASS |
| 3 | 1 | 0 | 10.0 | 1 | 0 | 0 | 0 | 10.0 | 1 | 0 | 0 | 10.0 | 1 | windowSize 1 is valid, average = value | PASS |
| 4 | 1 | 0 | 20.0 | 1 | 0 | 0 |  | 20.0 | 1 | 0 |  | 20.0 | 1 | window 1: average follows the latest value | PASS |
| 5 | 1 | 0 | 20.0 | 100 | 0 | 0 | 0 |  |  | 0 | 0 |  |  | windowSize 100 is valid | PASS |


## M04 Temperature Logic Control（`M04_TempCtrl`）

- 编译：通过；用例通过 4/4；整题通过

### TC01 Basic heating control and status display

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Basic heating control and status display |
| 所属题目 | M04 Temperature Logic Control（`M04_TempCtrl`） |
| 初始状态 | power-up, all outputs OFF |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | heater on below setpoint, off above, display mirrors inputs |
| 实际输出及结果 | ✅ 通过 |

| 周期 | TemperatureSensorInput | SetTemperature | 预期 HeaterOutput | 预期 HeaterStatus | 预期 OverheatProtection | 预期 CurrentTemperature | 预期 SetTempDisplay | 实际 HeaterOutput | 实际 HeaterStatus | 实际 OverheatProtection | 实际 CurrentTemperature | 实际 SetTempDisplay | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 25.0 | 30.0 | 1 | 1 | 0 | 25.0 | 30.0 | 1 | 1 | 0 | 25.0 | 30.0 | below setpoint -> heater on, displays mirror inputs | PASS |
| 1 | 29.9 | 30.0 | 1 | 1 |  | 29.9 |  | 1 | 1 |  | 29.9 |  | still below -> heating | PASS |
| 2 | 35.0 | 30.0 | 0 | 0 |  | 35.0 |  | 0 | 0 |  | 35.0 |  | above setpoint -> heater off | PASS |
| 3 | 30.0 | 30.0 | 0 | 0 |  |  |  | 0 | 0 |  |  |  | equal to setpoint -> not below -> heater off | PASS |
| 4 | 20.0 | 50.0 | 1 | 1 |  |  | 50.0 | 1 | 1 |  |  | 50.0 | new setpoint, below -> heating | PASS |

### TC02 Overheat protection after 5 s of continuous heating

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Overheat protection after 5 s of continuous heating |
| 所属题目 | M04 Temperature Logic Control（`M04_TempCtrl`） |
| 初始状态 | power-up, temperature 20, setpoint 80 (heater stays demanded) |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | protection trips at 5s, heater forced off, protection held for 3s, released afterwards |
| 实际输出及结果 | ✅ 通过 |

| 周期 | TemperatureSensorInput | SetTemperature | 预期 HeaterOutput | 预期 HeaterStatus | 预期 OverheatProtection | 实际 HeaterOutput | 实际 HeaterStatus | 实际 OverheatProtection | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0（保持 3000 ms） | 20.0 | 80.0 | 1 | 1 | 0 | 1 | 1 | 0 | heating starts | PASS |
| 1（保持 1900 ms） | 20.0 | 80.0 | 1 | 1 | 0 | 1 | 1 | 0 | 3s of continuous heating: no protection yet | PASS |
| 2（保持 200 ms） | 20.0 | 80.0 | 0 | 0 | 1 | 0 | 0 | 1 | 5s reached -> protection trips, heater off | PASS |
| 3（保持 2000 ms） | 20.0 | 80.0 | 0 | 0 | 1 | 0 | 0 | 1 | protection held, heater stays off although demand persists | PASS |
| 4（保持 700 ms） | 20.0 | 80.0 | 0 | 0 | 1 | 0 | 0 | 1 | 2.9 s of the 3 s wait: protection still active | PASS |
| 5（保持 200 ms） | 20.0 | 80.0 |  |  | 0 |  |  | 0 | 3 s elapsed -> protection lifted (heater restarts in the next cycle) | PASS |
| 6 | 20.0 | 80.0 | 1 | 1 | 0 | 1 | 1 | 0 | heating resumes | PASS |

### TC03 Sensor fault turns the heater off

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Sensor fault turns the heater off |
| 所属题目 | M04 Temperature Logic Control（`M04_TempCtrl`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | value < 0 and > 100 are faults, heater off, recovery when the value returns to range |
| 实际输出及结果 | ✅ 通过 |

| 周期 | TemperatureSensorInput | SetTemperature | 预期 HeaterOutput | 预期 HeaterStatus | 实际 HeaterOutput | 实际 HeaterStatus | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|
| 0 | 20.0 | 50.0 | 1 | 1 | 1 | 1 | normal heating | PASS |
| 1 | -0.1 | 50.0 | 0 | 0 | 0 | 0 | value < 0 -> sensor fault, heater off | PASS |
| 2 | 0.0 | 50.0 | 1 | 1 | 1 | 1 | 0 is a valid value -> heating again | PASS |
| 3 | 100.1 | 50.0 | 0 | 0 | 0 | 0 | value > 100 -> sensor fault, heater off | PASS |
| 4 | 100.0 | 50.0 | 0 | 0 | 0 | 0 | 100 is valid but above setpoint -> heater off | PASS |
| 5 | 100.0 | 120.0 | 1 | 1 | 1 | 1 | 100 valid and below setpoint -> heating | PASS |

### TC04 Heating interrupted before 5 s does not trip protection

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Heating interrupted before 5 s does not trip protection |
| 所属题目 | M04 Temperature Logic Control（`M04_TempCtrl`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | the run timer restarts when the heater stops |
| 实际输出及结果 | ✅ 通过 |

| 周期 | TemperatureSensorInput | SetTemperature | 预期 HeaterOutput | 预期 HeaterStatus | 预期 OverheatProtection | 实际 HeaterOutput | 实际 HeaterStatus | 实际 OverheatProtection | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0（保持 3000 ms） | 20.0 | 80.0 | 1 | 1 | 0 | 1 | 1 | 0 | heating | PASS |
| 1 | 90.0 | 80.0 | 0 | 0 | 0 | 0 | 0 | 0 | above setpoint -> heater off before 5s, no protection | PASS |
| 2（保持 3000 ms） | 20.0 | 80.0 | 1 | 1 | 0 | 1 | 1 | 0 | heating again | PASS |
| 3（保持 1000 ms） | 20.0 | 80.0 | 1 | 1 | 0 | 1 | 1 | 0 | 3s of the new heating period: still no protection | PASS |


## M05 Automated Production Line Control（`M05_ProdLine`）

- 编译：通过；用例通过 4/6；整题未通过

### TC01 Manual mode jog with interlock

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Manual mode jog with interlock |
| 所属题目 | M05 Automated Production Line Control（`M05_ProdLine`） |
| 初始状态 | power-up, Mode=0 (manual), all inputs FALSE |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | forward, reverse, both pressed -> both OFF, release -> stop, light OFF in manual |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Mode | ForwardButton | ReverseButton | SensorA | SensorB | SensorC | ButtonA | ButtonB | ButtonC | 预期 MotorForward | 预期 MotorReverse | 预期 CompletionLight | 实际 MotorForward | 实际 MotorReverse | 实际 CompletionLight | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | idle manual, all OFF | PASS |
| 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | forward button -> forward | PASS |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | released -> stop (jog, no latching) | PASS |
| 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | reverse button -> reverse | PASS |
| 4 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | both pressed -> interlock, both OFF | PASS |
| 5 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | forward released -> reverse again | PASS |
| 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | all released -> stop | PASS |
| 7 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | auto-mode signals have no effect in manual | PASS |

### TC02 Automatic full cycle

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Automatic full cycle |
| 所属题目 | M05 Automated Production Line Control（`M05_ProdLine`） |
| 初始状态 | power-up, Mode=1 (auto), product not yet at A |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | A->B->C sequence, motor stops on arrival, light ON after ButtonC, light OFF when product removed |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Mode | ForwardButton | ReverseButton | SensorA | SensorB | SensorC | ButtonA | ButtonB | ButtonC | 预期 MotorForward | 预期 MotorReverse | 预期 CompletionLight | 实际 MotorForward | 实际 MotorReverse | 实际 CompletionLight | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | auto idle, nothing moves | PASS |
| 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | product at A, waiting for ButtonA | PASS |
| 2 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |  | 0 | 0 |  | 0 | 0 | ButtonA -> motor forward (trigger cycle) | PASS |
| 3 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | motor starts in the following cycle | PASS |
| 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | product left A, still moving | PASS |
| 5 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | arrived at B -> motor stops | PASS |
| 6 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | waiting for ButtonB | PASS |
| 7 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |  | 0 | 0 |  | 0 | 0 | ButtonB -> motor forward (trigger cycle) | PASS |
| 8 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | motor starts in the following cycle | PASS |
| 9 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | moving B->C | PASS |
| 10 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | arrived at C -> motor stops | PASS |
| 11 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | ButtonC -> completion light ON | PASS |
| 12 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | light stays ON while product present | PASS |
| 13 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | product removed -> light OFF | PASS |
| 14 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |  | 0 | 0 |  | 0 | 0 | next product can start a new cycle (trigger cycle) | PASS |
| 15 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | motor starts in the following cycle | PASS |

### TC03 Automatic mode ignores wrong signals

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Automatic mode ignores wrong signals |
| 所属题目 | M05 Automated Production Line Control（`M05_ProdLine`） |
| 初始状态 | power-up, Mode=1 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | ButtonA without product, buttons at wrong station, manual buttons in auto, no reverse in auto |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Mode | ForwardButton | ReverseButton | SensorA | SensorB | SensorC | ButtonA | ButtonB | ButtonC | 预期 MotorForward | 预期 MotorReverse | 预期 CompletionLight | 实际 MotorForward | 实际 MotorReverse | 实际 CompletionLight | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ButtonA without product at A -> nothing | PASS |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | manual buttons ignored in auto | PASS |
| 2 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | wrong buttons at A -> nothing | PASS |
| 3 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |  | 0 | 0 |  | 0 | 0 | correct button starts (trigger cycle) | PASS |
| 4 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | motor starts in the following cycle | PASS |
| 5 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | at B | PASS |
| 6 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | wrong buttons at B -> stays stopped | PASS |
| 7 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |  | 0 | 0 |  | 0 | 0 | correct button continues (trigger cycle) | PASS |
| 8 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | motor starts in the following cycle | PASS |
| 9 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | at C, no light before ButtonC | PASS |
| 10 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | wrong buttons at C -> no light | PASS |

### TC04 Mode switch during automatic cycle

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Mode switch during automatic cycle |
| 所属题目 | M05 Automated Production Line Control（`M05_ProdLine`） |
| 初始状态 | power-up, Mode=1 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | switching to manual stops automatic motion; manual jog works; returning to automatic resumes the stored step |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Mode | ForwardButton | ReverseButton | SensorA | SensorB | SensorC | ButtonA | ButtonB | ButtonC | 预期 MotorReverse | 预期 CompletionLight | 预期 MotorForward | 实际 MotorReverse | 实际 CompletionLight | 实际 MotorForward | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |  | 0 | 0 |  | auto start (trigger cycle) | PASS |
| 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | motor starts in the following cycle | PASS |
| 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | moving | PASS |
| 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | switch to manual -> motor stops | PASS |
| 4 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | manual reverse works | PASS |
| 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | released | PASS |
| 6 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | 0 |  |  | back to automatic: the reference implementation keeps its internal step, so the interrupted move resumes (resume-vs-restart is not fixed by the requirement) | PASS |

### TC05 A station button held in advance does not release the carriage

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC05 A station button held in advance does not release the carriage |
| 所属题目 | M05 Automated Production Line Control（`M05_ProdLine`） |
| 初始状态 | auto mode, carriage at A (SensorA), step 0 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | edge-triggered station buttons: ButtonB pressed before station B is reached must not start the next leg; outputs follow a transition one scan later |
| 实际输出及结果 | ❌ 不通过；周期 1：MotorForward 预期 0，实际 True；周期 8：MotorForward 预期 0，实际 True |

| 周期 | Mode | ForwardButton | ReverseButton | SensorA | SensorB | SensorC | ButtonA | ButtonB | ButtonC | 预期 MotorForward | 预期 MotorReverse | 实际 MotorForward | 实际 MotorReverse | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | waiting at A | PASS |
| 1 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |  | 1 |  | ButtonA edge: transition to the travelling step, output next scan | FAIL |
| 2 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 1 |  | 1 |  | travelling to B; ButtonB is pressed early and held from here on | PASS |
| 3 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |  | 1 |  | still travelling, both buttons held | PASS |
| 4 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |  | 0 |  | arrived at B: motor stops | PASS |
| 5 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |  | 0 |  | DECISIVE: ButtonB was already held on arrival, so it has no rising edge and the carriage must stay at B | PASS |
| 6 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |  | 0 |  | still held: still waiting | PASS |
| 7 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  | 0 |  | released, still waiting | PASS |
| 8 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |  | 1 |  | fresh ButtonB edge: transition, output next scan | FAIL |
| 9 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 |  | 1 |  | now travelling to C | PASS |
| 10 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |  | 0 |  | arrived at C | PASS |

### TC06 Station sensors held while the operator works at the station

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC06 Station sensors held while the operator works at the station |
| 所属题目 | M05 Automated Production Line Control（`M05_ProdLine`） |
| 初始状态 | auto mode, carriage at A (SensorA), step 0 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | station sensor held TRUE across the whole processing time: the motor stays stopped, holding the button does not advance, and the carriage leaves only once the operator confirms |
| 实际输出及结果 | ❌ 不通过；周期 2：MotorForward 预期 0，实际 True；周期 7：MotorForward 预期 0，实际 True |

| 周期 | Mode | ForwardButton | ReverseButton | SensorA | SensorB | SensorC | ButtonA | ButtonB | ButtonC | 预期 MotorForward | 实际 MotorForward | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | product at A, waiting | PASS |
| 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | sensor held, no button: still waiting, nothing latches spuriously | PASS |
| 2 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | ButtonA edge: transition taken this cycle | FAIL |
| 3 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | motor now drives the product away, though SensorA is still TRUE. A level implementation that re-checks SensorA would stall here | PASS |
| 4 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | arrives at B: motor stops | PASS |
| 5 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | SensorB held for many cycles: the motor must stay stopped | PASS |
| 6 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | still held, and ButtonA is the wrong button: no movement | PASS |
| 7 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | ButtonB edge: transition to the travelling step | FAIL |
| 8 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | motor runs although SensorB is still TRUE | PASS |
| 9 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | arrives at C: motor stops | PASS |
| 10 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | SensorC held: motor stays stopped until the product is collected | PASS |


## M06 Slab Thickness Alarm and Fault History（`M06_SlabThick`）

- 编译：通过；用例通过 2/5；整题未通过

### TC01 Alarm with 500 ms minimum hold

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Alarm with 500 ms minimum hold |
| 所属题目 | M06 Slab Thickness Alarm and Fault History（`M06_SlabThick`） |
| 初始状态 | power-up: alarm off, counter 0, runtime 0, history zero |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | alarm on at the fault edge, held 500 ms after the fault clears, off afterwards |
| 实际输出及结果 | ✅ 通过 |

| 周期 | THICKNESS_FAULT | THICKNESS_SIGNAL_VALID | CUTTING_RUN | FaultTimestamp | CycleTime | 预期 THICKNESS_ALARM | 预期 Slab_Fault_Counter | 预期 Slab_Runtime_Accumulator | 预期 Slab_Fault_History[0] | 预期 Slab_Fault_History[1] | 预期 Slab_Fault_History[2] | 预期 Slab_Fault_History[3] | 预期 Slab_Fault_History[4] | 实际 THICKNESS_ALARM | 实际 Slab_Fault_Counter | 实际 Slab_Runtime_Accumulator | 实际 Slab_Fault_History[0] | 实际 Slab_Fault_History[1] | 实际 Slab_Fault_History[2] | 实际 Slab_Fault_History[3] | 实际 Slab_Fault_History[4] | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | power-up | PASS |
| 1 | 1 | 1 | 0 | 1000 | 100 | 1 | 1 |  |  |  |  |  |  | 1 | 1 |  |  |  |  |  |  | fault -> alarm, counted | PASS |
| 2（保持 300 ms） | 0 | 1 | 0 | 0 | 100 | 1 |  |  |  |  |  |  |  | 1 |  |  |  |  |  |  |  | fault cleared, still within the 500 ms hold | PASS |
| 3（保持 400 ms） | 0 | 1 | 0 | 0 | 100 | 0 |  |  |  |  |  |  |  | 0 |  |  |  |  |  |  |  | 500 ms elapsed -> alarm released | PASS |
| 4 | 0 | 1 | 0 | 0 | 100 | 0 | 1 |  |  |  |  |  |  | 0 | 1 |  |  |  |  |  |  | stays off | PASS |

### TC02 Alarm stays active while the fault persists

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Alarm stays active while the fault persists |
| 所属题目 | M06 Slab Thickness Alarm and Fault History（`M06_SlabThick`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | long fault keeps the alarm on, no repeated counting |
| 实际输出及结果 | ❌ 不通过；周期 0：Slab_Fault_Counter 预期 1，实际 0；周期 1：Slab_Fault_Counter 预期 1，实际 0；周期 2：THICKNESS_ALARM 预期 1，实际 False |

| 周期 | THICKNESS_FAULT | THICKNESS_SIGNAL_VALID | CUTTING_RUN | FaultTimestamp | CycleTime | 预期 THICKNESS_ALARM | 预期 Slab_Fault_Counter | 实际 THICKNESS_ALARM | 实际 Slab_Fault_Counter | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 2000 | 100 | 1 | 1 | 1 | 0 | fault | FAIL |
| 1（保持 2000 ms） | 1 | 1 | 0 | 0 | 100 | 1 | 1 | 1 | 0 | persists, not counted again | FAIL |
| 2（保持 200 ms） | 0 | 1 | 0 | 0 | 100 | 1 |  | 0 |  | cleared, hold starts | FAIL |
| 3（保持 500 ms） | 0 | 1 | 0 | 0 | 100 | 0 |  | 0 |  | released | PASS |

### TC03 Fault counting and history shifting

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Fault counting and history shifting |
| 所属题目 | M06 Slab Thickness Alarm and Fault History（`M06_SlabThick`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | one count per rising edge, newest at index 0, oldest dropped |
| 实际输出及结果 | ❌ 不通过；周期 0：Slab_Fault_Counter 预期 1，实际 0；Slab_Fault_History[0] 预期 101，实际 0；周期 1：Slab_Fault_Counter 预期 1，实际 0；周期 2：Slab_Fault_Counter 预期 2，实际 1；Slab_Fault_History[1] 预期 101，实际 0 |

| 周期 | THICKNESS_FAULT | THICKNESS_SIGNAL_VALID | CUTTING_RUN | FaultTimestamp | CycleTime | 预期 Slab_Fault_Counter | 预期 Slab_Fault_History[0] | 预期 Slab_Fault_History[1] | 预期 Slab_Fault_History[2] | 预期 Slab_Fault_History[3] | 预期 Slab_Fault_History[4] | 实际 Slab_Fault_Counter | 实际 Slab_Fault_History[0] | 实际 Slab_Fault_History[1] | 实际 Slab_Fault_History[2] | 实际 Slab_Fault_History[3] | 实际 Slab_Fault_History[4] | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 101 | 100 | 1 | 101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | fault 1 | FAIL |
| 1（保持 600 ms） | 0 | 1 | 0 | 0 | 100 | 1 |  |  |  |  |  | 0 |  |  |  |  |  | cleared | FAIL |
| 2 | 1 | 1 | 0 | 202 | 100 | 2 | 202 | 101 | 0 | 0 | 0 | 1 | 202 | 0 | 0 | 0 | 0 | fault 2 | FAIL |
| 3（保持 600 ms） | 0 | 1 | 0 | 0 | 100 | 2 | 202 | 101 |  |  |  | 1 | 202 | 0 |  |  |  | fault cleared: counter and history unchanged (no record without a rising edge) | FAIL |
| 4 | 1 | 1 | 0 | 303 | 100 | 3 | 303 | 202 | 101 | 0 | 0 | 2 | 303 | 202 | 0 | 0 | 0 | fault 3 | FAIL |
| 5（保持 600 ms） | 0 | 1 | 0 | 0 | 100 | 3 | 303 | 202 | 101 |  |  | 2 | 303 | 202 | 0 |  |  | fault cleared: counter and history unchanged (no record without a rising edge) | FAIL |
| 6 | 1 | 1 | 0 | 404 | 100 | 4 | 404 | 303 | 202 | 101 | 0 | 3 | 404 | 303 | 202 | 0 | 0 | fault 4 | FAIL |
| 7（保持 600 ms） | 0 | 1 | 0 | 0 | 100 | 4 | 404 | 303 | 202 | 101 |  | 3 | 404 | 303 | 202 | 0 |  | fault cleared: counter and history unchanged (no record without a rising edge) | FAIL |
| 8 | 1 | 1 | 0 | 505 | 100 | 5 | 505 | 404 | 303 | 202 | 101 | 4 | 505 | 404 | 303 | 202 | 0 | fault 5: history full | FAIL |
| 9（保持 600 ms） | 0 | 1 | 0 | 0 | 100 | 5 | 505 | 404 | 303 | 202 | 101 | 4 | 505 | 404 | 303 | 202 | 0 | fault cleared: counter and history unchanged (no record without a rising edge) | FAIL |
| 10 | 1 | 1 | 0 | 606 | 100 | 6 | 606 | 505 | 404 | 303 | 202 | 5 | 606 | 505 | 404 | 303 | 202 | fault 6: oldest dropped | FAIL |

### TC04 Runtime accumulates only during normal cutting

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Runtime accumulates only during normal cutting |
| 所属题目 | M06 Slab Thickness Alarm and Fault History（`M06_SlabThick`） |
| 初始状态 | power-up; CycleTime=1000 ms |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | accumulates when running and fault-free, preserved otherwise |
| 实际输出及结果 | ✅ 通过 |

| 周期 | THICKNESS_FAULT | THICKNESS_SIGNAL_VALID | CUTTING_RUN | FaultTimestamp | CycleTime | 预期 Slab_Runtime_Accumulator | 实际 Slab_Runtime_Accumulator | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 0 | 1000 | 1000 | 1000 | cutting | PASS |
| 1 | 0 | 1 | 1 | 0 | 1000 | 2000 | 2000 | accumulates | PASS |
| 2 | 0 | 1 | 0 | 0 | 1000 | 2000 | 2000 | stopped -> preserved | PASS |
| 3 | 1 | 1 | 1 | 10 | 1000 | 2000 | 2000 | fault -> not accumulated | PASS |
| 4 | 0 | 1 | 1 | 0 | 1000 | 3000 | 3000 | fault cleared -> accumulates | PASS |
| 5 | 0 | 0 | 1 | 0 | 1000 | 3000 | 3000 | invalid signal -> not accumulated | PASS |
| 6 | 0 | 1 | 1 | 0 | 1000 | 4000 | 4000 | valid again | PASS |

### TC05 Invalid signal clears the alarm and blocks recording

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC05 Invalid signal clears the alarm and blocks recording |
| 所属题目 | M06 Slab Thickness Alarm and Fault History（`M06_SlabThick`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | alarm off while invalid, nothing counted or recorded |
| 实际输出及结果 | ❌ 不通过；周期 0：Slab_Fault_Counter 预期 1，实际 0；Slab_Fault_History[0] 预期 11，实际 0；周期 1：Slab_Fault_Counter 预期 1，实际 0；周期 2：Slab_Fault_Counter 预期 1，实际 0；Slab_Fault_History[0] 预期 11，实际 0 |

| 周期 | THICKNESS_FAULT | THICKNESS_SIGNAL_VALID | CUTTING_RUN | FaultTimestamp | CycleTime | 预期 THICKNESS_ALARM | 预期 Slab_Fault_Counter | 预期 Slab_Fault_History[0] | 预期 Slab_Fault_History[1] | 预期 Slab_Fault_History[2] | 预期 Slab_Fault_History[3] | 预期 Slab_Fault_History[4] | 实际 THICKNESS_ALARM | 实际 Slab_Fault_Counter | 实际 Slab_Fault_History[0] | 实际 Slab_Fault_History[1] | 实际 Slab_Fault_History[2] | 实际 Slab_Fault_History[3] | 实际 Slab_Fault_History[4] | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 11 | 100 | 1 | 1 | 11 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | fault recorded | FAIL |
| 1 | 1 | 0 | 0 | 0 | 100 | 0 | 1 |  |  |  |  |  | 0 | 0 |  |  |  |  |  | invalid -> alarm off | FAIL |
| 2 | 1 | 0 | 0 | 22 | 100 |  | 1 | 11 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 | 0 | 0 | still invalid: not counted | FAIL |
| 3 | 0 | 0 | 0 | 0 | 100 | 0 |  |  |  |  |  |  | 0 |  |  |  |  |  |  | still invalid | PASS |
| 4 | 0 | 1 | 0 | 0 | 100 |  | 1 |  |  |  |  |  |  | 0 |  |  |  |  |  | valid again with no fault: nothing counted (alarm hold state is implementation-defined) | FAIL |


## M07 Office HVAC Multi-mode Energy-Saving Control（`M07_HVAC`）

- 编译：**未通过**（用例记为未通过）；用例通过 0/3；整题未通过

- 仿真器无法执行：期望 ':='，实际是 'SUPPLY_FAN_RUN'

### TC01 30-second fan start delay

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 30-second fan start delay |
| 所属题目 | M07 Office HVAC Multi-mode Energy-Saving Control（`M07_HVAC`） |
| 初始状态 | power-up: fan OFF, adjustment 0. Auto mode |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | power-up state, no run before 30s, run after 30s, stop on occupancy loss, full delay again |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'SUPPLY_FAN_RUN' |

| 周期 | OCCUPANCY_DETECTED | ENERGY_SAVING_MODE | HVAC_MODE_SELECTOR | 预期 SUPPLY_FAN_RUN | 预期 TEMP_SETPOINT_ADJUST | 实际 SUPPLY_FAN_RUN | 实际 TEMP_SETPOINT_ADJUST | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 2 |  |  | power-up, unoccupied auto standard -> +2 | FAIL |
| 1（保持 20000 ms） | 1 | 0 | 0 | 0 | 0 |  |  | occupancy -> delay starts, adjustment immediately 0 | 未执行 |
| 2（保持 9900 ms） | 1 | 0 | 0 | 0 |  |  |  | 20s: still waiting | 未执行 |
| 3（保持 200 ms） | 1 | 0 | 0 | 1 |  |  |  | 30s reached -> fan runs | 未执行 |
| 4 | 0 | 0 | 0 | 0 | 2 |  |  | occupancy lost -> fan stops immediately | 未执行 |
| 5（保持 20000 ms） | 1 | 0 | 0 | 0 |  |  |  | new occupancy: 20s is not enough | 未执行 |
| 6（保持 10200 ms） | 1 | 0 | 0 | 1 |  |  |  | full 30s -> fan runs again | 未执行 |

### TC02 Night mode blocks the fan

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Night mode blocks the fan |
| 所属题目 | M07 Office HVAC Multi-mode Energy-Saving Control（`M07_HVAC`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | night mode stops the fan and resets timing regardless of occupancy |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'SUPPLY_FAN_RUN' |

| 周期 | OCCUPANCY_DETECTED | ENERGY_SAVING_MODE | HVAC_MODE_SELECTOR | 预期 SUPPLY_FAN_RUN | 预期 TEMP_SETPOINT_ADJUST | 实际 SUPPLY_FAN_RUN | 实际 TEMP_SETPOINT_ADJUST | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|
| 0（保持 30200 ms） | 1 | 0 | 0 | 1 | 0 |  |  | auto occupied, fan running | FAIL |
| 1 | 1 | 0 | 3 | 0 | 4 |  |  | night mode -> fan stops immediately, +4 | 未执行 |
| 2（保持 31000 ms） | 1 | 0 | 3 | 0 | 4 |  |  | night mode: fan stays off even when occupied | 未执行 |
| 3 | 0 | 0 | 3 | 0 | 4 |  |  | night mode unoccupied -> still +4 | 未执行 |
| 4 | 1 | 0 | 0 | 0 | 0 |  |  | back to auto: full 30s required again | 未执行 |
| 5（保持 30200 ms） | 1 | 0 | 0 | 1 |  |  |  | 30s -> fan runs | 未执行 |

### TC03 Setpoint adjustment per mode

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Setpoint adjustment per mode |
| 所属题目 | M07 Office HVAC Multi-mode Energy-Saving Control（`M07_HVAC`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | all four modes, occupied and unoccupied, energy-saving affects Auto only, range within +-4 |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'SUPPLY_FAN_RUN' |

| 周期 | OCCUPANCY_DETECTED | ENERGY_SAVING_MODE | HVAC_MODE_SELECTOR | 预期 TEMP_SETPOINT_ADJUST | 实际 TEMP_SETPOINT_ADJUST | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 |  | auto occupied -> 0 | FAIL |
| 1 | 0 | 0 | 0 | 2 |  | auto unoccupied standard -> +2 | 未执行 |
| 2 | 0 | 1 | 0 | 3 |  | auto unoccupied energy-saving -> +3 | 未执行 |
| 3 | 1 | 0 | 1 | 0 |  | comfort occupied -> 0 | 未执行 |
| 4 | 0 | 0 | 1 | 1 |  | comfort unoccupied -> +1 | 未执行 |
| 5 | 0 | 1 | 1 | 1 |  | energy-saving does not affect comfort -> +1 | 未执行 |
| 6 | 1 | 0 | 2 | 0 |  | economy occupied -> 0 | 未执行 |
| 7 | 0 | 0 | 2 | 4 |  | economy unoccupied -> +4 | 未执行 |
| 8 | 0 | 1 | 2 | 4 |  | energy-saving does not affect economy -> +4 | 未执行 |
| 9 | 1 | 0 | 3 | 4 |  | night occupied -> +4 | 未执行 |
| 10 | 0 | 1 | 3 | 4 |  | night unoccupied energy-saving -> +4 | 未执行 |


## M08 IPv4 Parsing with Format and Range Checks（`M08_IPv4`）

- 编译：通过；用例通过 4/4；整题通过

### TC01 Valid addresses in network byte order

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Valid addresses in network byte order |
| 所属题目 | M08 IPv4 Parsing with Format and Range Checks（`M08_IPv4`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | typical address, first segment in the most significant byte, single digits, maximum segments |
| 实际输出及结果 | ✅ 通过 |

| 周期 | ipText | 预期 ipValue | 实际 ipValue | 检查内容 | 结果 |
|---|---|---|---|---|---|
| 0 | 192.168.1.1 | 3232235777 | 3232235777 | typical address | PASS |
| 1 | 1.2.3.4 | 16909060 | 16909060 | single digits, byte order check | PASS |
| 2 | 255.255.255.255 | 4294967295 | 4294967295 | all maximum segments | PASS |
| 3 | 10.0.0.255 | 167772415 | 167772415 | zeros in the middle | PASS |
| 4 | 127.0.0.1 | 2130706433 | 2130706433 | loopback | PASS |

### TC02 Zero address and leading zeros

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Zero address and leading zeros |
| 所属题目 | M08 IPv4 Parsing with Format and Range Checks（`M08_IPv4`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | 0.0.0.0 produces 0, leading zeros accepted as decimal |
| 实际输出及结果 | ✅ 通过 |

| 周期 | ipText | 预期 ipValue | 实际 ipValue | 检查内容 | 结果 |
|---|---|---|---|---|---|
| 0 | 0.0.0.0 | 0 | 0 | valid address 0.0.0.0 also produces 0 | PASS |
| 1 | 0.0.0.1 | 1 | 1 | smallest non-zero address | PASS |
| 2 | 010.001.000.009 | 167837705 | 167837705 | leading zeros are still decimal | PASS |

### TC03 Out-of-range segments

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Out-of-range segments |
| 所属题目 | M08 IPv4 Parsing with Format and Range Checks（`M08_IPv4`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | 256, 999, and a value just above the limit are rejected |
| 实际输出及结果 | ✅ 通过 |

| 周期 | ipText | 预期 ipValue | 实际 ipValue | 检查内容 | 结果 |
|---|---|---|---|---|---|
| 0 | 256.1.1.1 | 0 | 0 | first segment 256 > 255 | PASS |
| 1 | 1.256.1.1 | 0 | 0 | second segment out of range | PASS |
| 2 | 1.1.1.256 | 0 | 0 | last segment out of range | PASS |
| 3 | 999.999.999.999 | 0 | 0 | all segments out of range | PASS |
| 4 | 255.255.255.255 | 4294967295 | 4294967295 | 255 is still accepted | PASS |

### TC04 Malformed input

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Malformed input |
| 所属题目 | M08 IPv4 Parsing with Format and Range Checks（`M08_IPv4`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | wrong segment count, empty segments, non-digit characters, empty string |
| 实际输出及结果 | ✅ 通过 |

| 周期 | ipText | 预期 ipValue | 实际 ipValue | 检查内容 | 结果 |
|---|---|---|---|---|---|
| 0 | 1.2.3 | 0 | 0 | only three segments | PASS |
| 1 | 1.2.3.4.5 | 0 | 0 | five segments | PASS |
| 2 | 1.2..4 | 0 | 0 | empty segment | PASS |
| 3 | .1.2.3 | 0 | 0 | leading period | PASS |
| 4 | 1.2.3. | 0 | 0 | trailing period | PASS |
| 5 | 1.2.3.a | 0 | 0 | non-digit character | PASS |
| 6 | 192,168,1,1 | 0 | 0 | wrong separator | PASS |
| 7 |  | 0 | 0 | empty string | PASS |
| 8 | 1234 | 0 | 0 | no separators at all | PASS |
| 9 | 1.2.3.4  | 0 | 0 | trailing space is not a digit | PASS |


## H01 Material Proportioning Process Control（`H01_Proportion`）

- 编译：通过；用例通过 6/6；整题通过

### TC01 Manual mode: toggle on rising edge

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Manual mode: toggle on rising edge |
| 所属题目 | H01 Material Proportioning Process Control（`H01_Proportion`） |
| 初始状态 | power-up, estop=1 (not triggered), opeMode=0 (manual), all buttons released |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | each device toggles ON on a rising edge, holding the button does not re-toggle, second press turns OFF, devices independent |
| 实际输出及结果 | ✅ 通过 |

| 周期 | estop | opeMode | valveAStart | valveBStart | valveCStart | valveDStart | mixMotorStart | autoStart | processMode | levelSensor | mixMotorComplete | 预期 valveARun | 预期 valveBRun | 预期 valveCRun | 预期 valveDRun | 预期 mixMotorRun | 实际 valveARun | 实际 valveBRun | 实际 valveCRun | 实际 valveDRun | 实际 mixMotorRun | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | all OFF | PASS |
| 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | rising edge of valveAStart -> A ON | PASS |
| 2 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | button held -> no re-toggle, A stays ON | PASS |
| 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | button released -> A stays ON | PASS |
| 4 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | B and mixer toggled ON, A unaffected | PASS |
| 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | hold | PASS |
| 6 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | second press -> A OFF | PASS |
| 7 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | C and D ON | PASS |
| 8 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | buttons released, all stay | PASS |
| 9 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | second press on all -> all OFF | PASS |
| 10 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 100 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | auto inputs have no effect in manual | PASS |

### TC02 Automatic mode, processMode=FALSE (A -> B -> mix -> D)

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Automatic mode, processMode=FALSE (A -> B -> mix -> D) |
| 所属题目 | H01 Material Proportioning Process Control（`H01_Proportion`） |
| 初始状态 | power-up, estop=1, opeMode=1, processMode=0, levelSensor=0 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | autoStart opens A, level 50 switches to B, level 80 closes B and starts mixer (C skipped), mixComplete stops mixer and opens D |
| 实际输出及结果 | ✅ 通过 |

| 周期 | estop | opeMode | valveAStart | valveBStart | valveCStart | valveDStart | mixMotorStart | autoStart | processMode | levelSensor | mixMotorComplete | 预期 valveARun | 预期 valveBRun | 预期 valveCRun | 预期 valveDRun | 预期 mixMotorRun | 实际 valveARun | 实际 valveBRun | 实际 valveCRun | 实际 valveDRun | 实际 mixMotorRun | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | auto idle, nothing runs | PASS |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | autoStart -> valve A opens | PASS |
| 2 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 20 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | filling, A stays open after button released | PASS |
| 3 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 49 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | just below 50 -> A still open | PASS |
| 4 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 50 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | level 50 -> A closes, B opens | PASS |
| 5 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 65 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | filling B | PASS |
| 6 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 80 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | level 80 -> B closes; processMode=0 -> mixer starts, C not opened | PASS |
| 7 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 80 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | mixing | PASS |
| 8 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 80 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | mix complete -> mixer OFF, valve D opens, process ends | PASS |

### TC03 Automatic mode, processMode=TRUE (A -> B -> C -> mix -> D)

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Automatic mode, processMode=TRUE (A -> B -> C -> mix -> D) |
| 所属题目 | H01 Material Proportioning Process Control（`H01_Proportion`） |
| 初始状态 | power-up, estop=1, opeMode=1, processMode=1, levelSensor=0 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | third material through C until level 100, then mixer and D |
| 实际输出及结果 | ✅ 通过 |

| 周期 | estop | opeMode | valveAStart | valveBStart | valveCStart | valveDStart | mixMotorStart | autoStart | processMode | levelSensor | mixMotorComplete | 预期 valveARun | 预期 valveBRun | 预期 valveCRun | 预期 valveDRun | 预期 mixMotorRun | 实际 valveARun | 实际 valveBRun | 实际 valveCRun | 实际 valveDRun | 实际 mixMotorRun | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | autoStart -> A | PASS |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 50 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 50 -> B | PASS |
| 2 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 80 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 80 -> B closes, processMode=1 -> C opens, mixer not yet | PASS |
| 3 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 99 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | below 100 -> C still open | PASS |
| 4 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 100 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 100 -> C closes, mixer starts | PASS |
| 5 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 100 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | mix complete -> mixer OFF, D opens | PASS |

### TC04 Emergency stop in automatic mode

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Emergency stop in automatic mode |
| 所属题目 | H01 Material Proportioning Process Control（`H01_Proportion`） |
| 初始状态 | power-up, estop=1, opeMode=1 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | estop=0 stops everything immediately, outputs stay OFF while estop is held, sequence does not resume by itself after release, new autoStart restarts from A |
| 实际输出及结果 | ✅ 通过 |

| 周期 | estop | opeMode | valveAStart | valveBStart | valveCStart | valveDStart | mixMotorStart | autoStart | processMode | levelSensor | mixMotorComplete | 预期 valveARun | 预期 valveBRun | 预期 valveCRun | 预期 valveDRun | 预期 mixMotorRun | 实际 valveARun | 实际 valveBRun | 实际 valveCRun | 实际 valveDRun | 实际 mixMotorRun | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | start | PASS |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 50 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | B phase | PASS |
| 2 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 80 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | mixer running | PASS |
| 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 80 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ESTOP -> all OFF immediately | PASS |
| 4 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 80 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | while estop held, nothing can start | PASS |
| 5 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 80 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | estop released -> stays OFF, no automatic resume | PASS |
| 6 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | new autoStart restarts from valve A | PASS |

### TC05 Emergency stop in manual mode

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC05 Emergency stop in manual mode |
| 所属题目 | H01 Material Proportioning Process Control（`H01_Proportion`） |
| 初始状态 | power-up, estop=1, opeMode=0 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | running devices are stopped by estop, buttons ignored during estop, after release devices stay OFF until toggled again |
| 实际输出及结果 | ✅ 通过 |

| 周期 | estop | opeMode | valveAStart | valveBStart | valveCStart | valveDStart | mixMotorStart | autoStart | processMode | levelSensor | mixMotorComplete | 预期 valveARun | 预期 valveBRun | 预期 valveCRun | 预期 valveDRun | 预期 mixMotorRun | 实际 valveARun | 实际 valveBRun | 实际 valveCRun | 实际 valveDRun | 实际 mixMotorRun | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | A and mixer ON | PASS |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | hold | PASS |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ESTOP -> all OFF | PASS |
| 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | button during estop ignored | PASS |
| 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | estop released -> all remain OFF | PASS |
| 5 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | toggle works again after release | PASS |

### TC06 Automatic mode ignores manual buttons; autoStart only starts when idle

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC06 Automatic mode ignores manual buttons; autoStart only starts when idle |
| 所属题目 | H01 Material Proportioning Process Control（`H01_Proportion`） |
| 初始状态 | power-up, estop=1, opeMode=1 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | manual buttons have no effect in auto, pressing autoStart during a running sequence does not restart it |
| 实际输出及结果 | ✅ 通过 |

| 周期 | estop | opeMode | valveAStart | valveBStart | valveCStart | valveDStart | mixMotorStart | autoStart | processMode | levelSensor | mixMotorComplete | 预期 valveARun | 预期 valveBRun | 预期 valveCRun | 预期 valveDRun | 预期 mixMotorRun | 实际 valveARun | 实际 valveBRun | 实际 valveCRun | 实际 valveDRun | 实际 mixMotorRun | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | manual buttons ignored in auto | PASS |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | start | PASS |
| 2 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 50 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | B phase | PASS |
| 3 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 60 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | autoStart during sequence -> no restart, still B | PASS |
| 4 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 60 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | manual C button ignored | PASS |


## H02 Flexible Processing Control（`H02_FlexProcess`）

- 编译：**未通过**（用例记为未通过）；用例通过 0/3；整题未通过

- 仿真器无法执行：期望 ':='，实际是 'edgeStart'

### TC01 Simple route 1 -> 3 -> 5

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Simple route 1 -> 3 -> 5 |
| 所属题目 | H02 Flexible Processing Control（`H02_FlexProcess`） |
| 初始状态 | power-up, material at station 1, processSequence = [3,5], processLength = 2 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | start at station 1, move right to the first processing station, continue after completion, stop at station 5 |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'edgeStart' |

| 周期 | processLength | processSequence[1] | processSequence[2] | processSequence[3] | processSequence[4] | processSequence[5] | processSequence[6] | processSequence[7] | processSequence[8] | sensor1 | sensor2 | sensor3 | sensor4 | sensor5 | station1Start | station2Complete | station3Complete | station4Complete | 预期 conveyorLeft | 预期 conveyorRight | 实际 conveyorLeft | 实际 conveyorRight | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 2 | 3 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | material at station 1, start not pressed -> conveyor stopped | FAIL |
| 1 | 2 | 3 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |  |  | start pressed -> move right toward station 3 | 未执行 |
| 2 | 2 | 3 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  | in transit | 未执行 |
| 3 | 2 | 3 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | arrived at station 3 -> conveyor stops | 未执行 |
| 4 | 2 | 3 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | processing, no completion signal yet | 未执行 |
| 5 | 2 | 3 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |  |  | station 3 complete -> move right toward station 5 | 未执行 |
| 6 | 2 | 3 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  | in transit | 未执行 |
| 7 | 2 | 3 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | arrived at station 5 -> stop, production finished | 未执行 |

### TC02 Route requiring a leftward move 1 -> 4 -> 2 -> 5

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Route requiring a leftward move 1 -> 4 -> 2 -> 5 |
| 所属题目 | H02 Flexible Processing Control（`H02_FlexProcess`） |
| 初始状态 | power-up, material at station 1, processSequence = [4,2,5], processLength = 3 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | direction decided from the current and next station numbers, left movement |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'edgeStart' |

| 周期 | processLength | processSequence[1] | processSequence[2] | processSequence[3] | processSequence[4] | processSequence[5] | processSequence[6] | processSequence[7] | processSequence[8] | sensor1 | sensor2 | sensor3 | sensor4 | sensor5 | station1Start | station2Complete | station3Complete | station4Complete | 预期 conveyorLeft | 预期 conveyorRight | 实际 conveyorLeft | 实际 conveyorRight | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 3 | 4 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |  |  | start -> right toward station 4 | FAIL |
| 1 | 3 | 4 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | arrived at station 4 | 未执行 |
| 2 | 3 | 4 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 |  |  | station 4 complete, next is station 2 -> move LEFT | 未执行 |
| 3 | 3 | 4 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |  |  | in transit leftwards | 未执行 |
| 4 | 3 | 4 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | arrived at station 2 -> stop | 未执行 |
| 5 | 3 | 4 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |  |  | station 2 complete, next is station 5 -> move right | 未执行 |
| 6 | 3 | 4 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | arrived at station 5 -> stop | 未执行 |

### TC03 Wrong signals are ignored

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Wrong signals are ignored |
| 所属题目 | H02 Flexible Processing Control（`H02_FlexProcess`） |
| 初始状态 | power-up, processSequence = [2,5], processLength = 2 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | completion signal from a station the product is not at, start without material, conveyor never runs in both directions |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'edgeStart' |

| 周期 | processLength | processSequence[1] | processSequence[2] | processSequence[3] | processSequence[4] | processSequence[5] | processSequence[6] | processSequence[7] | processSequence[8] | sensor1 | sensor2 | sensor3 | sensor4 | sensor5 | station1Start | station2Complete | station3Complete | station4Complete | 预期 conveyorLeft | 预期 conveyorRight | 实际 conveyorLeft | 实际 conveyorRight | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 2 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  |  | start without material at station 1 -> nothing | FAIL |
| 1 | 2 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |  |  | completion signals before the product arrives are ignored | 未执行 |
| 2 | 2 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |  |  | correct start -> move right | 未执行 |
| 3 | 2 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | arrived at station 2 | 未执行 |
| 4 | 2 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |  |  | completion from stations 3/4 ignored at station 2 | 未执行 |
| 5 | 2 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |  |  | correct completion -> move right to station 5 | 未执行 |


## H03 Recipe Management System（`H03_RecipeMgr`）

- 编译：通过；用例通过 3/3；整题通过

### TC01 Add recipes and reject duplicates

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Add recipes and reject duplicates |
| 所属题目 | H03 Recipe Management System（`H03_RecipeMgr`） |
| 初始状态 | power-up, empty database (all recipeID = 0) |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | add into the lowest free slot, duplicate ID -> 16#8002 |
| 实际输出及结果 | ✅ 通过 |

| 周期 | addRecipe | deleteRecipe | modifyRecipe | queryRecipe | recipeIn.recipeID | recipeIn.ingredientType | recipeIn.ingredientRatio | recipeIn.productionTemperature | 预期 recipeAdded | 预期 error | 预期 status | 实际 recipeAdded | 实际 error | 实际 status | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 101 | 1 | 0.5 | 180.0 | 1 | 0 | 0 | 1 | 0 | 0 | first recipe added | PASS |
| 1 | 0 | 0 | 0 | 0 | 101 | 1 | 0.5 | 180.0 |  | 0 | 0 |  | 0 | 0 | request released | PASS |
| 2 | 1 | 0 | 0 | 0 | 102 | 2 | 0.3 | 200.0 | 1 | 0 | 0 | 1 | 0 | 0 | second recipe added | PASS |
| 3 | 0 | 0 | 0 | 0 | 102 | 2 | 0.3 | 200.0 |  | 0 | 0 |  | 0 | 0 | released | PASS |
| 4 | 1 | 0 | 0 | 0 | 101 | 9 | 0.9 | 90.0 |  | 1 | 32770 |  | 1 | 32770 | duplicate recipe number -> 16#8002 | PASS |

### TC02 Query existing and missing recipes

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Query existing and missing recipes |
| 所属题目 | H03 Recipe Management System（`H03_RecipeMgr`） |
| 初始状态 | database contains 101 and 102 from TC01-like preparation |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | query returns all fields, missing ID -> 16#8001 |
| 实际输出及结果 | ✅ 通过 |

| 周期 | addRecipe | deleteRecipe | modifyRecipe | queryRecipe | recipeIn.recipeID | recipeIn.ingredientType | recipeIn.ingredientRatio | recipeIn.productionTemperature | 预期 recipeAdded | 预期 error | 预期 status | 预期 recipeQueryResult.recipeID | 预期 recipeQueryResult.ingredientType | 预期 recipeQueryResult.ingredientRatio | 预期 recipeQueryResult.productionTemperature | 实际 recipeAdded | 实际 error | 实际 status | 实际 recipeQueryResult.recipeID | 实际 recipeQueryResult.ingredientType | 实际 recipeQueryResult.ingredientRatio | 实际 recipeQueryResult.productionTemperature | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 101 | 1 | 0.5 | 180.0 | 1 |  |  |  |  |  |  | 1 |  |  |  |  |  |  | prepare: add 101 | PASS |
| 1 | 0 | 0 | 0 | 0 | 101 | 1 | 0.5 | 180.0 |  | 0 | 0 |  |  |  |  |  | 0 | 0 |  |  |  |  | released | PASS |
| 2 | 0 | 0 | 0 | 1 | 101 | 0 | 0.0 | 0.0 |  | 0 | 0 | 101 | 1 | 0.5 | 180.0 |  | 0 | 0 | 101 | 1 | 0.5 | 180.0 | query 101 returns the stored recipe | PASS |
| 3 | 0 | 0 | 0 | 0 | 101 | 0 | 0.0 | 0.0 |  | 0 | 0 |  |  |  |  |  | 0 | 0 |  |  |  |  | released | PASS |
| 4 | 0 | 0 | 0 | 1 | 999 | 0 | 0.0 | 0.0 |  | 1 | 32769 |  |  |  |  |  | 1 | 32769 |  |  |  |  | query a missing number -> 16#8001 | PASS |

### TC03 Modify and delete

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Modify and delete |
| 所属题目 | H03 Recipe Management System（`H03_RecipeMgr`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | modify replaces the stored recipe, delete clears the slot, errors 16#8005 and 16#8004 for missing numbers |
| 实际输出及结果 | ✅ 通过 |

| 周期 | addRecipe | deleteRecipe | modifyRecipe | queryRecipe | recipeIn.recipeID | recipeIn.ingredientType | recipeIn.ingredientRatio | recipeIn.productionTemperature | 预期 recipeAdded | 预期 error | 预期 status | 预期 recipeModified | 预期 recipeQueryResult.recipeID | 预期 recipeQueryResult.ingredientType | 预期 recipeQueryResult.ingredientRatio | 预期 recipeQueryResult.productionTemperature | 预期 recipeDeleted | 实际 recipeAdded | 实际 error | 实际 status | 实际 recipeModified | 实际 recipeQueryResult.recipeID | 实际 recipeQueryResult.ingredientType | 实际 recipeQueryResult.ingredientRatio | 实际 recipeQueryResult.productionTemperature | 实际 recipeDeleted | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 101 | 1 | 0.5 | 180.0 | 1 |  |  |  |  |  |  |  |  | 1 |  |  |  |  |  |  |  |  | prepare | PASS |
| 1 | 0 | 0 | 0 | 0 | 101 | 1 | 0.5 | 180.0 |  | 0 | 0 |  |  |  |  |  |  |  | 0 | 0 |  |  |  |  |  |  | released | PASS |
| 2 | 0 | 0 | 1 | 0 | 101 | 7 | 0.8 | 220.0 |  | 0 | 0 | 1 |  |  |  |  |  |  | 0 | 0 | 1 |  |  |  |  |  | modify 101 | PASS |
| 3 | 0 | 0 | 0 | 0 | 101 | 7 | 0.8 | 220.0 |  | 0 | 0 |  |  |  |  |  |  |  | 0 | 0 |  |  |  |  |  |  | released | PASS |
| 4 | 0 | 0 | 0 | 1 | 101 | 0 | 0.0 | 0.0 |  |  |  |  | 101 | 7 | 0.8 | 220.0 |  |  |  |  |  | 101 | 7 | 0.8 | 220.0 |  | query shows the modified values | PASS |
| 5 | 0 | 0 | 0 | 0 | 101 | 0 | 0.0 | 0.0 |  | 0 | 0 |  |  |  |  |  |  |  | 0 | 0 |  |  |  |  |  |  | released | PASS |
| 6 | 0 | 0 | 1 | 0 | 777 | 0 | 0.0 | 0.0 |  | 1 | 32773 |  |  |  |  |  |  |  | 1 | 32773 |  |  |  |  |  |  | modify a missing number -> 16#8005 | PASS |
| 7 | 0 | 0 | 0 | 0 | 777 | 0 | 0.0 | 0.0 |  | 0 | 0 |  |  |  |  |  |  |  | 0 | 0 |  |  |  |  |  |  | released | PASS |
| 8 | 0 | 1 | 0 | 0 | 101 | 0 | 0.0 | 0.0 |  | 0 | 0 |  |  |  |  |  | 1 |  | 0 | 0 |  |  |  |  |  | 1 | delete 101 | PASS |
| 9 | 0 | 0 | 0 | 0 | 101 | 0 | 0.0 | 0.0 |  | 0 | 0 |  |  |  |  |  |  |  | 0 | 0 |  |  |  |  |  |  | released | PASS |
| 10 | 0 | 0 | 0 | 1 | 101 | 0 | 0.0 | 0.0 |  | 1 | 32769 |  |  |  |  |  |  |  | 1 | 32769 |  |  |  |  |  |  | deleted recipe can no longer be queried | PASS |
| 11 | 0 | 0 | 0 | 0 | 101 | 0 | 0.0 | 0.0 |  | 0 | 0 |  |  |  |  |  |  |  | 0 | 0 |  |  |  |  |  |  | released | PASS |
| 12 | 0 | 1 | 0 | 0 | 101 | 0 | 0.0 | 0.0 |  | 1 | 32772 |  |  |  |  |  |  |  | 1 | 32772 |  |  |  |  |  |  | delete a missing number -> 16#8004 | PASS |


## H04 FIFO First-In-First-Out Queue（`H04_FIFO`）

- 编译：通过；用例通过 5/5；整题通过

### TC01 Basic enqueue and dequeue in FIFO order

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Basic enqueue and dequeue in FIFO order |
| 所属题目 | H04 FIFO First-In-First-Out Queue（`H04_FIFO`） |
| 初始状态 | power-up: queue empty, elementCount 0, capacity 5 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | one operation per rising edge, held signal does not repeat, values come out in insertion order |
| 实际输出及结果 | ✅ 通过 |

| 周期 | enqueue | dequeue | reset | item | 预期 elementCount | 预期 status | 预期 item | 实际 elementCount | 实际 status | 实际 item | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 |  | 0 | 0 |  | 0 | 0 |  | power-up: empty | PASS |
| 1 | 1 | 0 | 0 | 11 | 1 | 0 |  | 1 | 0 |  | enqueue 11 | PASS |
| 2 | 1 | 0 | 0 | 99 | 1 |  |  | 1 |  |  | signal held -> no second enqueue | PASS |
| 3 | 0 | 0 | 0 | 99 | 1 |  |  | 1 |  |  | released | PASS |
| 4 | 1 | 0 | 0 | 22 | 2 |  |  | 2 |  |  | enqueue 22 | PASS |
| 5 | 0 | 0 | 0 |  | 2 |  |  | 2 |  |  | released | PASS |
| 6 | 0 | 1 | 0 |  | 1 | 0 | 11 | 1 | 0 | 11 | dequeue returns the first value 11 | PASS |
| 7 | 0 | 0 | 0 |  | 1 |  |  | 1 |  |  | released | PASS |
| 8 | 0 | 1 | 0 |  | 0 |  | 22 | 0 |  | 22 | dequeue returns 22, queue empty | PASS |

### TC02 Full queue rejects an enqueue

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Full queue rejects an enqueue |
| 所属题目 | H04 FIFO First-In-First-Out Queue（`H04_FIFO`） |
| 初始状态 | power-up, capacity 8 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | capacity 8 reached, 16#8002 reported, count unchanged, space freed by a dequeue |
| 实际输出及结果 | ✅ 通过 |

| 周期 | enqueue | dequeue | reset | item | 预期 elementCount | 预期 status | 预期 item | 实际 elementCount | 实际 status | 实际 item | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 1 | 0 |  | 1 | 0 |  | enqueue 1 | PASS |
| 1 | 0 | 0 | 0 | 1 | 1 |  |  | 1 |  |  | release | PASS |
| 2 | 1 | 0 | 0 | 2 | 2 | 0 |  | 2 | 0 |  | enqueue 2 | PASS |
| 3 | 0 | 0 | 0 | 2 | 2 |  |  | 2 |  |  | release | PASS |
| 4 | 1 | 0 | 0 | 3 | 3 | 0 |  | 3 | 0 |  | enqueue 3 | PASS |
| 5 | 0 | 0 | 0 | 3 | 3 |  |  | 3 |  |  | release | PASS |
| 6 | 1 | 0 | 0 | 4 | 4 | 0 |  | 4 | 0 |  | enqueue 4 | PASS |
| 7 | 0 | 0 | 0 | 4 | 4 |  |  | 4 |  |  | release | PASS |
| 8 | 1 | 0 | 0 | 5 | 5 | 0 |  | 5 | 0 |  | enqueue 5 | PASS |
| 9 | 0 | 0 | 0 | 5 | 5 |  |  | 5 |  |  | release | PASS |
| 10 | 1 | 0 | 0 | 6 | 6 | 0 |  | 6 | 0 |  | enqueue 6 | PASS |
| 11 | 0 | 0 | 0 | 6 | 6 |  |  | 6 |  |  | release | PASS |
| 12 | 1 | 0 | 0 | 7 | 7 | 0 |  | 7 | 0 |  | enqueue 7 | PASS |
| 13 | 0 | 0 | 0 | 7 | 7 |  |  | 7 |  |  | release | PASS |
| 14 | 1 | 0 | 0 | 8 | 8 | 0 |  | 8 | 0 |  | enqueue 8 | PASS |
| 15 | 0 | 0 | 0 | 8 | 8 |  |  | 8 |  |  | release | PASS |
| 16 | 1 | 0 | 0 | 99 | 8 | 32770 | 99 | 8 | 32770 | 99 | enqueue into a full queue -> 16#8002, unchanged | PASS |
| 17 | 0 | 0 | 0 | 99 | 8 |  |  | 8 |  |  | release | PASS |
| 18 | 0 | 1 | 0 |  | 7 | 0 | 1 | 7 | 0 | 1 | dequeue frees a slot, FIFO order returns 1 | PASS |
| 19 | 0 | 0 | 0 |  | 7 |  |  | 7 |  |  | release | PASS |
| 20 | 1 | 0 | 0 | 9 | 8 | 0 |  | 8 | 0 |  | enqueue succeeds again (wrap-around) | PASS |

### TC03 Empty queue rejects a dequeue

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Empty queue rejects a dequeue |
| 所属题目 | H04 FIFO First-In-First-Out Queue（`H04_FIFO`） |
| 初始状态 | power-up, queue empty |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | 16#8001 reported, item unchanged, count stays zero |
| 实际输出及结果 | ✅ 通过 |

| 周期 | enqueue | dequeue | reset | item | 预期 elementCount | 预期 status | 预期 item | 实际 elementCount | 实际 status | 实际 item | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 77 | 0 | 32769 | 77 | 0 | 32769 | 77 | dequeue from an empty queue -> 16#8001, item unchanged | PASS |
| 1 | 0 | 0 | 0 | 77 | 0 |  |  | 0 |  |  | release | PASS |
| 2 | 1 | 0 | 0 | 33 | 1 | 0 |  | 1 | 0 |  | enqueue works | PASS |
| 3 | 0 | 0 | 0 | 33 | 1 |  |  | 1 |  |  | release | PASS |
| 4 | 0 | 1 | 0 |  | 0 | 0 | 33 | 0 | 0 | 33 | dequeue returns 33 | PASS |
| 5 | 0 | 0 | 0 |  | 0 |  |  | 0 |  |  | release | PASS |
| 6 | 0 | 1 | 0 |  | 0 | 32769 |  | 0 | 32769 |  | empty again -> 16#8001 | PASS |

### TC04 Reset has priority and empties the queue

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Reset has priority and empties the queue |
| 所属题目 | H04 FIFO First-In-First-Out Queue（`H04_FIFO`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | reset clears the count, takes priority over enqueue/dequeue, status stays 16#0000 |
| 实际输出及结果 | ✅ 通过 |

| 周期 | enqueue | dequeue | reset | item | 预期 elementCount | 预期 status | 实际 elementCount | 实际 status | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 5 | 1 |  | 1 |  | enqueue | PASS |
| 1 | 0 | 0 | 0 | 5 | 1 |  | 1 |  | release | PASS |
| 2 | 1 | 0 | 0 | 6 | 2 |  | 2 |  | enqueue | PASS |
| 3 | 0 | 0 | 0 | 6 | 2 |  | 2 |  | release | PASS |
| 4 | 0 | 0 | 1 |  | 0 | 0 | 0 | 0 | reset -> empty, no error | PASS |
| 5 | 1 | 0 | 1 | 9 | 0 | 0 | 0 | 0 | reset has priority over enqueue | PASS |
| 6 | 0 | 0 | 0 |  | 0 |  | 0 |  | release | PASS |
| 7 | 0 | 1 | 0 |  | 0 | 32769 | 0 | 32769 | queue really is empty | PASS |
| 8 | 0 | 0 | 0 |  | 0 |  | 0 |  | release | PASS |
| 9 | 1 | 0 | 0 | 8 | 1 | 0 | 1 | 0 | queue usable after reset | PASS |

### TC05 Circular wrap-around keeps FIFO order

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC05 Circular wrap-around keeps FIFO order |
| 所属题目 | H04 FIFO First-In-First-Out Queue（`H04_FIFO`） |
| 初始状态 | power-up, capacity 5 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | repeated enqueue/dequeue cycles past the end of the buffer |
| 实际输出及结果 | ✅ 通过 |

| 周期 | enqueue | dequeue | reset | item | 预期 elementCount | 预期 item | 实际 elementCount | 实际 item | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 1 |  | 1 |  | in 1 | PASS |
| 1 | 0 | 0 | 0 | 1 | 1 |  | 1 |  | release | PASS |
| 2 | 1 | 0 | 0 | 2 | 2 |  | 2 |  | in 2 | PASS |
| 3 | 0 | 0 | 0 | 2 | 2 |  | 2 |  | release | PASS |
| 4 | 1 | 0 | 0 | 3 | 3 |  | 3 |  | in 3 | PASS |
| 5 | 0 | 0 | 0 | 3 | 3 |  | 3 |  | release | PASS |
| 6 | 0 | 1 | 0 |  | 2 | 1 | 2 | 1 | out 1 | PASS |
| 7 | 0 | 0 | 0 |  | 2 |  | 2 |  | release | PASS |
| 8 | 0 | 1 | 0 |  | 1 | 2 | 1 | 2 | out 2 | PASS |
| 9 | 0 | 0 | 0 |  | 1 |  | 1 |  | release | PASS |
| 10 | 1 | 0 | 0 | 4 | 2 |  | 2 |  | in 4 (wraps) | PASS |
| 11 | 0 | 0 | 0 | 4 | 2 |  | 2 |  | release | PASS |
| 12 | 1 | 0 | 0 | 5 | 3 |  | 3 |  | in 5 | PASS |
| 13 | 0 | 0 | 0 | 5 | 3 |  | 3 |  | release | PASS |
| 14 | 0 | 1 | 0 |  | 2 | 3 | 2 | 3 | out 3 - order preserved across the wrap | PASS |
| 15 | 0 | 0 | 0 |  | 2 |  | 2 |  | release | PASS |
| 16 | 0 | 1 | 0 |  | 1 | 4 | 1 | 4 | out 4 | PASS |
| 17 | 0 | 0 | 0 |  | 1 |  | 1 |  | release | PASS |
| 18 | 0 | 1 | 0 |  | 0 | 5 | 0 | 5 | out 5, queue empty | PASS |


## H05 Mechanical Arm Control（`H05_MechArm`）

- 编译：通过；用例通过 7/7；整题通过

### TC01 Manual mode: each button moves until its limit switch

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Manual mode: each button moves until its limit switch |
| 所属题目 | H05 Mechanical Arm Control（`H05_MechArm`） |
| 初始状态 | power-up, EmergencyStop=1 (inactive), ManualMode=1, arm at home (top-left, released) |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | button pressed & not in position -> move; in position -> no move; release -> stop; all six actions; Start ignored |
| 实际输出及结果 | ✅ 通过 |

| 周期 | ManualMode | SingleStepMode | SingleCycleMode | ContinuousMode | EmergencyStop | Start | DownButton | UpButton | LeftButton | RightButton | GripButton | ReleaseButton | DownLimitSwitch | UpLimitSwitch | LeftLimitSwitch | RightLimitSwitch | GripLimitSwitch | ReleaseLimitSwitch | 预期 MoveDown | 预期 MoveUp | 预期 MoveLeft | 预期 MoveRight | 预期 ActivateGrip | 预期 ActivateRelease | 实际 MoveDown | 实际 MoveUp | 实际 MoveLeft | 实际 MoveRight | 实际 ActivateGrip | 实际 ActivateRelease | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | no button -> no motion | PASS |
| 1 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | DownButton, not at down limit -> MoveDown | PASS |
| 2 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | still moving down (up switch released) | PASS |
| 3 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | down limit reached -> stop although button held | PASS |
| 4 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | button released | PASS |
| 5 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | UpButton -> MoveUp | PASS |
| 6 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | button released mid-way -> stop | PASS |
| 7 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | UpButton at up limit -> no motion | PASS |
| 8 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | RightButton, not at right limit -> MoveRight | PASS |
| 9 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | LeftButton at left limit -> no motion | PASS |
| 10 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | GripButton, not gripped -> ActivateGrip | PASS |
| 11 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ReleaseButton while already released -> no action | PASS |
| 12 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | ReleaseButton while gripped -> ActivateRelease | PASS |
| 13 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Start has no effect in manual mode | PASS |

### TC02 Single-step mode: one action per Start press

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Single-step mode: one action per Start press |
| 所属题目 | H05 Mechanical Arm Control（`H05_MechArm`） |
| 初始状态 | power-up, SingleStepMode=1, arm at home |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | eight actions each started by Start, each stops at its limit and waits; Start held does not start the next action |
| 实际输出及结果 | ✅ 通过 |

| 周期 | ManualMode | SingleStepMode | SingleCycleMode | ContinuousMode | EmergencyStop | Start | DownButton | UpButton | LeftButton | RightButton | GripButton | ReleaseButton | DownLimitSwitch | UpLimitSwitch | LeftLimitSwitch | RightLimitSwitch | GripLimitSwitch | ReleaseLimitSwitch | 预期 MoveDown | 预期 MoveUp | 预期 MoveLeft | 预期 MoveRight | 预期 ActivateGrip | 预期 ActivateRelease | 实际 MoveDown | 实际 MoveUp | 实际 MoveLeft | 实际 MoveRight | 实际 ActivateGrip | 实际 ActivateRelease | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Start -> down begins | PASS |
| 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | down: moving, Start released | PASS |
| 2 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | down: in motion | PASS |
| 3 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | down limit reached -> stop, wait for Start | PASS |
| 4 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | Start -> grip begins | PASS |
| 5 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | grip: moving, Start released | PASS |
| 6 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | grip: in motion | PASS |
| 7 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | grip limit reached -> stop, wait for Start | PASS |
| 8 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | Start -> up begins | PASS |
| 9 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | up: moving, Start released | PASS |
| 10 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | up: in motion | PASS |
| 11 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | up limit reached -> stop, wait for Start | PASS |
| 12 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | Start -> right begins | PASS |
| 13 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | right: moving, Start released | PASS |
| 14 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | right: in motion | PASS |
| 15 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | right limit reached -> stop, wait for Start | PASS |
| 16 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Start -> down begins | PASS |
| 17 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | down: moving, Start released | PASS |
| 18 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | down: in motion | PASS |
| 19 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | down limit reached -> stop, wait for Start | PASS |
| 20 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | Start -> release begins | PASS |
| 21 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | release: moving, Start released | PASS |
| 22 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | release: in motion | PASS |
| 23 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | release limit reached -> stop, wait for Start | PASS |
| 24 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | Start -> up begins | PASS |
| 25 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | up: moving, Start released | PASS |
| 26 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | up: in motion | PASS |
| 27 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | up limit reached -> stop, wait for Start | PASS |
| 28 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | Start -> left begins | PASS |
| 29 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | left: moving, Start released | PASS |
| 30 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | left: in motion | PASS |
| 31 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | left limit reached -> stop, wait for Start | PASS |

### TC03 Single-cycle mode: one Start runs the whole cycle and stops at home

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Single-cycle mode: one Start runs the whole cycle and stops at home |
| 所属题目 | H05 Mechanical Arm Control（`H05_MechArm`） |
| 初始状态 | power-up, SingleCycleMode=1, arm at home |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | automatic chaining of all eight actions, stops at home, waits for Start |
| 实际输出及结果 | ✅ 通过 |

| 周期 | ManualMode | SingleStepMode | SingleCycleMode | ContinuousMode | EmergencyStop | Start | DownButton | UpButton | LeftButton | RightButton | GripButton | ReleaseButton | DownLimitSwitch | UpLimitSwitch | LeftLimitSwitch | RightLimitSwitch | GripLimitSwitch | ReleaseLimitSwitch | 预期 MoveDown | 预期 MoveUp | 预期 MoveLeft | 预期 MoveRight | 预期 ActivateGrip | 预期 ActivateRelease | 实际 MoveDown | 实际 MoveUp | 实际 MoveLeft | 实际 MoveRight | 实际 ActivateGrip | 实际 ActivateRelease | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Start -> down begins | PASS |
| 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | down: moving, Start released | PASS |
| 2 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | down: in motion | PASS |
| 3 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 |  |  |  |  |  | 0 |  |  |  |  |  | down limit reached -> completed action stops | PASS |
| 4 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | next action ActivateGrip is running (same or next cycle) | PASS |
| 5 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | grip begins automatically | PASS |
| 6 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | grip: in motion | PASS |
| 7 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |  |  |  |  | 0 |  |  |  |  |  | 0 |  | grip limit reached -> completed action stops | PASS |
| 8 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | next action MoveUp is running (same or next cycle) | PASS |
| 9 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | up begins automatically | PASS |
| 10 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | up: in motion | PASS |
| 11 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |  | 0 |  |  |  |  |  | 0 |  |  |  |  | up limit reached -> completed action stops | PASS |
| 12 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | next action MoveRight is running (same or next cycle) | PASS |
| 13 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | right begins automatically | PASS |
| 14 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | right: in motion | PASS |
| 15 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 |  |  |  | 0 |  |  |  |  |  | 0 |  |  | right limit reached -> completed action stops | PASS |
| 16 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | next action MoveDown is running (same or next cycle) | PASS |
| 17 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | down begins automatically | PASS |
| 18 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | down: in motion | PASS |
| 19 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |  |  |  |  |  | 0 |  |  |  |  |  | down limit reached -> completed action stops | PASS |
| 20 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | next action ActivateRelease is running (same or next cycle) | PASS |
| 21 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | release begins automatically | PASS |
| 22 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | release: in motion | PASS |
| 23 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 |  |  |  |  |  | 0 |  |  |  |  |  | 0 | release limit reached -> completed action stops | PASS |
| 24 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | next action MoveUp is running (same or next cycle) | PASS |
| 25 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | up begins automatically | PASS |
| 26 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | up: in motion | PASS |
| 27 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 |  | 0 |  |  |  |  |  | 0 |  |  |  |  | up limit reached -> completed action stops | PASS |
| 28 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | next action MoveLeft is running (same or next cycle) | PASS |
| 29 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | left begins automatically | PASS |
| 30 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | left: in motion | PASS |
| 31 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | left limit reached -> cycle end | PASS |
| 32 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | back at home: stays stopped (single cycle) | PASS |
| 33 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | still stopped without Start | PASS |
| 34 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | new Start -> next cycle begins | PASS |

### TC04 Continuous mode: cycles repeat without Start

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Continuous mode: cycles repeat without Start |
| 所属题目 | H05 Mechanical Arm Control（`H05_MechArm`） |
| 初始状态 | power-up, ContinuousMode=1, arm at home |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | after the last action the next cycle starts automatically |
| 实际输出及结果 | ✅ 通过 |

| 周期 | ManualMode | SingleStepMode | SingleCycleMode | ContinuousMode | EmergencyStop | Start | DownButton | UpButton | LeftButton | RightButton | GripButton | ReleaseButton | DownLimitSwitch | UpLimitSwitch | LeftLimitSwitch | RightLimitSwitch | GripLimitSwitch | ReleaseLimitSwitch | 预期 MoveDown | 预期 MoveUp | 预期 MoveLeft | 预期 MoveRight | 预期 ActivateGrip | 预期 ActivateRelease | 实际 MoveDown | 实际 MoveUp | 实际 MoveLeft | 实际 MoveRight | 实际 ActivateGrip | 实际 ActivateRelease | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Start -> down begins | PASS |
| 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | down: moving, Start released | PASS |
| 2 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | down: in motion | PASS |
| 3 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 |  |  |  |  |  | 0 |  |  |  |  |  | down limit reached -> completed action stops | PASS |
| 4 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | next action ActivateGrip is running (same or next cycle) | PASS |
| 5 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | grip begins automatically | PASS |
| 6 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | grip: in motion | PASS |
| 7 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |  |  |  |  | 0 |  |  |  |  |  | 0 |  | grip limit reached -> completed action stops | PASS |
| 8 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | next action MoveUp is running (same or next cycle) | PASS |
| 9 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | up begins automatically | PASS |
| 10 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | up: in motion | PASS |
| 11 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |  | 0 |  |  |  |  |  | 0 |  |  |  |  | up limit reached -> completed action stops | PASS |
| 12 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | next action MoveRight is running (same or next cycle) | PASS |
| 13 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | right begins automatically | PASS |
| 14 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | right: in motion | PASS |
| 15 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 |  |  |  | 0 |  |  |  |  |  | 0 |  |  | right limit reached -> completed action stops | PASS |
| 16 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | next action MoveDown is running (same or next cycle) | PASS |
| 17 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | down begins automatically | PASS |
| 18 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | down: in motion | PASS |
| 19 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |  |  |  |  |  | 0 |  |  |  |  |  | down limit reached -> completed action stops | PASS |
| 20 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | next action ActivateRelease is running (same or next cycle) | PASS |
| 21 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | release begins automatically | PASS |
| 22 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | release: in motion | PASS |
| 23 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 |  |  |  |  |  | 0 |  |  |  |  |  | 0 | release limit reached -> completed action stops | PASS |
| 24 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | next action MoveUp is running (same or next cycle) | PASS |
| 25 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | up begins automatically | PASS |
| 26 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | up: in motion | PASS |
| 27 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 |  | 0 |  |  |  |  |  | 0 |  |  |  |  | up limit reached -> completed action stops | PASS |
| 28 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | next action MoveLeft is running (same or next cycle) | PASS |
| 29 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | left begins automatically | PASS |
| 30 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | left: in motion | PASS |
| 31 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |  |  | 0 |  |  |  |  |  | 0 |  |  |  | left limit reached -> completed action stops | PASS |
| 32 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | next action MoveDown is running (same or next cycle) | PASS |
| 33 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | second cycle running without Start | PASS |

### TC05 Emergency stop in automatic and manual modes

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC05 Emergency stop in automatic and manual modes |
| 所属题目 | H05 Mechanical Arm Control（`H05_MechArm`） |
| 初始状态 | power-up, SingleCycleMode=1, arm at home |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | all outputs OFF immediately, stay OFF while estop active, no automatic resume, manual buttons blocked |
| 实际输出及结果 | ✅ 通过 |

| 周期 | ManualMode | SingleStepMode | SingleCycleMode | ContinuousMode | EmergencyStop | Start | DownButton | UpButton | LeftButton | RightButton | GripButton | ReleaseButton | DownLimitSwitch | UpLimitSwitch | LeftLimitSwitch | RightLimitSwitch | GripLimitSwitch | ReleaseLimitSwitch | 预期 MoveDown | 预期 MoveUp | 预期 MoveLeft | 预期 MoveRight | 预期 ActivateGrip | 预期 ActivateRelease | 实际 MoveDown | 实际 MoveUp | 实际 MoveLeft | 实际 MoveRight | 实际 ActivateGrip | 实际 ActivateRelease | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | start cycle | PASS |
| 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | moving down | PASS |
| 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ESTOP -> all outputs OFF | PASS |
| 3 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Start during estop ignored | PASS |
| 4 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | estop released -> no automatic resume | PASS |
| 5 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | manual button during estop -> no motion | PASS |
| 6 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | estop released: manual works again | PASS |

### TC06 Automatic modes wait for Start; manual buttons ignored

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC06 Automatic modes wait for Start; manual buttons ignored |
| 所属题目 | H05 Mechanical Arm Control（`H05_MechArm`） |
| 初始状态 | power-up, arm at home |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | no motion without Start in single-step/single-cycle/continuous; manual buttons ignored in auto modes |
| 实际输出及结果 | ✅ 通过 |

| 周期 | ManualMode | SingleStepMode | SingleCycleMode | ContinuousMode | EmergencyStop | Start | DownButton | UpButton | LeftButton | RightButton | GripButton | ReleaseButton | DownLimitSwitch | UpLimitSwitch | LeftLimitSwitch | RightLimitSwitch | GripLimitSwitch | ReleaseLimitSwitch | 预期 MoveDown | 预期 MoveUp | 预期 MoveLeft | 预期 MoveRight | 预期 ActivateGrip | 预期 ActivateRelease | 实际 MoveDown | 实际 MoveUp | 实际 MoveLeft | 实际 MoveRight | 实际 ActivateGrip | 实际 ActivateRelease | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | single-step idle | PASS |
| 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | single-cycle idle, manual button ignored | PASS |
| 2 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | continuous idle, manual button ignored | PASS |
| 3 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Start -> continuous cycle begins | PASS |

### TC07 Single-step mode: one Start press performs exactly one action

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC07 Single-step mode: one Start press performs exactly one action |
| 所属题目 | H05 Mechanical Arm Control（`H05_MechArm`） |
| 初始状态 | single-step mode, e-stop released, arm idle at step 0 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | single-step mode is edge-triggered on Start; after an action completes the arm must wait for a new Start edge. This case fails on Part 2's reference implementation (DEFECT-H05-01) |
| 实际输出及结果 | ✅ 通过 |

| 周期 | ManualMode | SingleStepMode | SingleCycleMode | ContinuousMode | EmergencyStop | Start | DownButton | UpButton | LeftButton | RightButton | GripButton | ReleaseButton | DownLimitSwitch | UpLimitSwitch | LeftLimitSwitch | RightLimitSwitch | GripLimitSwitch | ReleaseLimitSwitch | 预期 MoveDown | 预期 ActivateGrip | 预期 MoveUp | 实际 MoveDown | 实际 ActivateGrip | 实际 MoveUp | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  | 1 |  |  | Start edge -> action 1: move down | PASS |
| 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  | 1 |  |  | Start released, action 1 continues | PASS |
| 2 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | 0 |  |  | down limit reached: action 1 finished | PASS |
| 3 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  | 0 |  |  | 0 |  | DECISIVE: no new Start edge, so the arm must wait. Action 2 (grip) must not begin | PASS |
| 4 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  | 0 |  |  | 0 |  | still waiting: one Start press, one action | PASS |
| 5 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  | 0 |  |  | 0 |  | still waiting, no unattended progression | PASS |
| 6 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  | 1 |  |  | 1 |  | a fresh Start edge now performs action 2: grip | PASS |
| 7 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  | 1 |  |  | 1 |  | grip continues while Start is held | PASS |
| 8 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 |  | 0 | 0 |  | 0 | 0 | grip limit reached: action 2 finished, and no new Start edge, so action 3 must not begin | PASS |


## H06 Production Control（`H06_Production`）

- 编译：通过；用例通过 6/6；整题通过

### TC01 Manual jog with interlock

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Manual jog with interlock |
| 所属题目 | H06 Production Control（`H06_Production`） |
| 初始状态 | power-up, Mode=0 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | forward, reverse, both -> OFF, release -> stop, kick/light OFF in manual |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Mode | ForwardButton | ReverseButton | SensorFeed | SensorWash | SensorWeight | SensorFiring | SensorOutput | washComplete | weightComplete | weight | firingComplete | 预期 MotorForward | 预期 MotorReverse | 预期 kick | 预期 CompletionLight | 实际 MotorForward | 实际 MotorReverse | 实际 kick | 实际 CompletionLight | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | all OFF | PASS |
| 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | forward | PASS |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | release -> stop | PASS |
| 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | reverse | PASS |
| 4 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | interlock: both OFF | PASS |
| 5 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | auto signals ignored in manual, no kick | PASS |

### TC02 Automatic cycle with qualified material (weight 150)

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Automatic cycle with qualified material (weight 150) |
| 所属题目 | H06 Production Control（`H06_Production`） |
| 初始状态 | power-up, Mode=1, no material |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | all five stations, motor stops at each sensor, firingTemp = 525 for weight 150, light ON/OFF |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Mode | ForwardButton | ReverseButton | SensorFeed | SensorWash | SensorWeight | SensorFiring | SensorOutput | washComplete | weightComplete | weight | firingComplete | 预期 MotorForward | 预期 MotorReverse | 预期 kick | 预期 CompletionLight | 预期 firingTemp | 实际 MotorForward | 实际 MotorReverse | 实际 kick | 实际 CompletionLight | 实际 firingTemp | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | auto idle | PASS |
| 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  | material at feed -> forward (trigger cycle) | PASS |
| 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |  | 1 | 0 | 0 | 0 |  | motor starts in the following cycle | PASS |
| 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |  | 1 | 0 | 0 | 0 |  | moving to wash | PASS |
| 4 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | at wash -> stop | PASS |
| 5 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | waiting washComplete | PASS |
| 6 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |  | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  | washComplete -> forward (trigger cycle) | PASS |
| 7 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |  | 1 | 0 | 0 | 0 |  | motor starts in the following cycle | PASS |
| 8 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |  | 1 | 0 | 0 | 0 |  | moving to weight | PASS |
| 9 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | at weight -> stop | PASS |
| 10 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 150 | 0 |  | 0 | 0 | 0 | 525.0 |  | 0 | 0 | 0 | 525.0 | qualified: firingTemp=525, forward, no kick (trigger cycle) | PASS |
| 11 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 150 | 0 | 1 | 0 | 0 | 0 | 525.0 | 1 | 0 | 0 | 0 | 525.0 | motor starts in the following cycle | PASS |
| 12 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 150 | 0 | 1 | 0 | 0 | 0 | 525.0 | 1 | 0 | 0 | 0 | 525.0 | moving to firing, temp held | PASS |
| 13 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 150 | 0 | 0 | 0 | 0 | 0 | 525.0 | 0 | 0 | 0 | 0 | 525.0 | at firing -> stop | PASS |
| 14 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 150 | 1 |  | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  | firingComplete -> forward (trigger cycle) | PASS |
| 15 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 150 | 0 | 1 | 0 | 0 | 0 |  | 1 | 0 | 0 | 0 |  | motor starts in the following cycle | PASS |
| 16 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 150 | 0 | 1 | 0 | 0 | 0 |  | 1 | 0 | 0 | 0 |  | moving to output | PASS |
| 17 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 150 | 0 | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  |  | at output -> stop, light ON (arrival cycle) | PASS |
| 18 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 150 | 0 | 0 | 0 | 0 | 1 |  | 0 | 0 | 0 | 1 |  | completion light on in the following cycle | PASS |
| 19 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 150 | 0 | 0 | 0 | 0 | 1 |  | 0 | 0 | 0 | 1 |  | light stays ON while product present | PASS |
| 20 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 150 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | product removed -> light OFF | PASS |
| 21 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  | next material starts a new cycle (trigger cycle) | PASS |
| 22 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |  | 1 | 0 | 0 | 0 |  | motor starts in the following cycle | PASS |

### TC03 Weight boundaries and temperature mapping

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Weight boundaries and temperature mapping |
| 所属题目 | H06 Production Control（`H06_Production`） |
| 初始状态 | power-up, Mode=1 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | weight 100 -> 500, weight 200 -> 550, weight 120 -> 510 (linear), all qualified |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Mode | ForwardButton | ReverseButton | SensorFeed | SensorWash | SensorWeight | SensorFiring | SensorOutput | washComplete | weightComplete | weight | firingComplete | 预期 MotorReverse | 预期 kick | 预期 CompletionLight | 预期 MotorForward | 预期 firingTemp | 实际 MotorReverse | 实际 kick | 实际 CompletionLight | 实际 MotorForward | 实际 firingTemp | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  |  | start (trigger cycle) | PASS |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 0 | 0 | 0 | 1 |  | motor starts in the following cycle | PASS |
| 2 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | at wash | PASS |
| 3 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  |  | washed (trigger cycle) | PASS |
| 4 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 0 | 0 | 0 | 1 |  | motor starts in the following cycle | PASS |
| 5 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | at weight | PASS |
| 6 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 100 | 0 | 0 | 0 | 0 |  | 500.0 | 0 | 0 | 0 |  | 500.0 | weight=100 (lower boundary) qualified, temp 500 (trigger cycle) | PASS |
| 7 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 100 | 0 | 0 | 0 | 0 | 1 | 500.0 | 0 | 0 | 0 | 1 | 500.0 | motor starts in the following cycle | PASS |
| 8 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 100 | 0 | 0 | 0 | 0 | 0 | 500.0 | 0 | 0 | 0 | 0 | 500.0 | at firing | PASS |
| 9 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 100 | 1 | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  |  | fired (trigger cycle) | PASS |
| 10 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 100 | 0 | 0 | 0 | 0 | 1 |  | 0 | 0 | 0 | 1 |  | motor starts in the following cycle | PASS |
| 11 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 100 | 0 | 0 | 0 |  | 0 |  | 0 | 0 |  | 0 |  | at output (arrival cycle) | PASS |
| 12 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 100 | 0 | 0 | 0 | 1 | 0 |  | 0 | 0 | 1 | 0 |  | completion light on in the following cycle | PASS |
| 13 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 100 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | removed | PASS |
| 14 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  |  | second material (trigger cycle) | PASS |
| 15 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 0 | 0 | 0 | 1 |  | motor starts in the following cycle | PASS |
| 16 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | at wash | PASS |
| 17 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  |  | washed (trigger cycle) | PASS |
| 18 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 0 | 0 | 0 | 1 |  | motor starts in the following cycle | PASS |
| 19 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | at weight | PASS |
| 20 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 200 | 0 | 0 | 0 | 0 |  | 550.0 | 0 | 0 | 0 |  | 550.0 | weight=200 (upper boundary) qualified, temp 550 (trigger cycle) | PASS |
| 21 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 200 | 0 | 0 | 0 | 0 | 1 | 550.0 | 0 | 0 | 0 | 1 | 550.0 | motor starts in the following cycle | PASS |
| 22 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 200 | 0 | 0 | 0 | 0 | 0 | 550.0 | 0 | 0 | 0 | 0 | 550.0 | at firing | PASS |
| 23 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 200 | 1 | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  |  | fired (trigger cycle) | PASS |
| 24 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 200 | 0 | 0 | 0 | 0 | 1 |  | 0 | 0 | 0 | 1 |  | motor starts in the following cycle | PASS |
| 25 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 200 | 0 | 0 | 0 |  | 0 |  | 0 | 0 |  | 0 |  | at output (arrival cycle) | PASS |
| 26 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 200 | 0 | 0 | 0 | 1 | 0 |  | 0 | 0 | 1 | 0 |  | completion light on in the following cycle | PASS |
| 27 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 200 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | removed | PASS |
| 28 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  |  | third material (trigger cycle) | PASS |
| 29 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 0 | 0 | 0 | 1 |  | motor starts in the following cycle | PASS |
| 30 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | at wash | PASS |
| 31 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  |  | washed (trigger cycle) | PASS |
| 32 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 0 | 0 | 0 | 1 |  | motor starts in the following cycle | PASS |
| 33 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | at weight | PASS |
| 34 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 120 | 0 | 0 | 0 | 0 |  | 510.0 | 0 | 0 | 0 |  | 510.0 | weight=120 -> temp 510 (linear) (trigger cycle) | PASS |
| 35 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 120 | 0 | 0 | 0 | 0 | 1 | 510.0 | 0 | 0 | 0 | 1 | 510.0 | motor starts in the following cycle | PASS |

### TC04 Unqualified material is rejected

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Unqualified material is rejected |
| 所属题目 | H06 Production Control（`H06_Production`） |
| 初始状态 | power-up, Mode=1 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | weight 99.9 -> kick, no forward; weight 200.1 -> kick; line ready again after rejection |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Mode | ForwardButton | ReverseButton | SensorFeed | SensorWash | SensorWeight | SensorFiring | SensorOutput | washComplete | weightComplete | weight | firingComplete | 预期 MotorReverse | 预期 kick | 预期 CompletionLight | 预期 MotorForward | 实际 MotorReverse | 实际 kick | 实际 CompletionLight | 实际 MotorForward | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 |  | start (trigger cycle) | PASS |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | motor starts in the following cycle | PASS |
| 2 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | at wash | PASS |
| 3 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 |  | washed (trigger cycle) | PASS |
| 4 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | motor starts in the following cycle | PASS |
| 5 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | at weight | PASS |
| 6 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 99.9 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | weight 99.9 -> kick, motor stays stopped | PASS |
| 7 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 99.9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | rejected material removed -> kick released, motor stopped | PASS |
| 8 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 |  | line accepts the next material (trigger cycle) | PASS |
| 9 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | motor starts in the following cycle | PASS |
| 10 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | at wash | PASS |
| 11 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 |  | washed (trigger cycle) | PASS |
| 12 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | motor starts in the following cycle | PASS |
| 13 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | at weight | PASS |
| 14 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 200.1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | weight 200.1 -> kick | PASS |

### TC05 Signals at the wrong station are ignored

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC05 Signals at the wrong station are ignored |
| 所属题目 | H06 Production Control（`H06_Production`） |
| 初始状态 | power-up, Mode=1 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | washComplete/weightComplete/firingComplete before arrival do nothing; manual buttons ignored in auto |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Mode | ForwardButton | ReverseButton | SensorFeed | SensorWash | SensorWeight | SensorFiring | SensorOutput | washComplete | weightComplete | weight | firingComplete | 预期 MotorForward | 预期 MotorReverse | 预期 kick | 预期 CompletionLight | 实际 MotorForward | 实际 MotorReverse | 实际 kick | 实际 CompletionLight | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 150 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | complete signals without material -> nothing, no kick | PASS |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | manual buttons ignored | PASS |
| 2 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 |  | 0 | 0 | 0 | start (trigger cycle) | PASS |
| 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | motor starts in the following cycle | PASS |
| 4 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 150 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | at wash: other complete signals ignored, motor stopped | PASS |
| 5 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |  | 0 | 0 | 0 |  | 0 | 0 | 0 | correct signal continues (trigger cycle) | PASS |
| 6 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | motor starts in the following cycle | PASS |
| 7 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 50 | 0 | 0 |  |  |  | 0 |  |  |  | release the confirm button (edge-triggered) | PASS |
| 8 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 50 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | at weight: no kick until weightComplete | PASS |

### TC06 Mode switch during automatic motion

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC06 Mode switch during automatic motion |
| 所属题目 | H06 Production Control（`H06_Production`） |
| 初始状态 | power-up, Mode=1 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | switch to manual stops motor; back to auto restarts idle |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Mode | ForwardButton | ReverseButton | SensorFeed | SensorWash | SensorWeight | SensorFiring | SensorOutput | washComplete | weightComplete | weight | firingComplete | 预期 MotorReverse | 预期 kick | 预期 CompletionLight | 预期 MotorForward | 实际 MotorReverse | 实际 kick | 实际 CompletionLight | 实际 MotorForward | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 |  | start (trigger cycle) | PASS |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | motor starts in the following cycle | PASS |
| 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | moving | PASS |
| 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Mode=0 -> motor stops | PASS |
| 4 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | manual jog | PASS |
| 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | back to auto, idle | PASS |


## C01 Product Reject and Filtering Station（`FB_C01`）

- 编译：通过；用例通过 2/2；整题通过

### TC01 accept and reject a part

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 accept and reject a part |
| 所属题目 | C01 Product Reject and Filtering Station（`FB_C01`） |
| 初始状态 | counters zero, batch not full |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | normal accept, defective reject, pusher time-out |
| 实际输出及结果 | ✅ 通过 |

| 周期 | RunSwitch | PartPresent | DefectSensor | ResetButton | 预期 ConveyorMotor | 预期 AcceptCount | 预期 RejectCount | 预期 BatchFull | 预期 RejectPusher | 实际 ConveyorMotor | 实际 AcceptCount | 实际 RejectCount | 实际 BatchFull | 实际 RejectPusher | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | reset | PASS |
| 1 |  | 1 | 0 | 0 | 1 | 1 | 0 |  | 0 | 1 | 1 | 0 |  | 0 | good part accepted | PASS |
| 2 |  | 0 |  |  |  | 1 | 0 |  | 0 |  | 1 | 0 |  | 0 | part leaves | PASS |
| 3 |  | 1 | 1 |  | 1 | 1 | 1 |  | 1 | 1 | 1 | 1 |  | 1 | defective part rejected | PASS |
| 4（保持 1100 ms） |  | 0 |  |  |  |  | 1 |  | 0 |  |  | 1 |  | 0 | pusher retracted after 1 s | PASS |

### TC02 batch of five stops the conveyor

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 batch of five stops the conveyor |
| 所属题目 | C01 Product Reject and Filtering Station（`FB_C01`） |
| 初始状态 | counters zero, batch not full |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | five accepted parts, batch full, reset |
| 实际输出及结果 | ✅ 通过 |

| 周期 | RunSwitch | ResetButton | PartPresent | 预期 AcceptCount | 预期 BatchFull | 预期 ConveyorMotor | 预期 RejectCount | 实际 AcceptCount | 实际 BatchFull | 实际 ConveyorMotor | 实际 RejectCount | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 0 | 0 | 1 |  | 0 | 0 | 1 |  | reset | PASS |
| 1 |  | 0 | 1 | 1 |  | 1 |  | 1 |  | 1 |  | part 1 | PASS |
| 2 |  |  | 0 | 1 |  |  |  | 1 |  |  |  | gap | PASS |
| 3 |  |  | 1 | 2 |  |  |  | 2 |  |  |  | part 2 | PASS |
| 4 |  |  | 0 | 2 |  |  |  | 2 |  |  |  | gap | PASS |
| 5 |  |  | 1 | 3 |  |  |  | 3 |  |  |  | part 3 | PASS |
| 6 |  |  | 0 | 3 |  |  |  | 3 |  |  |  | gap | PASS |
| 7 |  |  | 1 | 4 |  |  |  | 4 |  |  |  | part 4 | PASS |
| 8 |  |  | 0 | 4 |  |  |  | 4 |  |  |  | gap | PASS |
| 9 |  |  | 1 | 5 | 1 | 0 |  | 5 | 1 | 0 |  | fifth part fills batch | PASS |
| 10 |  | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | reset starts a new batch | PASS |


## C02 Two-Hand Safety Press（`FB_C02`）

- 编译：通过；用例通过 2/2；整题通过

### TC01 two-hand press and release

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 two-hand press and release |
| 所属题目 | C02 Two-Hand Safety Press（`FB_C02`） |
| 初始状态 | no buttons, no part, no fault |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | normal two-hand start, cycle-complete pulse, reset state |
| 实际输出及结果 | ✅ 通过 |

| 周期 | LeftButton | RightButton | PartPresent | ResetButton | 预期 PressOutput | 预期 CycleComplete | 预期 Fault | 实际 PressOutput | 实际 CycleComplete | 实际 Fault | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | reset | PASS |
| 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | both buttons close the press | PASS |
| 2 | 0 | 1 | 1 |  | 0 | 1 |  | 0 | 1 |  | release one button, cycle complete | PASS |
| 3 | 0 | 0 | 0 |  | 0 | 0 |  | 0 | 0 |  | cycle pulse ends | PASS |

### TC02 anti-tiedown fault

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 anti-tiedown fault |
| 所属题目 | C02 Two-Hand Safety Press（`FB_C02`） |
| 初始状态 | no fault |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | single button held 500 ms, fault latch, reset, restart |
| 实际输出及结果 | ✅ 通过 |

| 周期 | LeftButton | RightButton | PartPresent | ResetButton | 预期 Fault | 预期 PressOutput | 实际 Fault | 实际 PressOutput | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | reset | PASS |
| 1（保持 600 ms） | 1 | 0 |  | 0 | 1 | 0 | 1 | 0 | one button held alone | PASS |
| 2 | 1 | 1 | 1 |  | 1 | 0 | 1 | 0 | fault blocks the press | PASS |
| 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | reset while released | PASS |
| 4 |  |  |  | 0 | 0 | 0 | 0 | 0 | buttons released | PASS |
| 5 | 1 | 1 | 1 |  | 0 | 1 | 0 | 1 | press can restart | PASS |


## C03 Automatic Barrier Gate（`FB_C03`）

- 编译：通过；用例通过 2/2；整题通过

### TC01 open button and automatic close

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 open button and automatic close |
| 所属题目 | C03 Automatic Barrier Gate（`FB_C03`） |
| 初始状态 | gate closed, no vehicle, no beam |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | manual open, 3 s close delay, closed state |
| 实际输出及结果 | ✅ 通过 |

| 周期 | VehiclePresent | OpenButton | SafetyBeam | 预期 GateOpen | 预期 GateClosed | 预期 WarningLight | 实际 GateOpen | 实际 GateClosed | 实际 WarningLight | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | initial closed | PASS |
| 1 |  | 1 |  | 1 | 0 | 0 | 1 | 0 | 0 | manual open | PASS |
| 2 |  | 0 |  | 1 | 0 |  | 1 | 0 |  | no vehicle, close delay running | PASS |
| 3（保持 3100 ms） |  |  |  | 0 | 1 |  | 0 | 1 |  | closed after 3 s | PASS |

### TC02 vehicle and safety beam

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 vehicle and safety beam |
| 所属题目 | C03 Automatic Barrier Gate（`FB_C03`） |
| 初始状态 | gate closed |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | hold open by vehicle, beam warning, reopen while closed |
| 实际输出及结果 | ✅ 通过 |

| 周期 | VehiclePresent | SafetyBeam | 预期 GateOpen | 预期 GateClosed | 预期 WarningLight | 实际 GateOpen | 实际 GateClosed | 实际 WarningLight | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 |  | 1 | 0 |  | 1 | 0 |  | vehicle opens gate | PASS |
| 1 | 0 |  | 1 | 0 |  | 1 | 0 |  | vehicle leaves, close delay | PASS |
| 2 |  | 1 | 1 |  | 1 | 1 |  | 1 | beam keeps gate open | PASS |
| 3（保持 3100 ms） |  | 0 | 0 | 1 | 0 | 0 | 1 | 0 | beam clear, close after 3 s | PASS |
| 4 |  | 1 | 1 | 0 | 1 | 1 | 0 | 1 | beam reopens closed gate | PASS |


## C04 Star-Delta Motor Starter（`FB_C04`）

- 编译：通过；用例通过 2/2；整题通过

### TC01 start, transition and stop

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 start, transition and stop |
| 所属题目 | C04 Star-Delta Motor Starter（`FB_C04`） |
| 初始状态 | motor stopped |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | star start, 3 s transition, delta run, stop |
| 实际输出及结果 | ✅ 通过 |

| 周期 | StartButton | StopButton | Overload | ResetButton | 预期 MainContactor | 预期 StarContactor | 预期 DeltaContactor | 预期 Running | 实际 MainContactor | 实际 StarContactor | 实际 DeltaContactor | 实际 Running | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | stopped | PASS |
| 1 | 1 |  |  |  | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | star start | PASS |
| 2（保持 3100 ms） | 0 |  |  |  | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | delta after 3 s | PASS |
| 3 |  | 1 |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | stop | PASS |

### TC02 overload latch and reset

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 overload latch and reset |
| 所属题目 | C04 Star-Delta Motor Starter（`FB_C04`） |
| 初始状态 | motor stopped |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | overload during delta, fault latch, reset, restart |
| 实际输出及结果 | ✅ 通过 |

| 周期 | StartButton | ResetButton | Overload | 预期 MainContactor | 预期 StarContactor | 预期 DeltaContactor | 预期 Fault | 预期 Running | 实际 MainContactor | 实际 StarContactor | 实际 DeltaContactor | 实际 Fault | 实际 Running | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 |  |  | 1 | 1 |  |  |  | 1 | 1 |  |  |  | start | PASS |
| 1（保持 3100 ms） | 0 |  |  | 1 |  | 1 |  |  | 1 |  | 1 |  |  | delta | PASS |
| 2 |  |  | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | overload trip | PASS |
| 3 |  | 1 | 0 |  |  |  | 0 |  |  |  |  | 0 |  | reset | PASS |
| 4 | 1 | 0 |  | 1 | 1 |  |  |  | 1 | 1 |  |  |  | restart | PASS |


## C05 Car Wash Sequence（`FB_C05`）

- 编译：通过；用例通过 2/2；整题通过

### TC01 full wash sequence

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 full wash sequence |
| 所属题目 | C05 Car Wash Sequence（`FB_C05`） |
| 初始状态 | idle, vehicle present |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | foam, brush, rinse, dry, cycle complete |
| 实际输出及结果 | ✅ 通过 |

| 周期 | StartButton | EmergencyStop | VehiclePresent | ResetButton | 预期 ConveyorMotor | 预期 CycleComplete | 预期 Fault | 预期 FoamValve | 预期 BrushMotor | 预期 RinseValve | 预期 DryFan | 实际 ConveyorMotor | 实际 CycleComplete | 实际 Fault | 实际 FoamValve | 实际 BrushMotor | 实际 RinseValve | 实际 DryFan | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |  |  |  |  | 0 | 0 | 0 |  |  |  |  | reset | PASS |
| 1 | 1 |  | 1 | 0 | 1 | 0 |  | 1 | 0 |  |  | 1 | 0 |  | 1 | 0 |  |  | foam step | PASS |
| 2（保持 2100 ms） | 0 |  |  |  | 1 |  |  | 0 | 1 |  |  | 1 |  |  | 0 | 1 |  |  | brush step | PASS |
| 3（保持 2100 ms） |  |  |  |  | 1 |  |  |  | 0 | 1 |  | 1 |  |  |  | 0 | 1 |  | rinse step | PASS |
| 4（保持 1100 ms） |  |  |  |  | 1 |  |  |  |  | 0 | 1 | 1 |  |  |  |  | 0 | 1 | dry step | PASS |
| 5（保持 1100 ms） |  |  |  |  | 0 | 1 |  |  |  |  | 0 | 0 | 1 |  |  |  |  | 0 | cycle complete | PASS |

### TC02 emergency stop and reset

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 emergency stop and reset |
| 所属题目 | C05 Car Wash Sequence（`FB_C05`） |
| 初始状态 | idle |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | emergency during foam, fault latch, reset, restart |
| 实际输出及结果 | ✅ 通过 |

| 周期 | StartButton | VehiclePresent | ResetButton | EmergencyStop | 预期 ConveyorMotor | 预期 FoamValve | 预期 Fault | 实际 ConveyorMotor | 实际 FoamValve | 实际 Fault | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 |  |  | 1 | 1 | 0 | 1 | 1 | 0 | cycle starts | PASS |
| 1 | 0 |  |  | 1 | 0 | 0 | 1 | 0 | 0 | 1 | emergency stop | PASS |
| 2 |  |  |  | 0 | 0 |  | 1 | 0 |  | 1 | fault remains latched | PASS |
| 3 |  |  | 1 |  | 0 |  | 0 | 0 |  | 0 | reset | PASS |
| 4 | 1 |  | 0 |  | 1 | 1 |  | 1 | 1 |  | restart | PASS |


## C06 Elevator Door Control（`FB_C06`）

- 编译：通过；用例通过 3/3；整题通过

### TC01 open, close by button, limit stop

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 open, close by button, limit stop |
| 所属题目 | C06 Elevator Door Control（`FB_C06`） |
| 初始状态 | door closed |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | open command, open limit, close command, closed limit |
| 实际输出及结果 | ✅ 通过 |

| 周期 | OpenButton | CloseButton | ObstacleSensor | DoorOpenLimit | DoorClosedLimit | ResetButton | 预期 DoorMotorOpen | 预期 DoorMotorClose | 预期 DoorClosed | 预期 DoorOpen | 实际 DoorMotorOpen | 实际 DoorMotorClose | 实际 DoorClosed | 实际 DoorOpen | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | closed | PASS |
| 1 | 1 |  |  |  | 0 |  | 1 | 0 |  |  | 1 | 0 |  |  | opening | PASS |
| 2 | 0 |  |  | 1 |  |  | 0 |  | 0 | 1 | 0 |  | 0 | 1 | open limit | PASS |
| 3 |  | 1 |  | 1 |  |  | 0 | 1 |  |  | 0 | 1 |  |  | closing | PASS |
| 4 |  | 0 |  | 0 | 1 |  |  | 0 | 1 |  |  | 0 | 1 |  | closed limit | PASS |

### TC02 obstacle reversal and buzzer

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 obstacle reversal and buzzer |
| 所属题目 | C06 Elevator Door Control（`FB_C06`） |
| 初始状态 | door open |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | closing, obstacle, reopen, buzzer |
| 实际输出及结果 | ✅ 通过 |

| 周期 | DoorOpenLimit | DoorClosedLimit | ObstacleSensor | CloseButton | 预期 DoorOpen | 预期 DoorMotorClose | 预期 DoorMotorOpen | 预期 WarningBuzzer | 实际 DoorOpen | 实际 DoorMotorClose | 实际 DoorMotorOpen | 实际 WarningBuzzer | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 |  | 1 | 0 |  |  | 1 | 0 |  |  | open | PASS |
| 1 |  |  |  | 1 |  | 1 | 0 |  |  | 1 | 0 |  | closing | PASS |
| 2 | 0 |  | 1 |  |  | 0 | 1 | 1 |  | 0 | 1 | 1 | obstacle reverses | PASS |
| 3 | 1 |  | 0 | 0 | 1 |  | 0 | 0 | 1 |  | 0 | 0 | open limit reached | PASS |

### TC03 automatic close after 5 s

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 automatic close after 5 s |
| 所属题目 | C06 Elevator Door Control（`FB_C06`） |
| 初始状态 | door open, path clear |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | open door, no commands, auto close timer |
| 实际输出及结果 | ✅ 通过 |

| 周期 | DoorOpenLimit | DoorClosedLimit | OpenButton | CloseButton | ObstacleSensor | 预期 DoorMotorClose | 预期 DoorMotorOpen | 实际 DoorMotorClose | 实际 DoorMotorOpen | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0（保持 5100 ms） | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | auto close starts after 5 s | PASS |


## C07 Bottle Height Sorting（`FB_C07`）

- 编译：通过；用例通过 2/2；整题通过

### TC01 accept and reject bottles

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 accept and reject bottles |
| 所属题目 | C07 Bottle Height Sorting（`FB_C07`） |
| 初始状态 | counters zero, conveyor enabled |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | in-range accept, high reject, gate pulse 500 ms |
| 实际输出及结果 | ✅ 通过 |

| 周期 | RunSwitch | PartPresent | HeightSensor | ResetButton | 预期 ConveyorMotor | 预期 AcceptCount | 预期 RejectCount | 预期 Fault | 预期 AcceptGate | 预期 RejectGate | 实际 ConveyorMotor | 实际 AcceptCount | 实际 RejectCount | 实际 Fault | 实际 AcceptGate | 实际 RejectGate | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 50.0 | 1 | 1 | 0 | 0 | 0 |  |  | 1 | 0 | 0 | 0 |  |  | reset | PASS |
| 1 |  | 1 | 50.0 | 0 | 1 | 1 |  |  | 1 | 0 | 1 | 1 |  |  | 1 | 0 | accept 50 mm | PASS |
| 2（保持 600 ms） |  | 0 |  |  |  | 1 |  |  | 0 |  |  | 1 |  |  | 0 |  | accept gate retracts | PASS |
| 3 |  | 1 | 70.0 |  |  |  | 1 |  | 0 | 1 |  |  | 1 |  | 0 | 1 | reject 70 mm | PASS |
| 4（保持 600 ms） |  | 0 |  |  |  |  | 1 |  |  | 0 |  |  | 1 |  |  | 0 | reject gate retracts | PASS |

### TC02 invalid sensor value

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 invalid sensor value |
| 所属题目 | C07 Bottle Height Sorting（`FB_C07`） |
| 初始状态 | counters zero |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | out-of-range sensor latches fault and inhibits gates |
| 实际输出及结果 | ✅ 通过 |

| 周期 | RunSwitch | PartPresent | HeightSensor | ResetButton | 预期 Fault | 预期 ConveyorMotor | 预期 AcceptGate | 预期 RejectGate | 预期 AcceptCount | 预期 RejectCount | 实际 Fault | 实际 ConveyorMotor | 实际 AcceptGate | 实际 RejectGate | 实际 AcceptCount | 实际 RejectCount | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 50.0 | 1 | 0 | 1 |  |  |  |  | 0 | 1 |  |  |  |  | reset | PASS |
| 1 |  | 1 | 150.0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | invalid height | PASS |
| 2 |  |  | 50.0 | 1 | 0 | 1 |  |  | 0 | 0 | 0 | 1 |  |  | 0 | 0 | reset | PASS |


## C08 Greenhouse Irrigation Zones（`FB_C08`）

- 编译：通过；用例通过 2/3；整题未通过

### TC01 dry, wet, dry zones

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 dry, wet, dry zones |
| 所属题目 | C08 Greenhouse Irrigation Zones（`FB_C08`） |
| 初始状态 | idle, zone 1 and 3 dry |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | zone 1 waters, zone 2 skipped, zone 3 waters, complete |
| 实际输出及结果 | ✅ 通过 |

| 周期 | StartButton | StopButton | Zone1Moisture | Zone2Moisture | Zone3Moisture | ResetButton | 预期 Zone1Valve | 预期 Pump | 预期 CycleComplete | 预期 Zone2Valve | 预期 Zone3Valve | 实际 Zone1Valve | 实际 Pump | 实际 CycleComplete | 实际 Zone2Valve | 实际 Zone3Valve | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 20.0 | 50.0 | 20.0 | 1 | 1 | 1 | 0 |  |  | 1 | 1 | 0 |  |  | zone 1 starts | PASS |
| 1（保持 3100 ms） | 0 |  |  |  |  | 0 | 0 | 1 |  | 0 | 1 | 0 | 1 |  | 0 | 1 | zone 2 skipped, zone 3 starts | PASS |
| 2（保持 3100 ms） |  |  |  |  |  |  |  | 0 | 1 |  | 0 |  | 0 | 1 |  | 0 | cycle complete | PASS |
| 3 |  |  |  |  |  | 1 |  | 0 | 0 |  |  |  | 0 | 0 |  |  | reset complete flag | PASS |

### TC02 all zones wet

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 all zones wet |
| 所属题目 | C08 Greenhouse Irrigation Zones（`FB_C08`） |
| 初始状态 | idle |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | all zones skipped, immediate completion |
| 实际输出及结果 | ❌ 不通过；周期 0：CycleComplete 预期 1，实际 False |

| 周期 | StartButton | Zone1Moisture | Zone2Moisture | Zone3Moisture | 预期 Zone1Valve | 预期 Zone2Valve | 预期 Zone3Valve | 预期 Pump | 预期 CycleComplete | 实际 Zone1Valve | 实际 Zone2Valve | 实际 Zone3Valve | 实际 Pump | 实际 CycleComplete | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 50.0 | 50.0 | 50.0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | all wet, complete immediately | FAIL |

### TC03 stop aborts irrigation

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 stop aborts irrigation |
| 所属题目 | C08 Greenhouse Irrigation Zones（`FB_C08`） |
| 初始状态 | idle |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | stop during zone 1, outputs off, complete cleared |
| 实际输出及结果 | ✅ 通过 |

| 周期 | StartButton | Zone1Moisture | StopButton | 预期 Zone1Valve | 预期 Pump | 预期 CycleComplete | 实际 Zone1Valve | 实际 Pump | 实际 CycleComplete | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 20.0 |  | 1 | 1 |  | 1 | 1 |  | zone 1 starts | PASS |
| 1 | 0 |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | stop aborts | PASS |


## C09 Conveyor Zone Accumulation（`FB_C09`）

- 编译：通过；用例通过 3/3；整题通过

### TC01 normal accumulation

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 normal accumulation |
| 所属题目 | C09 Conveyor Zone Accumulation（`FB_C09`） |
| 初始状态 | line enabled, empty |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | zone 1 moves, zone 1 full, zone 2 moves |
| 实际输出及结果 | ✅ 通过 |

| 周期 | RunSwitch | Zone1Sensor | Zone2Sensor | Zone3Sensor | ReleaseButton | ResetButton | 预期 Zone1Motor | 预期 Zone2Motor | 预期 Zone1Full | 预期 JamAlarm | 预期 Zone2Full | 预期 Zone3Motor | 预期 Zone3Full | 实际 Zone1Motor | 实际 Zone2Motor | 实际 Zone1Full | 实际 JamAlarm | 实际 Zone2Full | 实际 Zone3Motor | 实际 Zone3Full | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 |  |  |  | 1 | 0 | 0 | 0 |  |  |  | zone 1 moves | PASS |
| 1 |  |  | 1 |  |  | 0 | 0 | 1 | 1 |  | 0 |  |  | 0 | 1 | 1 |  | 0 |  |  | zone 1 full, zone 2 moves | PASS |
| 2 |  |  |  | 1 |  |  |  | 0 |  |  | 1 | 0 | 1 |  | 0 |  |  | 1 | 0 | 1 | zone 2 full | PASS |

### TC02 jam detection and reset

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 jam detection and reset |
| 所属题目 | C09 Conveyor Zone Accumulation（`FB_C09`） |
| 初始状态 | line enabled |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | blocked zone 1 for 5 s, jam alarm, all motors off, reset |
| 实际输出及结果 | ✅ 通过 |

| 周期 | RunSwitch | Zone1Sensor | Zone2Sensor | Zone3Sensor | ReleaseButton | ResetButton | 预期 Zone1Full | 预期 JamAlarm | 预期 Zone1Motor | 预期 Zone2Motor | 实际 Zone1Full | 实际 JamAlarm | 实际 Zone1Motor | 实际 Zone2Motor | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0（保持 5100 ms） | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | zone 1 blocked, jam after 5 s | PASS |
| 1 |  | 0 | 0 |  |  | 1 |  | 0 | 0 | 0 |  | 0 | 0 | 0 | reset and clear sensors | PASS |
| 2 |  | 1 |  |  |  | 0 |  | 0 | 1 |  |  | 0 | 1 |  | line restarts | PASS |

### TC03 release zone 3

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 release zone 3 |
| 所属题目 | C09 Conveyor Zone Accumulation（`FB_C09`） |
| 初始状态 | line enabled |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | release button runs zone 3, blocked zone 3 jams |
| 实际输出及结果 | ✅ 通过 |

| 周期 | RunSwitch | Zone3Sensor | ReleaseButton | 预期 Zone3Motor | 预期 Zone3Full | 预期 JamAlarm | 实际 Zone3Motor | 实际 Zone3Full | 实际 JamAlarm | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | release runs zone 3 | PASS |
| 1（保持 5100 ms） |  |  | 0 | 0 | 1 | 1 | 0 | 1 | 1 | zone 3 blocked, jam after 5 s | PASS |


# qwen3-coder-flash（model_b）

## E01 Automated Filling Line Control（`E01_Filling`）

- 编译：通过；用例通过 0/6；整题未通过

### TC01 Full production cycle

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Full production cycle |
| 所属题目 | E01 Automated Filling Line Control（`E01_Filling`） |
| 初始状态 | power-up, all inputs FALSE, all outputs FALSE |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | power-up idle, every step transition, exactly one actuator active per step, outputs stay latched after the trigger is released, light reset by finishedButton |
| 实际输出及结果 | ❌ 不通过；周期 0：Pump_Motor 预期 0，实际 True；周期 3：Pump_Motor 预期 0，实际 True；Filling_Valve 预期 1，实际 False；周期 4：Pump_Motor 预期 0，实际 True；Filling_Valve 预期 1，实际 False |

| 周期 | bottleSensor | cleaningConfirmButton | fillingConfirmButton | cappingConfirmButton | packingConfirmButton | finishedButton | 预期 Pump_Motor | 预期 Filling_Valve | 预期 Capping_Machine | 预期 Packing_Machine | 预期 Completion_Light | 实际 Pump_Motor | 实际 Filling_Valve | 实际 Capping_Machine | 实际 Packing_Machine | 实际 Completion_Light | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | idle: all outputs OFF | FAIL |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | bottle detected -> pump ON | PASS |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | sensor released, pump keeps running | PASS |
| 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | cleaning confirmed -> pump OFF, valve ON | FAIL |
| 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | button released, valve stays ON | FAIL |
| 5 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | filling confirmed -> valve OFF, capping ON | FAIL |
| 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | capping stays ON | FAIL |
| 7 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | capping confirmed -> capping OFF, packing ON | FAIL |
| 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | packing stays ON | FAIL |
| 9 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | packing confirmed -> packing OFF, light ON | FAIL |
| 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | light stays ON while waiting for pickup | FAIL |
| 11 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | finishedButton -> light OFF, back to idle | FAIL |
| 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | idle again, all OFF | FAIL |

### TC02 Second cycle after reset

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Second cycle after reset |
| 所属题目 | E01 Automated Filling Line Control（`E01_Filling`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | the line is ready for the next bottle after finishedButton |
| 实际输出及结果 | ❌ 不通过；周期 1：Pump_Motor 预期 0，实际 True；Filling_Valve 预期 1，实际 False；周期 2：Pump_Motor 预期 0，实际 True；Capping_Machine 预期 1，实际 False；周期 3：Pump_Motor 预期 0，实际 True；Packing_Machine 预期 1，实际 False |

| 周期 | bottleSensor | cleaningConfirmButton | fillingConfirmButton | cappingConfirmButton | packingConfirmButton | finishedButton | 预期 Pump_Motor | 预期 Filling_Valve | 预期 Capping_Machine | 预期 Packing_Machine | 预期 Completion_Light | 实际 Pump_Motor | 实际 Filling_Valve | 实际 Capping_Machine | 实际 Packing_Machine | 实际 Completion_Light | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | cycle 1: pump ON | PASS |
| 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | to filling | FAIL |
| 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | to capping | FAIL |
| 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | to packing | FAIL |
| 4 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | to done | FAIL |
| 5 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | reset | FAIL |
| 6 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | cycle 2: next bottle starts the pump again | PASS |
| 7 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | cycle 2 continues normally | FAIL |

### TC03 Out-of-sequence buttons are ignored

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Out-of-sequence buttons are ignored |
| 所属题目 | E01 Automated Filling Line Control（`E01_Filling`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | confirm buttons only act in their own step; finishedButton has no effect before completion; no actuator starts in idle without a bottle |
| 实际输出及结果 | ❌ 不通过；周期 0：Pump_Motor 预期 0，实际 True；周期 5：Pump_Motor 预期 0，实际 True；Filling_Valve 预期 1，实际 False；周期 6：Pump_Motor 预期 0，实际 True；Filling_Valve 预期 1，实际 False |

| 周期 | bottleSensor | cleaningConfirmButton | fillingConfirmButton | cappingConfirmButton | packingConfirmButton | finishedButton | 预期 Pump_Motor | 预期 Filling_Valve | 预期 Capping_Machine | 预期 Packing_Machine | 预期 Completion_Light | 实际 Pump_Motor | 实际 Filling_Valve | 实际 Capping_Machine | 实际 Packing_Machine | 实际 Completion_Light | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | idle: buttons without a bottle do nothing | FAIL |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | bottle -> cleaning | PASS |
| 2 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | fillingConfirm during cleaning is ignored | PASS |
| 3 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | packingConfirm during cleaning is ignored | PASS |
| 4 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | finishedButton during cleaning is ignored | PASS |
| 5 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | correct button advances to filling | FAIL |
| 6 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | repeated cleaningConfirm in filling is ignored | FAIL |
| 7 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | cappingConfirm during filling is ignored | FAIL |
| 8 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | correct button advances to capping | FAIL |

### TC04 Completion light waits for pickup

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Completion light waits for pickup |
| 所属题目 | E01 Automated Filling Line Control（`E01_Filling`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | light stays ON until finishedButton; a new bottle signal or other buttons do not clear it |
| 实际输出及结果 | ❌ 不通过；周期 1：Pump_Motor 预期 0，实际 True；Filling_Valve 预期 1，实际 False；周期 2：Pump_Motor 预期 0，实际 True；Capping_Machine 预期 1，实际 False；周期 3：Pump_Motor 预期 0，实际 True；Packing_Machine 预期 1，实际 False |

| 周期 | bottleSensor | cleaningConfirmButton | fillingConfirmButton | cappingConfirmButton | packingConfirmButton | finishedButton | 预期 Pump_Motor | 预期 Filling_Valve | 预期 Capping_Machine | 预期 Packing_Machine | 预期 Completion_Light | 实际 Pump_Motor | 实际 Filling_Valve | 实际 Capping_Machine | 实际 Packing_Machine | 实际 Completion_Light | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | start | PASS |
| 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |  | FAIL |
| 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |  | FAIL |
| 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |  | FAIL |
| 4 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | light ON | FAIL |
| 5 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | packingConfirm held: light stays ON | FAIL |
| 6 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | other confirm buttons do not clear the light | FAIL |
| 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | still ON | FAIL |
| 8 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | only finishedButton clears the light | FAIL |

### TC05 A confirm button held in advance does not skip a step

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC05 A confirm button held in advance does not skip a step |
| 所属题目 | E01 Automated Filling Line Control（`E01_Filling`） |
| 初始状态 | power-up: step 0, all actuators off |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | edge-triggered confirmation: a button already held when its step is reached must not advance it; a fresh rising edge is required |
| 实际输出及结果 | ❌ 不通过；周期 0：Pump_Motor 预期 0，实际 True；周期 4：Filling_Valve 预期 1，实际 False；Pump_Motor 预期 0，实际 True；周期 5：Filling_Valve 预期 1，实际 False |

| 周期 | bottleSensor | cleaningConfirmButton | fillingConfirmButton | cappingConfirmButton | packingConfirmButton | finishedButton | 预期 Pump_Motor | 预期 Filling_Valve | 预期 Capping_Machine | 预期 Packing_Machine | 预期 Completion_Light | 实际 Pump_Motor | 实际 Filling_Valve | 实际 Capping_Machine | 实际 Packing_Machine | 实际 Completion_Light | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | confirm pressed early, no bottle yet: nothing happens | FAIL |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |  |  |  | 1 | 0 |  |  |  | DECISIVE: bottle arrives while the confirm button is already held. The cleaning step must be entered and must NOT be confirmed in the same scan, because the button has no rising edge | PASS |
| 2 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |  |  |  | 1 | 0 |  |  |  | still held: still cleaning | PASS |
| 3 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  | 1 |  |  |  |  | released: still cleaning | PASS |
| 4 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  | 1 | 0 |  |  |  | a fresh rising edge confirms cleaning -> filling | FAIL |
| 5 | 1 | 1 | 0 | 0 | 0 | 0 |  | 1 | 0 |  |  |  | 0 | 0 |  |  | held again: filling is not confirmed by the stale press | FAIL |

### TC06 A bottle that stays under the sensor does not restart the line

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC06 A bottle that stays under the sensor does not restart the line |
| 所属题目 | E01 Automated Filling Line Control（`E01_Filling`） |
| 初始状态 | power-up: idle, all actuators off |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | sensor held TRUE for many cycles: the latch must survive, the sensor must not re-trigger cleaning after the bottle has been processed, and a second bottle arriving later starts a new cycle |
| 实际输出及结果 | ❌ 不通过；周期 3：Filling_Valve 预期 1，实际 False；Pump_Motor 预期 0，实际 True；周期 4：Filling_Valve 预期 1，实际 False；周期 5：Capping_Machine 预期 1，实际 False |

| 周期 | bottleSensor | cleaningConfirmButton | fillingConfirmButton | cappingConfirmButton | packingConfirmButton | finishedButton | 预期 Pump_Motor | 预期 Filling_Valve | 预期 Capping_Machine | 预期 Packing_Machine | 预期 Completion_Light | 实际 Pump_Motor | 实际 Filling_Valve | 实际 Capping_Machine | 实际 Packing_Machine | 实际 Completion_Light | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  | 1 |  |  |  |  | bottle arrives -> cleaning starts | PASS |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  | 1 |  |  |  |  | sensor still TRUE: the latch holds, no repeated start | PASS |
| 2 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  | 1 |  |  |  |  | sensor still TRUE: still the same cleaning step | PASS |
| 3 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  | 1 | 0 |  |  |  | cleaning confirmed while the bottle is still under the sensor | FAIL |
| 4 | 1 | 0 | 0 | 0 | 0 | 0 |  | 1 |  |  |  |  | 0 |  |  |  | sensor still TRUE and cleaning is over: the line must NOT go back to cleaning, the bottle is the same one | FAIL |
| 5 | 1 | 0 | 1 | 0 | 0 | 0 |  | 0 | 1 |  |  |  | 0 | 0 |  |  | filling confirmed | FAIL |
| 6 | 1 | 0 | 0 | 1 | 0 | 0 |  |  | 0 | 1 |  |  |  | 0 | 0 |  | capping confirmed | FAIL |
| 7 | 1 | 0 | 0 | 0 | 1 | 0 |  |  |  | 0 | 1 |  |  |  | 0 | 0 | packing confirmed | FAIL |
| 8 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |  |  |  | 0 | 1 |  |  |  | 0 | bottle picked up while the sensor still reads TRUE: back to idle and the stale sensor level must not start a new cycle, because there is no rising edge | FAIL |
| 9 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  | 1 |  |  |  |  | sensor still TRUE, idle: nothing starts without a new rising edge | FAIL |
| 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  | 1 |  |  |  |  | bottle removed: sensor FALSE | FAIL |
| 11 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  | 1 |  |  |  |  | a second bottle gives a fresh rising edge: a new cycle starts | PASS |


## E02 Dual-Word Edge Detection（`E02_DualEdge`）

- 编译：**未通过**（用例记为未通过）；用例通过 0/4；整题未通过

- 仿真器无法执行：无法解析的表达式片段 '<'

### TC01 Single-bit rising and falling edges

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Single-bit rising and falling edges |
| 所属题目 | E02 Dual-Word Edge Detection（`E02_DualEdge`） |
| 初始状态 | power-up, previous value treated as 0 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | first invocation, one bit set, one bit cleared, no change |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 无法解析的表达式片段 '<' |

| 周期 | value | 预期 hasChanged | 预期 hasRisingEdges | 预期 risingBits | 预期 noOfRisingBits | 预期 hasFallingEdges | 预期 fallingBits | 预期 noOfFallingBits | 实际 hasChanged | 实际 hasRisingEdges | 实际 risingBits | 实际 noOfRisingBits | 实际 hasFallingEdges | 实际 fallingBits | 实际 noOfFallingBits | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  | no change from the initial zero value | FAIL |
| 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |  |  |  |  |  |  |  | bit0 rises | 未执行 |
| 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  | unchanged -> no edges | 未执行 |
| 3 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 1 |  |  |  |  |  |  |  | bit0 falls | 未执行 |
| 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  | unchanged | 未执行 |

### TC02 Multiple simultaneous edges

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Multiple simultaneous edges |
| 所属题目 | E02 Dual-Word Edge Detection（`E02_DualEdge`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | several bits rise and fall in the same cycle, counts are correct |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 无法解析的表达式片段 '<' |

| 周期 | value | 预期 hasChanged | 预期 hasRisingEdges | 预期 risingBits | 预期 noOfRisingBits | 预期 hasFallingEdges | 预期 fallingBits | 预期 noOfFallingBits | 实际 hasChanged | 实际 hasRisingEdges | 实际 risingBits | 实际 noOfRisingBits | 实际 hasFallingEdges | 实际 fallingBits | 实际 noOfFallingBits | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 15 | 1 | 1 | 15 | 4 | 0 | 0 | 0 |  |  |  |  |  |  |  | four bits rise at once | FAIL |
| 1 | 240 | 1 | 1 | 240 | 4 | 1 | 15 | 4 |  |  |  |  |  |  |  | four rise and four fall in the same cycle | 未执行 |
| 2 | 255 | 1 | 1 | 15 | 4 | 0 | 0 | 0 |  |  |  |  |  |  |  | four more rise, none fall | 未执行 |
| 3 | 0 | 1 | 0 | 0 | 0 | 1 | 255 | 8 |  |  |  |  |  |  |  | all eight fall | 未执行 |

### TC03 Boundary bits and full word

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Boundary bits and full word |
| 所属题目 | E02 Dual-Word Edge Detection（`E02_DualEdge`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | bit31 (most significant), all 32 bits at once, maximum counts |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 无法解析的表达式片段 '<' |

| 周期 | value | 预期 hasChanged | 预期 hasRisingEdges | 预期 risingBits | 预期 noOfRisingBits | 预期 hasFallingEdges | 预期 fallingBits | 预期 noOfFallingBits | 实际 hasChanged | 实际 hasRisingEdges | 实际 risingBits | 实际 noOfRisingBits | 实际 hasFallingEdges | 实际 fallingBits | 实际 noOfFallingBits | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 2147483648 | 1 | 1 | 2147483648 | 1 | 0 | 0 | 0 |  |  |  |  |  |  |  | bit31 rises | FAIL |
| 1 | 4294967295 | 1 | 1 | 2147483647 | 31 | 0 | 0 | 0 |  |  |  |  |  |  |  | the remaining 31 bits rise, count 31 | 未执行 |
| 2 | 4294967295 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  | unchanged | 未执行 |
| 3 | 0 | 1 | 0 | 0 | 0 | 1 | 4294967295 | 32 |  |  |  |  |  |  |  | all 32 bits fall, count 32 | 未执行 |
| 4 | 4294967295 | 1 | 1 | 4294967295 | 32 | 0 | 0 | 0 |  |  |  |  |  |  |  | all 32 bits rise, count 32 | 未执行 |

### TC04 Alternating patterns

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Alternating patterns |
| 所属题目 | E02 Dual-Word Edge Detection（`E02_DualEdge`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | interleaved bit patterns, rising and falling masks are disjoint |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 无法解析的表达式片段 '<' |

| 周期 | value | 预期 hasChanged | 预期 hasRisingEdges | 预期 risingBits | 预期 noOfRisingBits | 预期 hasFallingEdges | 预期 fallingBits | 预期 noOfFallingBits | 实际 hasChanged | 实际 hasRisingEdges | 实际 risingBits | 实际 noOfRisingBits | 实际 hasFallingEdges | 实际 fallingBits | 实际 noOfFallingBits | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 2863311530 | 1 | 1 | 2863311530 | 16 | 0 | 0 | 0 |  |  |  |  |  |  |  | 16 odd bits rise | FAIL |
| 1 | 1431655765 | 1 | 1 | 1431655765 | 16 | 1 | 2863311530 | 16 |  |  |  |  |  |  |  | 16 rise, 16 fall simultaneously | 未执行 |
| 2 | 1431655765 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  | unchanged | 未执行 |
| 3 | 1431633920 | 1 | 0 | 0 | 0 | 1 | 21845 | 8 |  |  |  |  |  |  |  | upper half kept, lower half falls | 未执行 |


## E03 Alarm Handling（`E03_Hysteresis`）

- 编译：通过；用例通过 3/5；整题未通过

### TC01 High alarm with hysteresis

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 High alarm with hysteresis |
| 所属题目 | E03 Alarm Handling（`E03_Hysteresis`） |
| 初始状态 | power-up, all outputs FALSE/0; hiLevel=80, loLevel=20, hystWindow=5 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | trigger above hiLevel, hold inside window, boundary Value=hiLevel-hystWindow, release, Value=hiLevel does not trigger |
| 实际输出及结果 | ❌ 不通过；周期 2：hiAlarm 预期 1，实际 False；周期 3：hiAlarm 预期 1，实际 False |

| 周期 | Value | hiLevel | loLevel | hystWindow | 预期 hiAlarm | 预期 loAlarm | 预期 error | 预期 status | 实际 hiAlarm | 实际 loAlarm | 实际 error | 实际 status | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 50 | 80 | 20 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | normal range, no alarm | PASS |
| 1 | 85 | 80 | 20 | 5 | 1 | 0 |  |  | 1 | 0 |  |  | Value>hiLevel triggers hiAlarm | PASS |
| 2 | 78 | 80 | 20 | 5 | 1 |  |  |  | 0 |  |  |  | inside hysteresis window, alarm held | FAIL |
| 3 | 75 | 80 | 20 | 5 | 1 |  |  |  | 0 |  |  |  | Value=hiLevel-hystWindow is not < 75, alarm held | FAIL |
| 4 | 74 | 80 | 20 | 5 | 0 |  |  |  | 0 |  |  |  | Value<hiLevel-hystWindow releases hiAlarm | PASS |
| 5 | 80 | 80 | 20 | 5 | 0 |  |  |  | 0 |  |  |  | Value=hiLevel is not > hiLevel, no re-trigger | PASS |
| 6 | 81 | 80 | 20 | 5 | 1 |  |  |  | 1 |  |  |  | Value>hiLevel re-triggers | PASS |

### TC02 Low alarm with hysteresis

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Low alarm with hysteresis |
| 所属题目 | E03 Alarm Handling（`E03_Hysteresis`） |
| 初始状态 | power-up; hiLevel=80, loLevel=20, hystWindow=5 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | trigger below loLevel, hold inside window, boundary Value=loLevel+hystWindow, release, Value=loLevel does not trigger |
| 实际输出及结果 | ❌ 不通过；周期 2：loAlarm 预期 1，实际 False；周期 3：loAlarm 预期 1，实际 False |

| 周期 | Value | hiLevel | loLevel | hystWindow | 预期 hiAlarm | 预期 loAlarm | 预期 error | 预期 status | 实际 hiAlarm | 实际 loAlarm | 实际 error | 实际 status | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 50 | 80 | 20 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | normal range | PASS |
| 1 | 15 | 80 | 20 | 5 | 0 | 1 |  |  | 0 | 1 |  |  | Value<loLevel triggers loAlarm | PASS |
| 2 | 22 | 80 | 20 | 5 |  | 1 |  |  |  | 0 |  |  | inside window, alarm held | FAIL |
| 3 | 25 | 80 | 20 | 5 |  | 1 |  |  |  | 0 |  |  | Value=loLevel+hystWindow is not > 25, alarm held | FAIL |
| 4 | 26 | 80 | 20 | 5 |  | 0 |  |  |  | 0 |  |  | Value>loLevel+hystWindow releases loAlarm | PASS |
| 5 | 20 | 80 | 20 | 5 |  | 0 |  |  |  | 0 |  |  | Value=loLevel is not < loLevel, no re-trigger | PASS |
| 6 | 19 | 80 | 20 | 5 |  | 1 |  |  |  | 1 |  |  | Value<loLevel re-triggers | PASS |

### TC03 Error 16#8001: loLevel >= hiLevel

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Error 16#8001: loLevel >= hiLevel |
| 所属题目 | E03 Alarm Handling（`E03_Hysteresis`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | loLevel>hiLevel, loLevel=hiLevel boundary, 8001 has priority over 8002 |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Value | hiLevel | loLevel | hystWindow | 预期 error | 预期 status | 实际 error | 实际 status | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 50 | 20 | 80 | 5 | 1 | 32769 | 1 | 32769 | loLevel>hiLevel -> 16#8001 | PASS |
| 1 | 50 | 50 | 50 | 5 | 1 | 32769 | 1 | 32769 | loLevel=hiLevel -> 16#8001 | PASS |
| 2 | 50 | 20 | 80 | 100 | 1 | 32769 | 1 | 32769 | both conditions violated: 16#8001 takes priority | PASS |

### TC04 Error 16#8002: hysteresis window too large

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Error 16#8002: hysteresis window too large |
| 所属题目 | E03 Alarm Handling（`E03_Hysteresis`） |
| 初始状态 | power-up; hiLevel=80, loLevel=20 (range 60) |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | hystWindow > range, hystWindow = range boundary, hystWindow just below range is valid |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Value | hiLevel | loLevel | hystWindow | 预期 error | 预期 status | 实际 error | 实际 status | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 50 | 80 | 20 | 70 | 1 | 32770 | 1 | 32770 | hystWindow>60 -> 16#8002 | PASS |
| 1 | 50 | 80 | 20 | 60 | 1 | 32770 | 1 | 32770 | hystWindow=60 (boundary) -> 16#8002 | PASS |
| 2 | 50 | 80 | 20 | 59 | 0 | 0 | 0 | 0 | hystWindow=59 is valid | PASS |

### TC05 Recovery after parameter error

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC05 Recovery after parameter error |
| 所属题目 | E03 Alarm Handling（`E03_Hysteresis`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | error clears when parameters are corrected, alarm logic works again |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Value | hiLevel | loLevel | hystWindow | 预期 error | 预期 status | 预期 hiAlarm | 预期 loAlarm | 实际 error | 实际 status | 实际 hiAlarm | 实际 loAlarm | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 50 | 20 | 80 | 5 | 1 | 32769 |  |  | 1 | 32769 |  |  | invalid limits | PASS |
| 1 | 50 | 80 | 20 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | limits corrected, error cleared | PASS |
| 2 | 90 | 80 | 20 | 5 | 0 | 0 | 1 |  | 0 | 0 | 1 |  | alarm logic active again | PASS |


## E04 Jam Pump Debouncing and Runtime Maintenance（`E04_JamPump`）

- 编译：通过；用例通过 0/4；整题未通过

### TC01 Debounce before the pump may run

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Debounce before the pump may run |
| 所属题目 | E04 Jam Pump Debouncing and Runtime Maintenance（`E04_JamPump`） |
| 初始状态 | power-up: VFD_RUN FALSE, runtime 0, maintenance FALSE; DebounceTime=1000ms |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | power-up state, viscosity held shorter than DebounceTime, run after the full debounce |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 定时器只支持 .Q / .ET 成员，实际是 .IN |

| 周期 | VISCOSITY_OK | PASTE_E_STOP_NC | DebounceTime | CycleTime | 预期 VFD_RUN | 预期 PUMP_MAINT_DUE | 预期 PUMP_RUNTIME_ACC | 实际 VFD_RUN | 实际 PUMP_MAINT_DUE | 实际 PUMP_RUNTIME_ACC | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 1000 | 100 | 0 | 0 | 0 |  |  |  | power-up: everything off | FAIL |
| 1（保持 800 ms） | 1 | 1 | 1000 | 100 | 0 |  |  |  |  |  | viscosity valid, debounce running | 未执行 |
| 2（保持 400 ms） | 1 | 1 | 1000 | 100 | 1 |  |  |  |  |  | full DebounceTime elapsed -> pump runs | 未执行 |
| 3（保持 200 ms） | 1 | 1 | 1000 | 100 | 1 |  |  |  |  |  | keeps running | 未执行 |

### TC02 Viscosity loss stops the pump and clears timing

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Viscosity loss stops the pump and clears timing |
| 所属题目 | E04 Jam Pump Debouncing and Runtime Maintenance（`E04_JamPump`） |
| 初始状态 | power-up; DebounceTime=1000ms |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | FALSE stops the pump immediately, debounce restarts from zero |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 定时器只支持 .Q / .ET 成员，实际是 .IN |

| 周期 | VISCOSITY_OK | PASTE_E_STOP_NC | DebounceTime | CycleTime | 预期 VFD_RUN | 实际 VFD_RUN | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|
| 0（保持 1200 ms） | 1 | 1 | 1000 | 100 | 1 |  | running after the debounce | FAIL |
| 1 | 0 | 1 | 1000 | 100 | 0 |  | viscosity lost -> stop immediately | 未执行 |
| 2（保持 500 ms） | 1 | 1 | 1000 | 100 | 0 |  | new demand: not yet debounced | 未执行 |
| 3（保持 600 ms） | 1 | 1 | 1000 | 100 | 1 |  | full debounce again -> running | 未执行 |

### TC03 Emergency stop has priority and clears debounce timing

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Emergency stop has priority and clears debounce timing |
| 所属题目 | E04 Jam Pump Debouncing and Runtime Maintenance（`E04_JamPump`） |
| 初始状态 | power-up; DebounceTime=1000ms |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | e-stop stops the pump, blocks starting, requires a full debounce after release |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 定时器只支持 .Q / .ET 成员，实际是 .IN |

| 周期 | VISCOSITY_OK | PASTE_E_STOP_NC | DebounceTime | CycleTime | 预期 VFD_RUN | 实际 VFD_RUN | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|
| 0（保持 1200 ms） | 1 | 1 | 1000 | 100 | 1 |  | running | FAIL |
| 1 | 1 | 0 | 1000 | 100 | 0 |  | E-STOP -> stop immediately | 未执行 |
| 2（保持 1500 ms） | 1 | 0 | 1000 | 100 | 0 |  | cannot start while the e-stop is active | 未执行 |
| 3 | 1 | 1 | 1000 | 100 | 0 |  | released: debounce was cleared | 未执行 |
| 4（保持 1100 ms） | 1 | 1 | 1000 | 100 | 1 |  | full debounce -> running again | 未执行 |

### TC04 Runtime accumulation and the maintenance indication

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Runtime accumulation and the maintenance indication |
| 所属题目 | E04 Jam Pump Debouncing and Runtime Maintenance（`E04_JamPump`） |
| 初始状态 | power-up; DebounceTime=0ms, CycleTime=100h per invocation |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | runtime accumulates only while running, preserved while stopped, flag at 500 h, flag does not affect the pump |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 定时器只支持 .Q / .ET 成员，实际是 .IN |

| 周期 | VISCOSITY_OK | PASTE_E_STOP_NC | DebounceTime | CycleTime | 预期 VFD_RUN | 预期 PUMP_RUNTIME_ACC | 预期 PUMP_MAINT_DUE | 实际 VFD_RUN | 实际 PUMP_RUNTIME_ACC | 实际 PUMP_MAINT_DUE | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 360000000 | 1 | 360000000 | 0 |  |  |  | 100h | FAIL |
| 1 | 1 | 1 | 0 | 360000000 |  | 720000000 | 0 |  |  |  | 200h | 未执行 |
| 2 | 0 | 1 | 0 | 360000000 | 0 | 720000000 |  |  |  |  | stopped -> runtime preserved | 未执行 |
| 3 | 1 | 1 | 0 | 360000000 | 1 | 1080000000 |  |  |  |  | 300h | 未执行 |
| 4 | 1 | 1 | 0 | 360000000 |  | 1440000000 | 0 |  |  |  | 400h: still below | 未执行 |
| 5 | 1 | 1 | 0 | 360000000 |  | 1800000000 | 1 |  |  |  | 500h -> maintenance due | 未执行 |
| 6 | 1 | 1 | 0 | 360000000 | 1 |  | 1 |  |  |  | flag does not affect the pump | 未执行 |


## E05 Weld Gap Alarm and Startup Inhibition（`E05_WeldGap`）

- 编译：通过；用例通过 3/3；整题通过

### TC01 Power-up inhibition period

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Power-up inhibition period |
| 所属题目 | E05 Weld Gap Alarm and Startup Inhibition（`E05_WeldGap`） |
| 初始状态 | power-up, Weld_E_Stop_NC=1, DebounceTime=200ms |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | soft-start active for 5s, alarm suppressed during inhibition, debounce does not accumulate, monitoring resumes afterwards |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Gap_Exceeded | Weld_E_Stop_NC | DebounceTime | 预期 Operator_Alert | 预期 Weld_Soft_Start_Active | 实际 Operator_Alert | 实际 Weld_Soft_Start_Active | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 200 | 0 | 1 | 0 | 1 | power-up: inhibition active | PASS |
| 1（保持 3000 ms） | 1 | 1 | 200 | 0 | 1 | 0 | 1 | gap during inhibition: no alarm | PASS |
| 2 | 1 | 1 | 200 | 0 | 1 | 0 | 1 | 3s elapsed: still inhibited, debounce not accumulating | PASS |
| 3（保持 2100 ms） | 1 | 1 | 200 | 0 | 0 | 0 | 0 | 5s elapsed: inhibition ends; debounce starts now from zero | PASS |
| 4（保持 300 ms） | 1 | 1 | 200 | 1 | 0 | 1 | 0 | gap held for DebounceTime after init -> alarm | PASS |

### TC02 Debounce during normal monitoring

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Debounce during normal monitoring |
| 所属题目 | E05 Weld Gap Alarm and Startup Inhibition（`E05_WeldGap`） |
| 初始状态 | after the 5s inhibition, DebounceTime=500ms |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | alarm only after DebounceTime, short gap ignored, signal FALSE clears alarm and timing |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Gap_Exceeded | Weld_E_Stop_NC | DebounceTime | 预期 Operator_Alert | 预期 Weld_Soft_Start_Active | 实际 Operator_Alert | 实际 Weld_Soft_Start_Active | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|
| 0（保持 5200 ms） | 0 | 1 | 500 | 0 | 0 | 0 | 0 | initialisation finished | PASS |
| 1（保持 300 ms） | 1 | 1 | 500 | 0 |  | 0 |  | gap appears, debounce running | PASS |
| 2 | 0 | 1 | 500 | 0 |  | 0 |  | gap disappears before 500ms -> no alarm, timing cleared | PASS |
| 3（保持 300 ms） | 1 | 1 | 500 | 0 |  | 0 |  | new gap: full debounce required again | PASS |
| 4（保持 300 ms） | 1 | 1 | 500 | 1 |  | 1 |  | 500ms reached -> alarm | PASS |
| 5（保持 500 ms） | 1 | 1 | 500 | 1 |  | 1 |  | alarm held while gap persists | PASS |
| 6 | 0 | 1 | 500 | 0 |  | 0 |  | gap cleared -> alarm off immediately | PASS |

### TC03 Emergency stop priority

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Emergency stop priority |
| 所属题目 | E05 Weld Gap Alarm and Startup Inhibition（`E05_WeldGap`） |
| 初始状态 | after initialisation, DebounceTime=400ms |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | estop clears alarm immediately, blocks alarm during inhibition and monitoring, debounce cleared, full debounce after release |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Gap_Exceeded | Weld_E_Stop_NC | DebounceTime | 预期 Operator_Alert | 预期 Weld_Soft_Start_Active | 实际 Operator_Alert | 实际 Weld_Soft_Start_Active | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|
| 0（保持 5200 ms） | 0 | 1 | 400 | 0 | 0 | 0 | 0 | ready | PASS |
| 1（保持 500 ms） | 1 | 1 | 400 | 1 |  | 1 |  | alarm active | PASS |
| 2 | 1 | 0 | 400 | 0 |  | 0 |  | E-STOP -> alarm off immediately | PASS |
| 3（保持 1000 ms） | 1 | 0 | 400 | 0 |  | 0 |  | alarm stays off while e-stop active | PASS |
| 4 | 1 | 1 | 400 | 0 |  | 0 |  | released: debounce was cleared, not yet alarming | PASS |
| 5（保持 500 ms） | 1 | 1 | 400 | 1 |  | 1 |  | after a full DebounceTime -> alarm again | PASS |


## E06 Aeration Blower Delayed Start（`E06_Blower`）

- 编译：通过；用例通过 3/3；整题通过

### TC01 5-second start delay

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 5-second start delay |
| 所属题目 | E06 Aeration Blower Delayed Start（`E06_Blower`） |
| 初始状态 | power-up: BLOWER_RUN FALSE, count 0 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | power-up state, no run before 5s, run after 5s, count incremented once |
| 实际输出及结果 | ✅ 通过 |

| 周期 | DO_LOW | AERATION_E_STOP_NC | 预期 BLOWER_RUN | 预期 AERATION_BLOWER_CYCLE_COUNT | 实际 BLOWER_RUN | 实际 AERATION_BLOWER_CYCLE_COUNT | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 0 | 0 | power-up | PASS |
| 1（保持 3000 ms） | 1 | 1 | 0 | 0 | 0 | 0 | demand starts the delay | PASS |
| 2（保持 1900 ms） | 1 | 1 | 0 | 0 | 0 | 0 | 3s: still waiting | PASS |
| 3（保持 200 ms） | 1 | 1 | 1 | 1 | 1 | 1 | 5s reached -> blower runs, count 1 | PASS |
| 4（保持 3000 ms） | 1 | 1 | 1 | 1 | 1 | 1 | continuous running does not increment the count | PASS |

### TC02 Demand loss resets the delay

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Demand loss resets the delay |
| 所属题目 | E06 Aeration Blower Delayed Start（`E06_Blower`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | DO_LOW FALSE stops immediately, partial timing discarded, full 5s required again |
| 实际输出及结果 | ✅ 通过 |

| 周期 | DO_LOW | AERATION_E_STOP_NC | 预期 BLOWER_RUN | 预期 AERATION_BLOWER_CYCLE_COUNT | 实际 BLOWER_RUN | 实际 AERATION_BLOWER_CYCLE_COUNT | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|
| 0（保持 3000 ms） | 1 | 1 | 0 |  | 0 |  | delay running | PASS |
| 1 | 0 | 1 | 0 |  | 0 |  | demand lost at 3s -> timer reset | PASS |
| 2（保持 3000 ms） | 1 | 1 | 0 |  | 0 |  | new demand: 3s is not enough because timing restarted | PASS |
| 3（保持 1900 ms） | 1 | 1 | 0 |  | 0 |  | still below 5s | PASS |
| 4（保持 200 ms） | 1 | 1 | 1 | 1 | 1 | 1 | 5s of continuous demand -> run | PASS |
| 5 | 0 | 1 | 0 | 1 | 0 | 1 | demand lost while running -> stop immediately | PASS |
| 6（保持 4900 ms） | 1 | 1 | 0 | 1 | 0 | 1 | restart requires the full 5s again | PASS |
| 7（保持 200 ms） | 1 | 1 | 1 | 2 | 1 | 2 | second start -> count 2 | PASS |

### TC03 Emergency stop priority

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Emergency stop priority |
| 所属题目 | E06 Aeration Blower Delayed Start（`E06_Blower`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | estop stops the blower, blocks starting, resets timing, count unchanged by estop |
| 实际输出及结果 | ✅ 通过 |

| 周期 | DO_LOW | AERATION_E_STOP_NC | 预期 BLOWER_RUN | 预期 AERATION_BLOWER_CYCLE_COUNT | 实际 BLOWER_RUN | 实际 AERATION_BLOWER_CYCLE_COUNT | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|
| 0（保持 5200 ms） | 1 | 1 | 1 | 1 | 1 | 1 | demand held for 5 s -> blower running, first start counted | PASS |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | still running | PASS |
| 2 | 1 | 0 | 0 | 1 | 0 | 1 | E-STOP -> stop immediately, count unchanged | PASS |
| 3（保持 6000 ms） | 1 | 0 | 0 | 1 | 0 | 1 | cannot start during e-stop | PASS |
| 4 | 1 | 1 | 0 | 1 | 0 | 1 | released: timing restarted, not running yet | PASS |
| 5（保持 5200 ms） | 1 | 1 | 1 | 2 | 1 | 2 | after a full 5s -> running, count 2 | PASS |


## M01 Multi-Pump Switching Control System（`M01_PumpSwitch`）

- 编译：**未通过**（用例记为未通过）；用例通过 0/3；整题未通过

- 仿真器无法执行：期望 ':='，实际是 'bStartRisingEdge'

### TC01 Manual mode runs the selected pumps

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Manual mode runs the selected pumps |
| 所属题目 | M01 Multi-Pump Switching Control System（`M01_PumpSwitch`） |
| 初始状态 | power-up, mode=0 (manual), no pump running |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | start runs selected pumps, selection changes are followed, stop stops all |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'bStartRisingEdge' |

| 周期 | mode | start | stop | pumpGroup[1].priority | pumpGroup[1].selection | pumpGroup[2].priority | pumpGroup[2].selection | pumpGroup[3].priority | pumpGroup[3].selection | pumpGroup[4].priority | pumpGroup[4].selection | pumpGroup[5].priority | pumpGroup[5].selection | 预期 pumpGroup[1].RunComd | 预期 pumpGroup[2].RunComd | 预期 pumpGroup[3].RunComd | 预期 pumpGroup[4].RunComd | 预期 pumpGroup[5].RunComd | 实际 pumpGroup[1].RunComd | 实际 pumpGroup[2].RunComd | 实际 pumpGroup[3].RunComd | 实际 pumpGroup[4].RunComd | 实际 pumpGroup[5].RunComd | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  | not started yet -> all stopped | FAIL |
| 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |  |  |  |  |  | start -> selected pumps 1 and 3 run | 未执行 |
| 2 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |  |  |  |  |  | button released -> still running | 未执行 |
| 3 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 |  |  |  |  |  | selection changed -> pumps follow | 未执行 |
| 4 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  | stop -> all pumps stop | 未执行 |
| 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  | stays stopped until start | 未执行 |

### TC02 Automatic mode runs the three highest priorities

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Automatic mode runs the three highest priorities |
| 所属题目 | M01 Multi-Pump Switching Control System（`M01_PumpSwitch`） |
| 初始状态 | power-up, mode=1 (automatic) |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | 3 duty / 2 standby selection, priority ranking, selection ignored in auto |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'bStartRisingEdge' |

| 周期 | mode | start | stop | pumpGroup[1].priority | pumpGroup[1].selection | pumpGroup[2].priority | pumpGroup[2].selection | pumpGroup[3].priority | pumpGroup[3].selection | pumpGroup[4].priority | pumpGroup[4].selection | pumpGroup[5].priority | pumpGroup[5].selection | 预期 pumpGroup[1].RunComd | 预期 pumpGroup[2].RunComd | 预期 pumpGroup[3].RunComd | 预期 pumpGroup[4].RunComd | 预期 pumpGroup[5].RunComd | 实际 pumpGroup[1].RunComd | 实际 pumpGroup[2].RunComd | 实际 pumpGroup[3].RunComd | 实际 pumpGroup[4].RunComd | 实际 pumpGroup[5].RunComd | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 10 | 0 | 50 | 0 | 30 | 0 | 40 | 0 | 20 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  | not started yet | FAIL |
| 1 | 1 | 1 | 0 | 10 | 0 | 50 | 0 | 30 | 0 | 40 | 0 | 20 | 0 | 0 | 1 | 1 | 1 | 0 |  |  |  |  |  | top three priorities (50,40,30) = pumps 2,4,3 | 未执行 |
| 2 | 1 | 1 | 0 | 10 | 1 | 50 | 0 | 30 | 0 | 40 | 0 | 20 | 1 | 0 | 1 | 1 | 1 | 0 |  |  |  |  |  | manual selection ignored in automatic mode | 未执行 |
| 3 | 1 | 1 | 0 | 90 | 0 | 10 | 0 | 20 | 0 | 30 | 0 | 40 | 0 | 1 | 0 | 0 | 1 | 1 |  |  |  |  |  | priorities changed -> pumps 1,5,4 run | 未执行 |
| 4 | 1 | 0 | 1 | 90 | 0 | 10 | 0 | 20 | 0 | 30 | 0 | 40 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  | stop -> all stop | 未执行 |

### TC03 Mode switching and priority ties

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Mode switching and priority ties |
| 所属题目 | M01 Multi-Pump Switching Control System（`M01_PumpSwitch`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | switching between manual and automatic, equal priorities still select exactly three pumps |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'bStartRisingEdge' |

| 周期 | mode | start | stop | pumpGroup[1].priority | pumpGroup[1].selection | pumpGroup[2].priority | pumpGroup[2].selection | pumpGroup[3].priority | pumpGroup[3].selection | pumpGroup[4].priority | pumpGroup[4].selection | pumpGroup[5].priority | pumpGroup[5].selection | 预期 pumpGroup[1].RunComd | 预期 pumpGroup[2].RunComd | 预期 pumpGroup[3].RunComd | 预期 pumpGroup[4].RunComd | 预期 pumpGroup[5].RunComd | 实际 pumpGroup[1].RunComd | 实际 pumpGroup[2].RunComd | 实际 pumpGroup[3].RunComd | 实际 pumpGroup[4].RunComd | 实际 pumpGroup[5].RunComd | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 |  |  |  |  |  | manual: two selected pumps | FAIL |
| 1 | 1 | 1 | 0 | 5 | 1 | 4 | 1 | 3 | 0 | 2 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 |  |  |  |  |  | switch to automatic -> top three (5,4,3) | 未执行 |
| 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |  |  |  |  |  | back to manual -> only the selected pump | 未执行 |
| 3 | 1 | 1 | 0 | 7 | 0 | 7 | 0 | 7 | 0 | 7 | 0 | 7 | 0 | 1 | 1 | 1 | 0 | 0 |  |  |  |  |  | all priorities equal -> exactly three pumps run | 未执行 |


## M02 Analog Batch Processing（`M02_AnalogBatch`）

- 编译：**未通过**（用例记为未通过）；用例通过 0/3；整题未通过

- 仿真器无法执行：期望 ':='，实际是 'FOR'

### TC01 Unipolar and bipolar linear scaling (mode 0)

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Unipolar and bipolar linear scaling (mode 0) |
| 所属题目 | M02 Analog Batch Processing（`M02_AnalogBatch`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | raw 0, mid and full scale mapped to the engineering range, bipolar negative range |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'FOR' |

| 周期 | count | analogValues[1] | channels[1].enable | channels[1].hiLIM | channels[1].loLIM | channels[1].bipolar | channels[1].measuringMode | analogValues[2] | channels[2].enable | channels[2].hiLIM | channels[2].loLIM | channels[2].bipolar | channels[2].measuringMode | 预期 channels[1].outputValue | 预期 channels[1].retVal | 预期 channels[2].outputValue | 预期 channels[2].retVal | 实际 channels[1].outputValue | 实际 channels[1].retVal | 实际 channels[2].outputValue | 实际 channels[2].retVal | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 2 | 0 | 1 | 100.0 | 0.0 | 0 | 0 | 27648 | 1 | 100.0 | 0.0 | 0 | 0 | 0.0 | 0 | 100.0 | 0 |  |  |  |  | unipolar: 0 -> loLIM, 27648 -> hiLIM | FAIL |
| 1 | 2 | 13824 | 1 | 100.0 | 0.0 | 0 | 0 | 13824 | 1 | 200.0 | 100.0 | 0 | 0 | 50.0 | 0 | 150.0 | 0 |  |  |  |  | unipolar mid scale | 未执行 |
| 2 | 2 | -27648 | 1 | 100.0 | -100.0 | 1 | 0 | 27648 | 1 | 100.0 | -100.0 | 1 | 0 | -100.0 | 0 | 100.0 | 0 |  |  |  |  | bipolar: -27648 -> loLIM, 27648 -> hiLIM | 未执行 |
| 3 | 1 | 0 | 1 | 100.0 | -100.0 | 1 | 0 |  |  |  |  |  |  | 0.0 | 0 |  |  |  |  |  |  | bipolar zero -> midpoint of the range | 未执行 |

### TC02 Temperature conversions (modes 1 and 2)

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Temperature conversions (modes 1 and 2) |
| 所属题目 | M02 Analog Batch Processing（`M02_AnalogBatch`） |
| 初始状态 | power-up; limits set to a valid range (the limit check applies to every mode) |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | standard temperature = raw/10, climatic temperature = raw/100, negative values |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'FOR' |

| 周期 | count | analogValues[1] | channels[1].enable | channels[1].hiLIM | channels[1].loLIM | channels[1].bipolar | channels[1].measuringMode | analogValues[2] | channels[2].enable | channels[2].hiLIM | channels[2].loLIM | channels[2].bipolar | channels[2].measuringMode | 预期 channels[1].outputValue | 预期 channels[1].retVal | 预期 channels[2].outputValue | 预期 channels[2].retVal | 实际 channels[1].outputValue | 实际 channels[1].retVal | 实际 channels[2].outputValue | 实际 channels[2].retVal | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 2 | 250 | 1 | 100.0 | 0.0 | 0 | 1 | 2500 | 1 | 100.0 | 0.0 | 0 | 2 | 25.0 | 0 | 25.0 | 0 |  |  |  |  | mode 1: 250 -> 25.0; mode 2: 2500 -> 25.0 | FAIL |
| 1 | 2 | -125 | 1 | 100.0 | 0.0 | 0 | 1 | -1250 | 1 | 100.0 | 0.0 | 0 | 2 | -12.5 | 0 | -12.5 | 0 |  |  |  |  | negative temperatures | 未执行 |
| 2 | 1 | 0 | 1 | 100.0 | 0.0 | 0 | 1 |  |  |  |  |  |  | 0.0 | 0 |  |  |  |  |  |  | zero raw value | 未执行 |

### TC03 Error handling and enable flag

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Error handling and enable flag |
| 所属题目 | M02 Analog Batch Processing（`M02_AnalogBatch`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | invalid mode -> 16#8001, hiLIM <= loLIM -> 16#8002, disabled channels are skipped, count limits processing |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'FOR' |

| 周期 | count | analogValues[1] | channels[1].enable | channels[1].hiLIM | channels[1].loLIM | channels[1].bipolar | channels[1].measuringMode | analogValues[2] | channels[2].enable | channels[2].hiLIM | channels[2].loLIM | channels[2].bipolar | channels[2].measuringMode | 预期 channels[1].retVal | 预期 channels[2].outputValue | 预期 channels[2].retVal | 预期 channels[1].outputValue | 实际 channels[1].retVal | 实际 channels[2].outputValue | 实际 channels[2].retVal | 实际 channels[1].outputValue | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 2 | 13824 | 1 | 100.0 | 0.0 | 0 | 5 | 13824 | 1 | 100.0 | 0.0 | 0 | 0 | 32769 | 50.0 | 0 |  |  |  |  |  | channel 1 invalid mode -> 16#8001, channel 2 still converted | FAIL |
| 1 | 2 | 13824 | 1 | 0.0 | 100.0 | 0 | 0 | 13824 | 1 | 50.0 | 50.0 | 0 | 0 | 32770 |  | 32770 |  |  |  |  |  | hiLIM < loLIM and hiLIM = loLIM -> 16#8002 | 未执行 |
| 2 | 2 | 13824 | 0 | 100.0 | 0.0 | 0 | 0 | 13824 | 1 | 100.0 | 0.0 | 0 | 0 |  | 50.0 | 0 |  |  |  |  |  | disabled channel is skipped | 未执行 |
| 3 | 1 | 13824 | 1 | 100.0 | 0.0 | 0 | 0 | 13824 | 1 | 100.0 | 0.0 | 0 | 0 | 0 |  |  | 50.0 |  |  |  |  | count=1: only the first channel is processed | 未执行 |


## M03 Calculate Moving Average（`M03_MovingAvg`）

- 编译：**未通过**（用例记为未通过）；用例通过 0/5；整题未通过

### TC01 Cyclic moving average with window 3

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Cyclic moving average with window 3 |
| 所属题目 | M03 Calculate Moving Average（`M03_MovingAvg`） |
| 初始状态 | power-up, windowSize=3, cyclicExecution=TRUE |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | average over a partially filled window, window reached, oldest value replaced |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 不支持的函数 REAL（支持类型转换 X_TO_Y、ABS/MIN/MAX/LIMIT/SEL 与 Standard 字符串函数） |

| 周期 | cyclicExecution | trigger | value | windowSize | reset | 预期 average | 预期 windowSizeReached | 预期 error | 预期 status | 实际 average | 实际 windowSizeReached | 实际 error | 实际 status | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 10.0 | 3 | 0 | 10.0 | 0 | 0 | 0 |  |  |  |  | first value: average = 10 | FAIL |
| 1 | 1 | 0 | 20.0 | 3 | 0 | 15.0 | 0 |  |  |  |  |  |  | two values: (10+20)/2 = 15 | 未执行 |
| 2 | 1 | 0 | 30.0 | 3 | 0 | 20.0 | 1 |  |  |  |  |  |  | three values: (10+20+30)/3 = 20, window reached | 未执行 |
| 3 | 1 | 0 | 60.0 | 3 | 0 | 36.666666666666664 | 1 |  |  |  |  |  |  | oldest (10) dropped: (20+30+60)/3 | 未执行 |
| 4 | 1 | 0 | 90.0 | 3 | 0 | 60.0 | 1 |  |  |  |  |  |  | (30+60+90)/3 = 60 | 未执行 |

### TC02 Trigger mode reads only on a rising edge

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Trigger mode reads only on a rising edge |
| 所属题目 | M03 Calculate Moving Average（`M03_MovingAvg`） |
| 初始状态 | power-up, windowSize=2, cyclicExecution=FALSE |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | no read without a trigger, one read per rising edge, held trigger does not read again |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 不支持的函数 REAL（支持类型转换 X_TO_Y、ABS/MIN/MAX/LIMIT/SEL 与 Standard 字符串函数） |

| 周期 | cyclicExecution | trigger | value | windowSize | reset | 预期 average | 预期 windowSizeReached | 实际 average | 实际 windowSizeReached | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 10.0 | 2 | 0 | 0.0 | 0 | 0.0 | 0 | no trigger -> nothing read | PASS |
| 1 | 0 | 1 | 10.0 | 2 | 0 | 10.0 |  |  |  | rising edge -> value read | FAIL |
| 2 | 0 | 1 | 99.0 | 2 | 0 | 10.0 |  |  |  | trigger held -> no new read | 未执行 |
| 3 | 0 | 0 | 99.0 | 2 | 0 | 10.0 |  |  |  | trigger released -> no read | 未执行 |
| 4 | 0 | 1 | 30.0 | 2 | 0 | 20.0 | 1 |  |  | new rising edge -> (10+30)/2 = 20 | 未执行 |

### TC03 cyclicExecution overrides the trigger

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 cyclicExecution overrides the trigger |
| 所属题目 | M03 Calculate Moving Average（`M03_MovingAvg`） |
| 初始状态 | power-up, windowSize=2, cyclicExecution=TRUE |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | with cyclicExecution TRUE a value is read every cycle regardless of the trigger |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 不支持的函数 REAL（支持类型转换 X_TO_Y、ABS/MIN/MAX/LIMIT/SEL 与 Standard 字符串函数） |

| 周期 | cyclicExecution | trigger | value | windowSize | reset | 预期 average | 预期 windowSizeReached | 实际 average | 实际 windowSizeReached | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 4.0 | 2 | 0 | 4.0 |  |  |  | read without a trigger | FAIL |
| 1 | 1 | 0 | 8.0 | 2 | 0 | 6.0 | 1 |  |  | read again: (4+8)/2 = 6 | 未执行 |
| 2 | 1 | 1 | 12.0 | 2 | 0 | 10.0 |  |  |  | trigger has no additional effect: (8+12)/2 = 10 | 未执行 |

### TC04 Reset clears the calculation

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Reset clears the calculation |
| 所属题目 | M03 Calculate Moving Average（`M03_MovingAvg`） |
| 初始状态 | power-up, windowSize=3, cyclicExecution=TRUE |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | reset zeroes the average and the window, new values start from scratch |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 不支持的函数 REAL（支持类型转换 X_TO_Y、ABS/MIN/MAX/LIMIT/SEL 与 Standard 字符串函数） |

| 周期 | cyclicExecution | trigger | value | windowSize | reset | 预期 average | 预期 windowSizeReached | 预期 error | 实际 average | 实际 windowSizeReached | 实际 error | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 10.0 | 3 | 0 | 10.0 |  |  |  |  |  | first value | FAIL |
| 1 | 1 | 0 | 20.0 | 3 | 0 | 15.0 |  |  |  |  |  | second | 未执行 |
| 2 | 1 | 0 | 30.0 | 3 | 0 | 20.0 | 1 |  |  |  |  | window reached | 未执行 |
| 3 | 1 | 0 | 99.0 | 3 | 1 | 0.0 | 0 | 0 |  |  |  | reset -> average 0, window not reached | 未执行 |
| 4 | 1 | 0 | 50.0 | 3 | 0 | 50.0 | 0 |  |  |  |  | restart: only the new value counts | 未执行 |

### TC05 Window-size errors

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC05 Window-size errors |
| 所属题目 | M03 Calculate Moving Average（`M03_MovingAvg`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | windowSize 0 and 101 produce 16#8200, boundaries 1 and 100 are valid, recovery after a valid size |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 不支持的函数 REAL（支持类型转换 X_TO_Y、ABS/MIN/MAX/LIMIT/SEL 与 Standard 字符串函数） |

| 周期 | cyclicExecution | trigger | value | windowSize | reset | 预期 error | 预期 status | 预期 average | 预期 windowSizeReached | 实际 error | 实际 status | 实际 average | 实际 windowSizeReached | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 10.0 | 0 | 0 | 1 | 33280 |  |  | 1 | 33280 |  |  | windowSize 0 -> error 16#8200 | PASS |
| 1 | 1 | 0 | 10.0 | 101 | 0 | 1 | 33280 |  |  | 1 | 33280 |  |  | windowSize 101 -> error | PASS |
| 2 | 1 | 0 | 10.0 | -5 | 0 | 1 | 33280 |  |  | 1 | 33280 |  |  | negative window -> error | PASS |
| 3 | 1 | 0 | 10.0 | 1 | 0 | 0 | 0 | 10.0 | 1 |  |  |  |  | windowSize 1 is valid, average = value | FAIL |
| 4 | 1 | 0 | 20.0 | 1 | 0 | 0 |  | 20.0 | 1 |  |  |  |  | window 1: average follows the latest value | 未执行 |
| 5 | 1 | 0 | 20.0 | 100 | 0 | 0 | 0 |  |  |  |  |  |  | windowSize 100 is valid | 未执行 |


## M04 Temperature Logic Control（`M04_TempCtrl`）

- 编译：通过；用例通过 3/4；整题未通过

### TC01 Basic heating control and status display

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Basic heating control and status display |
| 所属题目 | M04 Temperature Logic Control（`M04_TempCtrl`） |
| 初始状态 | power-up, all outputs OFF |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | heater on below setpoint, off above, display mirrors inputs |
| 实际输出及结果 | ✅ 通过 |

| 周期 | TemperatureSensorInput | SetTemperature | 预期 HeaterOutput | 预期 HeaterStatus | 预期 OverheatProtection | 预期 CurrentTemperature | 预期 SetTempDisplay | 实际 HeaterOutput | 实际 HeaterStatus | 实际 OverheatProtection | 实际 CurrentTemperature | 实际 SetTempDisplay | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 25.0 | 30.0 | 1 | 1 | 0 | 25.0 | 30.0 | 1 | 1 | 0 | 25.0 | 30.0 | below setpoint -> heater on, displays mirror inputs | PASS |
| 1 | 29.9 | 30.0 | 1 | 1 |  | 29.9 |  | 1 | 1 |  | 29.9 |  | still below -> heating | PASS |
| 2 | 35.0 | 30.0 | 0 | 0 |  | 35.0 |  | 0 | 0 |  | 35.0 |  | above setpoint -> heater off | PASS |
| 3 | 30.0 | 30.0 | 0 | 0 |  |  |  | 0 | 0 |  |  |  | equal to setpoint -> not below -> heater off | PASS |
| 4 | 20.0 | 50.0 | 1 | 1 |  |  | 50.0 | 1 | 1 |  |  | 50.0 | new setpoint, below -> heating | PASS |

### TC02 Overheat protection after 5 s of continuous heating

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Overheat protection after 5 s of continuous heating |
| 所属题目 | M04 Temperature Logic Control（`M04_TempCtrl`） |
| 初始状态 | power-up, temperature 20, setpoint 80 (heater stays demanded) |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | protection trips at 5s, heater forced off, protection held for 3s, released afterwards |
| 实际输出及结果 | ❌ 不通过；周期 2：HeaterOutput 预期 0，实际 True；HeaterStatus 预期 0，实际 True；OverheatProtection 预期 1，实际 False；周期 3：HeaterOutput 预期 0，实际 True；HeaterStatus 预期 0，实际 True；OverheatProtection 预期 1，实际 False；周期 4：HeaterOutput 预期 0，实际 True；HeaterStatus 预期 0，实际 True；OverheatProtection 预期 1，实际 False |

| 周期 | TemperatureSensorInput | SetTemperature | 预期 HeaterOutput | 预期 HeaterStatus | 预期 OverheatProtection | 实际 HeaterOutput | 实际 HeaterStatus | 实际 OverheatProtection | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0（保持 3000 ms） | 20.0 | 80.0 | 1 | 1 | 0 | 1 | 1 | 0 | heating starts | PASS |
| 1（保持 1900 ms） | 20.0 | 80.0 | 1 | 1 | 0 | 1 | 1 | 0 | 3s of continuous heating: no protection yet | PASS |
| 2（保持 200 ms） | 20.0 | 80.0 | 0 | 0 | 1 | 1 | 1 | 0 | 5s reached -> protection trips, heater off | FAIL |
| 3（保持 2000 ms） | 20.0 | 80.0 | 0 | 0 | 1 | 1 | 1 | 0 | protection held, heater stays off although demand persists | FAIL |
| 4（保持 700 ms） | 20.0 | 80.0 | 0 | 0 | 1 | 1 | 1 | 0 | 2.9 s of the 3 s wait: protection still active | FAIL |
| 5（保持 200 ms） | 20.0 | 80.0 |  |  | 0 |  |  | 0 | 3 s elapsed -> protection lifted (heater restarts in the next cycle) | PASS |
| 6 | 20.0 | 80.0 | 1 | 1 | 0 | 1 | 1 | 0 | heating resumes | PASS |

### TC03 Sensor fault turns the heater off

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Sensor fault turns the heater off |
| 所属题目 | M04 Temperature Logic Control（`M04_TempCtrl`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | value < 0 and > 100 are faults, heater off, recovery when the value returns to range |
| 实际输出及结果 | ✅ 通过 |

| 周期 | TemperatureSensorInput | SetTemperature | 预期 HeaterOutput | 预期 HeaterStatus | 实际 HeaterOutput | 实际 HeaterStatus | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|
| 0 | 20.0 | 50.0 | 1 | 1 | 1 | 1 | normal heating | PASS |
| 1 | -0.1 | 50.0 | 0 | 0 | 0 | 0 | value < 0 -> sensor fault, heater off | PASS |
| 2 | 0.0 | 50.0 | 1 | 1 | 1 | 1 | 0 is a valid value -> heating again | PASS |
| 3 | 100.1 | 50.0 | 0 | 0 | 0 | 0 | value > 100 -> sensor fault, heater off | PASS |
| 4 | 100.0 | 50.0 | 0 | 0 | 0 | 0 | 100 is valid but above setpoint -> heater off | PASS |
| 5 | 100.0 | 120.0 | 1 | 1 | 1 | 1 | 100 valid and below setpoint -> heating | PASS |

### TC04 Heating interrupted before 5 s does not trip protection

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Heating interrupted before 5 s does not trip protection |
| 所属题目 | M04 Temperature Logic Control（`M04_TempCtrl`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | the run timer restarts when the heater stops |
| 实际输出及结果 | ✅ 通过 |

| 周期 | TemperatureSensorInput | SetTemperature | 预期 HeaterOutput | 预期 HeaterStatus | 预期 OverheatProtection | 实际 HeaterOutput | 实际 HeaterStatus | 实际 OverheatProtection | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0（保持 3000 ms） | 20.0 | 80.0 | 1 | 1 | 0 | 1 | 1 | 0 | heating | PASS |
| 1 | 90.0 | 80.0 | 0 | 0 | 0 | 0 | 0 | 0 | above setpoint -> heater off before 5s, no protection | PASS |
| 2（保持 3000 ms） | 20.0 | 80.0 | 1 | 1 | 0 | 1 | 1 | 0 | heating again | PASS |
| 3（保持 1000 ms） | 20.0 | 80.0 | 1 | 1 | 0 | 1 | 1 | 0 | 3s of the new heating period: still no protection | PASS |


## M05 Automated Production Line Control（`M05_ProdLine`）

- 编译：通过；用例通过 1/6；整题未通过

### TC01 Manual mode jog with interlock

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Manual mode jog with interlock |
| 所属题目 | M05 Automated Production Line Control（`M05_ProdLine`） |
| 初始状态 | power-up, Mode=0 (manual), all inputs FALSE |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | forward, reverse, both pressed -> both OFF, release -> stop, light OFF in manual |
| 实际输出及结果 | ❌ 不通过；周期 4：MotorForward 预期 0，实际 True；周期 5：MotorReverse 预期 1，实际 False；周期 7：MotorForward 预期 0，实际 True |

| 周期 | Mode | ForwardButton | ReverseButton | SensorA | SensorB | SensorC | ButtonA | ButtonB | ButtonC | 预期 MotorForward | 预期 MotorReverse | 预期 CompletionLight | 实际 MotorForward | 实际 MotorReverse | 实际 CompletionLight | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | idle manual, all OFF | PASS |
| 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | forward button -> forward | PASS |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | released -> stop (jog, no latching) | PASS |
| 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | reverse button -> reverse | PASS |
| 4 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | both pressed -> interlock, both OFF | FAIL |
| 5 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | forward released -> reverse again | FAIL |
| 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | all released -> stop | PASS |
| 7 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | auto-mode signals have no effect in manual | FAIL |

### TC02 Automatic full cycle

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Automatic full cycle |
| 所属题目 | M05 Automated Production Line Control（`M05_ProdLine`） |
| 初始状态 | power-up, Mode=1 (auto), product not yet at A |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | A->B->C sequence, motor stops on arrival, light ON after ButtonC, light OFF when product removed |
| 实际输出及结果 | ❌ 不通过；周期 13：CompletionLight 预期 0，实际 True |

| 周期 | Mode | ForwardButton | ReverseButton | SensorA | SensorB | SensorC | ButtonA | ButtonB | ButtonC | 预期 MotorForward | 预期 MotorReverse | 预期 CompletionLight | 实际 MotorForward | 实际 MotorReverse | 实际 CompletionLight | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | auto idle, nothing moves | PASS |
| 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | product at A, waiting for ButtonA | PASS |
| 2 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |  | 0 | 0 |  | 0 | 0 | ButtonA -> motor forward (trigger cycle) | PASS |
| 3 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | motor starts in the following cycle | PASS |
| 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | product left A, still moving | PASS |
| 5 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | arrived at B -> motor stops | PASS |
| 6 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | waiting for ButtonB | PASS |
| 7 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |  | 0 | 0 |  | 0 | 0 | ButtonB -> motor forward (trigger cycle) | PASS |
| 8 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | motor starts in the following cycle | PASS |
| 9 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | moving B->C | PASS |
| 10 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | arrived at C -> motor stops | PASS |
| 11 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | ButtonC -> completion light ON | PASS |
| 12 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | light stays ON while product present | PASS |
| 13 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | product removed -> light OFF | FAIL |
| 14 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |  | 0 | 0 |  | 0 | 0 | next product can start a new cycle (trigger cycle) | PASS |
| 15 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | motor starts in the following cycle | PASS |

### TC03 Automatic mode ignores wrong signals

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Automatic mode ignores wrong signals |
| 所属题目 | M05 Automated Production Line Control（`M05_ProdLine`） |
| 初始状态 | power-up, Mode=1 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | ButtonA without product, buttons at wrong station, manual buttons in auto, no reverse in auto |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Mode | ForwardButton | ReverseButton | SensorA | SensorB | SensorC | ButtonA | ButtonB | ButtonC | 预期 MotorForward | 预期 MotorReverse | 预期 CompletionLight | 实际 MotorForward | 实际 MotorReverse | 实际 CompletionLight | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ButtonA without product at A -> nothing | PASS |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | manual buttons ignored in auto | PASS |
| 2 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | wrong buttons at A -> nothing | PASS |
| 3 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |  | 0 | 0 |  | 0 | 0 | correct button starts (trigger cycle) | PASS |
| 4 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | motor starts in the following cycle | PASS |
| 5 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | at B | PASS |
| 6 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | wrong buttons at B -> stays stopped | PASS |
| 7 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |  | 0 | 0 |  | 0 | 0 | correct button continues (trigger cycle) | PASS |
| 8 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | motor starts in the following cycle | PASS |
| 9 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | at C, no light before ButtonC | PASS |
| 10 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | wrong buttons at C -> no light | PASS |

### TC04 Mode switch during automatic cycle

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Mode switch during automatic cycle |
| 所属题目 | M05 Automated Production Line Control（`M05_ProdLine`） |
| 初始状态 | power-up, Mode=1 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | switching to manual stops automatic motion; manual jog works; returning to automatic resumes the stored step |
| 实际输出及结果 | ❌ 不通过；周期 3：MotorForward 预期 0，实际 True；周期 4：MotorForward 预期 0，实际 True；周期 5：MotorForward 预期 0，实际 True |

| 周期 | Mode | ForwardButton | ReverseButton | SensorA | SensorB | SensorC | ButtonA | ButtonB | ButtonC | 预期 MotorReverse | 预期 CompletionLight | 预期 MotorForward | 实际 MotorReverse | 实际 CompletionLight | 实际 MotorForward | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |  | 0 | 0 |  | auto start (trigger cycle) | PASS |
| 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | motor starts in the following cycle | PASS |
| 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | moving | PASS |
| 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | switch to manual -> motor stops | FAIL |
| 4 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | manual reverse works | FAIL |
| 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | released | FAIL |
| 6 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | 0 |  |  | back to automatic: the reference implementation keeps its internal step, so the interrupted move resumes (resume-vs-restart is not fixed by the requirement) | PASS |

### TC05 A station button held in advance does not release the carriage

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC05 A station button held in advance does not release the carriage |
| 所属题目 | M05 Automated Production Line Control（`M05_ProdLine`） |
| 初始状态 | auto mode, carriage at A (SensorA), step 0 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | edge-triggered station buttons: ButtonB pressed before station B is reached must not start the next leg; outputs follow a transition one scan later |
| 实际输出及结果 | ❌ 不通过；周期 1：MotorForward 预期 0，实际 True；周期 8：MotorForward 预期 0，实际 True |

| 周期 | Mode | ForwardButton | ReverseButton | SensorA | SensorB | SensorC | ButtonA | ButtonB | ButtonC | 预期 MotorForward | 预期 MotorReverse | 实际 MotorForward | 实际 MotorReverse | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | waiting at A | PASS |
| 1 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |  | 1 |  | ButtonA edge: transition to the travelling step, output next scan | FAIL |
| 2 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 1 |  | 1 |  | travelling to B; ButtonB is pressed early and held from here on | PASS |
| 3 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |  | 1 |  | still travelling, both buttons held | PASS |
| 4 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |  | 0 |  | arrived at B: motor stops | PASS |
| 5 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |  | 0 |  | DECISIVE: ButtonB was already held on arrival, so it has no rising edge and the carriage must stay at B | PASS |
| 6 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |  | 0 |  | still held: still waiting | PASS |
| 7 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  | 0 |  | released, still waiting | PASS |
| 8 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |  | 1 |  | fresh ButtonB edge: transition, output next scan | FAIL |
| 9 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 |  | 1 |  | now travelling to C | PASS |
| 10 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |  | 0 |  | arrived at C | PASS |

### TC06 Station sensors held while the operator works at the station

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC06 Station sensors held while the operator works at the station |
| 所属题目 | M05 Automated Production Line Control（`M05_ProdLine`） |
| 初始状态 | auto mode, carriage at A (SensorA), step 0 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | station sensor held TRUE across the whole processing time: the motor stays stopped, holding the button does not advance, and the carriage leaves only once the operator confirms |
| 实际输出及结果 | ❌ 不通过；周期 2：MotorForward 预期 0，实际 True；周期 7：MotorForward 预期 0，实际 True |

| 周期 | Mode | ForwardButton | ReverseButton | SensorA | SensorB | SensorC | ButtonA | ButtonB | ButtonC | 预期 MotorForward | 实际 MotorForward | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | product at A, waiting | PASS |
| 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | sensor held, no button: still waiting, nothing latches spuriously | PASS |
| 2 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | ButtonA edge: transition taken this cycle | FAIL |
| 3 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | motor now drives the product away, though SensorA is still TRUE. A level implementation that re-checks SensorA would stall here | PASS |
| 4 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | arrives at B: motor stops | PASS |
| 5 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | SensorB held for many cycles: the motor must stay stopped | PASS |
| 6 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | still held, and ButtonA is the wrong button: no movement | PASS |
| 7 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | ButtonB edge: transition to the travelling step | FAIL |
| 8 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | motor runs although SensorB is still TRUE | PASS |
| 9 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | arrives at C: motor stops | PASS |
| 10 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | SensorC held: motor stays stopped until the product is collected | PASS |


## M06 Slab Thickness Alarm and Fault History（`M06_SlabThick`）

- 编译：**未通过**（用例记为未通过）；用例通过 0/5；整题未通过

### TC01 Alarm with 500 ms minimum hold

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Alarm with 500 ms minimum hold |
| 所属题目 | M06 Slab Thickness Alarm and Fault History（`M06_SlabThick`） |
| 初始状态 | power-up: alarm off, counter 0, runtime 0, history zero |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | alarm on at the fault edge, held 500 ms after the fault clears, off afterwards |
| 实际输出及结果 | ❌ 不通过；周期 2：THICKNESS_ALARM 预期 1，实际 False |

| 周期 | THICKNESS_FAULT | THICKNESS_SIGNAL_VALID | CUTTING_RUN | FaultTimestamp | CycleTime | 预期 THICKNESS_ALARM | 预期 Slab_Fault_Counter | 预期 Slab_Runtime_Accumulator | 预期 Slab_Fault_History[0] | 预期 Slab_Fault_History[1] | 预期 Slab_Fault_History[2] | 预期 Slab_Fault_History[3] | 预期 Slab_Fault_History[4] | 实际 THICKNESS_ALARM | 实际 Slab_Fault_Counter | 实际 Slab_Runtime_Accumulator | 实际 Slab_Fault_History[0] | 实际 Slab_Fault_History[1] | 实际 Slab_Fault_History[2] | 实际 Slab_Fault_History[3] | 实际 Slab_Fault_History[4] | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | power-up | PASS |
| 1 | 1 | 1 | 0 | 1000 | 100 | 1 | 1 |  |  |  |  |  |  | 1 | 1 |  |  |  |  |  |  | fault -> alarm, counted | PASS |
| 2（保持 300 ms） | 0 | 1 | 0 | 0 | 100 | 1 |  |  |  |  |  |  |  | 0 |  |  |  |  |  |  |  | fault cleared, still within the 500 ms hold | FAIL |
| 3（保持 400 ms） | 0 | 1 | 0 | 0 | 100 | 0 |  |  |  |  |  |  |  | 0 |  |  |  |  |  |  |  | 500 ms elapsed -> alarm released | PASS |
| 4 | 0 | 1 | 0 | 0 | 100 | 0 | 1 |  |  |  |  |  |  | 0 | 1 |  |  |  |  |  |  | stays off | PASS |

### TC02 Alarm stays active while the fault persists

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Alarm stays active while the fault persists |
| 所属题目 | M06 Slab Thickness Alarm and Fault History（`M06_SlabThick`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | long fault keeps the alarm on, no repeated counting |
| 实际输出及结果 | ❌ 不通过；周期 2：THICKNESS_ALARM 预期 1，实际 False |

| 周期 | THICKNESS_FAULT | THICKNESS_SIGNAL_VALID | CUTTING_RUN | FaultTimestamp | CycleTime | 预期 THICKNESS_ALARM | 预期 Slab_Fault_Counter | 实际 THICKNESS_ALARM | 实际 Slab_Fault_Counter | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 2000 | 100 | 1 | 1 | 1 | 1 | fault | PASS |
| 1（保持 2000 ms） | 1 | 1 | 0 | 0 | 100 | 1 | 1 | 1 | 1 | persists, not counted again | PASS |
| 2（保持 200 ms） | 0 | 1 | 0 | 0 | 100 | 1 |  | 0 |  | cleared, hold starts | FAIL |
| 3（保持 500 ms） | 0 | 1 | 0 | 0 | 100 | 0 |  | 0 |  | released | PASS |

### TC03 Fault counting and history shifting

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Fault counting and history shifting |
| 所属题目 | M06 Slab Thickness Alarm and Fault History（`M06_SlabThick`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | one count per rising edge, newest at index 0, oldest dropped |
| 实际输出及结果 | ❌ 不通过；周期 0：Slab_Fault_History[1] 预期 0，实际 101；周期 2：Slab_Fault_History[1] 预期 101，实际 202；Slab_Fault_History[2] 预期 0，实际 101；周期 3：Slab_Fault_History[1] 预期 101，实际 202 |

| 周期 | THICKNESS_FAULT | THICKNESS_SIGNAL_VALID | CUTTING_RUN | FaultTimestamp | CycleTime | 预期 Slab_Fault_Counter | 预期 Slab_Fault_History[0] | 预期 Slab_Fault_History[1] | 预期 Slab_Fault_History[2] | 预期 Slab_Fault_History[3] | 预期 Slab_Fault_History[4] | 实际 Slab_Fault_Counter | 实际 Slab_Fault_History[0] | 实际 Slab_Fault_History[1] | 实际 Slab_Fault_History[2] | 实际 Slab_Fault_History[3] | 实际 Slab_Fault_History[4] | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 101 | 100 | 1 | 101 | 0 | 0 | 0 | 0 | 1 | 101 | 101 | 0 | 0 | 0 | fault 1 | FAIL |
| 1（保持 600 ms） | 0 | 1 | 0 | 0 | 100 | 1 |  |  |  |  |  | 1 |  |  |  |  |  | cleared | PASS |
| 2 | 1 | 1 | 0 | 202 | 100 | 2 | 202 | 101 | 0 | 0 | 0 | 2 | 202 | 202 | 101 | 0 | 0 | fault 2 | FAIL |
| 3（保持 600 ms） | 0 | 1 | 0 | 0 | 100 | 2 | 202 | 101 |  |  |  | 2 | 202 | 202 |  |  |  | fault cleared: counter and history unchanged (no record without a rising edge) | FAIL |
| 4 | 1 | 1 | 0 | 303 | 100 | 3 | 303 | 202 | 101 | 0 | 0 | 3 | 303 | 303 | 202 | 101 | 0 | fault 3 | FAIL |
| 5（保持 600 ms） | 0 | 1 | 0 | 0 | 100 | 3 | 303 | 202 | 101 |  |  | 3 | 303 | 303 | 202 |  |  | fault cleared: counter and history unchanged (no record without a rising edge) | FAIL |
| 6 | 1 | 1 | 0 | 404 | 100 | 4 | 404 | 303 | 202 | 101 | 0 | 4 | 404 | 404 | 303 | 202 | 101 | fault 4 | FAIL |
| 7（保持 600 ms） | 0 | 1 | 0 | 0 | 100 | 4 | 404 | 303 | 202 | 101 |  | 4 | 404 | 404 | 303 | 202 |  | fault cleared: counter and history unchanged (no record without a rising edge) | FAIL |
| 8 | 1 | 1 | 0 | 505 | 100 | 5 | 505 | 404 | 303 | 202 | 101 | 5 | 505 | 505 | 404 | 303 | 202 | fault 5: history full | FAIL |
| 9（保持 600 ms） | 0 | 1 | 0 | 0 | 100 | 5 | 505 | 404 | 303 | 202 | 101 | 5 | 505 | 505 | 404 | 303 | 202 | fault cleared: counter and history unchanged (no record without a rising edge) | FAIL |
| 10 | 1 | 1 | 0 | 606 | 100 | 6 | 606 | 505 | 404 | 303 | 202 | 6 | 606 | 606 | 505 | 404 | 303 | fault 6: oldest dropped | FAIL |

### TC04 Runtime accumulates only during normal cutting

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Runtime accumulates only during normal cutting |
| 所属题目 | M06 Slab Thickness Alarm and Fault History（`M06_SlabThick`） |
| 初始状态 | power-up; CycleTime=1000 ms |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | accumulates when running and fault-free, preserved otherwise |
| 实际输出及结果 | ❌ 不通过；周期 5：Slab_Runtime_Accumulator 预期 3000，实际 0；周期 6：Slab_Runtime_Accumulator 预期 4000，实际 1000 |

| 周期 | THICKNESS_FAULT | THICKNESS_SIGNAL_VALID | CUTTING_RUN | FaultTimestamp | CycleTime | 预期 Slab_Runtime_Accumulator | 实际 Slab_Runtime_Accumulator | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 0 | 1000 | 1000 | 1000 | cutting | PASS |
| 1 | 0 | 1 | 1 | 0 | 1000 | 2000 | 2000 | accumulates | PASS |
| 2 | 0 | 1 | 0 | 0 | 1000 | 2000 | 2000 | stopped -> preserved | PASS |
| 3 | 1 | 1 | 1 | 10 | 1000 | 2000 | 2000 | fault -> not accumulated | PASS |
| 4 | 0 | 1 | 1 | 0 | 1000 | 3000 | 3000 | fault cleared -> accumulates | PASS |
| 5 | 0 | 0 | 1 | 0 | 1000 | 3000 | 0 | invalid signal -> not accumulated | FAIL |
| 6 | 0 | 1 | 1 | 0 | 1000 | 4000 | 1000 | valid again | FAIL |

### TC05 Invalid signal clears the alarm and blocks recording

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC05 Invalid signal clears the alarm and blocks recording |
| 所属题目 | M06 Slab Thickness Alarm and Fault History（`M06_SlabThick`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | alarm off while invalid, nothing counted or recorded |
| 实际输出及结果 | ❌ 不通过；周期 0：Slab_Fault_History[1] 预期 0，实际 11；周期 1：Slab_Fault_Counter 预期 1，实际 0；周期 2：Slab_Fault_Counter 预期 1，实际 0；Slab_Fault_History[0] 预期 11，实际 0 |

| 周期 | THICKNESS_FAULT | THICKNESS_SIGNAL_VALID | CUTTING_RUN | FaultTimestamp | CycleTime | 预期 THICKNESS_ALARM | 预期 Slab_Fault_Counter | 预期 Slab_Fault_History[0] | 预期 Slab_Fault_History[1] | 预期 Slab_Fault_History[2] | 预期 Slab_Fault_History[3] | 预期 Slab_Fault_History[4] | 实际 THICKNESS_ALARM | 实际 Slab_Fault_Counter | 实际 Slab_Fault_History[0] | 实际 Slab_Fault_History[1] | 实际 Slab_Fault_History[2] | 实际 Slab_Fault_History[3] | 实际 Slab_Fault_History[4] | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 11 | 100 | 1 | 1 | 11 | 0 | 0 | 0 | 0 | 1 | 1 | 11 | 11 | 0 | 0 | 0 | fault recorded | FAIL |
| 1 | 1 | 0 | 0 | 0 | 100 | 0 | 1 |  |  |  |  |  | 0 | 0 |  |  |  |  |  | invalid -> alarm off | FAIL |
| 2 | 1 | 0 | 0 | 22 | 100 |  | 1 | 11 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 | 0 | 0 | still invalid: not counted | FAIL |
| 3 | 0 | 0 | 0 | 0 | 100 | 0 |  |  |  |  |  |  | 0 |  |  |  |  |  |  | still invalid | PASS |
| 4 | 0 | 1 | 0 | 0 | 100 |  | 1 |  |  |  |  |  |  | 0 |  |  |  |  |  | valid again with no fault: nothing counted (alarm hold state is implementation-defined) | FAIL |


## M07 Office HVAC Multi-mode Energy-Saving Control（`M07_HVAC`）

- 编译：**未通过**（用例记为未通过）；用例通过 0/3；整题未通过

- 仿真器无法执行：期望 ':='，实际是 'IF'

### TC01 30-second fan start delay

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 30-second fan start delay |
| 所属题目 | M07 Office HVAC Multi-mode Energy-Saving Control（`M07_HVAC`） |
| 初始状态 | power-up: fan OFF, adjustment 0. Auto mode |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | power-up state, no run before 30s, run after 30s, stop on occupancy loss, full delay again |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'IF' |

| 周期 | OCCUPANCY_DETECTED | ENERGY_SAVING_MODE | HVAC_MODE_SELECTOR | 预期 SUPPLY_FAN_RUN | 预期 TEMP_SETPOINT_ADJUST | 实际 SUPPLY_FAN_RUN | 实际 TEMP_SETPOINT_ADJUST | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 2 |  |  | power-up, unoccupied auto standard -> +2 | FAIL |
| 1（保持 20000 ms） | 1 | 0 | 0 | 0 | 0 |  |  | occupancy -> delay starts, adjustment immediately 0 | 未执行 |
| 2（保持 9900 ms） | 1 | 0 | 0 | 0 |  |  |  | 20s: still waiting | 未执行 |
| 3（保持 200 ms） | 1 | 0 | 0 | 1 |  |  |  | 30s reached -> fan runs | 未执行 |
| 4 | 0 | 0 | 0 | 0 | 2 |  |  | occupancy lost -> fan stops immediately | 未执行 |
| 5（保持 20000 ms） | 1 | 0 | 0 | 0 |  |  |  | new occupancy: 20s is not enough | 未执行 |
| 6（保持 10200 ms） | 1 | 0 | 0 | 1 |  |  |  | full 30s -> fan runs again | 未执行 |

### TC02 Night mode blocks the fan

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Night mode blocks the fan |
| 所属题目 | M07 Office HVAC Multi-mode Energy-Saving Control（`M07_HVAC`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | night mode stops the fan and resets timing regardless of occupancy |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'IF' |

| 周期 | OCCUPANCY_DETECTED | ENERGY_SAVING_MODE | HVAC_MODE_SELECTOR | 预期 SUPPLY_FAN_RUN | 预期 TEMP_SETPOINT_ADJUST | 实际 SUPPLY_FAN_RUN | 实际 TEMP_SETPOINT_ADJUST | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|
| 0（保持 30200 ms） | 1 | 0 | 0 | 1 | 0 |  |  | auto occupied, fan running | FAIL |
| 1 | 1 | 0 | 3 | 0 | 4 |  |  | night mode -> fan stops immediately, +4 | 未执行 |
| 2（保持 31000 ms） | 1 | 0 | 3 | 0 | 4 |  |  | night mode: fan stays off even when occupied | 未执行 |
| 3 | 0 | 0 | 3 | 0 | 4 |  |  | night mode unoccupied -> still +4 | 未执行 |
| 4 | 1 | 0 | 0 | 0 | 0 |  |  | back to auto: full 30s required again | 未执行 |
| 5（保持 30200 ms） | 1 | 0 | 0 | 1 |  |  |  | 30s -> fan runs | 未执行 |

### TC03 Setpoint adjustment per mode

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Setpoint adjustment per mode |
| 所属题目 | M07 Office HVAC Multi-mode Energy-Saving Control（`M07_HVAC`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | all four modes, occupied and unoccupied, energy-saving affects Auto only, range within +-4 |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'IF' |

| 周期 | OCCUPANCY_DETECTED | ENERGY_SAVING_MODE | HVAC_MODE_SELECTOR | 预期 TEMP_SETPOINT_ADJUST | 实际 TEMP_SETPOINT_ADJUST | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 |  | auto occupied -> 0 | FAIL |
| 1 | 0 | 0 | 0 | 2 |  | auto unoccupied standard -> +2 | 未执行 |
| 2 | 0 | 1 | 0 | 3 |  | auto unoccupied energy-saving -> +3 | 未执行 |
| 3 | 1 | 0 | 1 | 0 |  | comfort occupied -> 0 | 未执行 |
| 4 | 0 | 0 | 1 | 1 |  | comfort unoccupied -> +1 | 未执行 |
| 5 | 0 | 1 | 1 | 1 |  | energy-saving does not affect comfort -> +1 | 未执行 |
| 6 | 1 | 0 | 2 | 0 |  | economy occupied -> 0 | 未执行 |
| 7 | 0 | 0 | 2 | 4 |  | economy unoccupied -> +4 | 未执行 |
| 8 | 0 | 1 | 2 | 4 |  | energy-saving does not affect economy -> +4 | 未执行 |
| 9 | 1 | 0 | 3 | 4 |  | night occupied -> +4 | 未执行 |
| 10 | 0 | 1 | 3 | 4 |  | night unoccupied energy-saving -> +4 | 未执行 |


## M08 IPv4 Parsing with Format and Range Checks（`M08_IPv4`）

- 编译：**未通过**（用例记为未通过）；用例通过 0/4；整题未通过

- 仿真器无法执行：TypeError: '>=' not supported between instances of 'int' and 'str'

### TC01 Valid addresses in network byte order

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Valid addresses in network byte order |
| 所属题目 | M08 IPv4 Parsing with Format and Range Checks（`M08_IPv4`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | typical address, first segment in the most significant byte, single digits, maximum segments |
| 实际输出及结果 | ⚠️ 未执行 |

| 周期 | ipText | 预期 ipValue | 实际 ipValue | 检查内容 | 结果 |
|---|---|---|---|---|---|
| 0 | 192.168.1.1 | 3232235777 |  | typical address | 未执行 |
| 1 | 1.2.3.4 | 16909060 |  | single digits, byte order check | 未执行 |
| 2 | 255.255.255.255 | 4294967295 |  | all maximum segments | 未执行 |
| 3 | 10.0.0.255 | 167772415 |  | zeros in the middle | 未执行 |
| 4 | 127.0.0.1 | 2130706433 |  | loopback | 未执行 |

### TC02 Zero address and leading zeros

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Zero address and leading zeros |
| 所属题目 | M08 IPv4 Parsing with Format and Range Checks（`M08_IPv4`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | 0.0.0.0 produces 0, leading zeros accepted as decimal |
| 实际输出及结果 | ⚠️ 未执行 |

| 周期 | ipText | 预期 ipValue | 实际 ipValue | 检查内容 | 结果 |
|---|---|---|---|---|---|
| 0 | 0.0.0.0 | 0 |  | valid address 0.0.0.0 also produces 0 | 未执行 |
| 1 | 0.0.0.1 | 1 |  | smallest non-zero address | 未执行 |
| 2 | 010.001.000.009 | 167837705 |  | leading zeros are still decimal | 未执行 |

### TC03 Out-of-range segments

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Out-of-range segments |
| 所属题目 | M08 IPv4 Parsing with Format and Range Checks（`M08_IPv4`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | 256, 999, and a value just above the limit are rejected |
| 实际输出及结果 | ⚠️ 未执行 |

| 周期 | ipText | 预期 ipValue | 实际 ipValue | 检查内容 | 结果 |
|---|---|---|---|---|---|
| 0 | 256.1.1.1 | 0 |  | first segment 256 > 255 | 未执行 |
| 1 | 1.256.1.1 | 0 |  | second segment out of range | 未执行 |
| 2 | 1.1.1.256 | 0 |  | last segment out of range | 未执行 |
| 3 | 999.999.999.999 | 0 |  | all segments out of range | 未执行 |
| 4 | 255.255.255.255 | 4294967295 |  | 255 is still accepted | 未执行 |

### TC04 Malformed input

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Malformed input |
| 所属题目 | M08 IPv4 Parsing with Format and Range Checks（`M08_IPv4`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | wrong segment count, empty segments, non-digit characters, empty string |
| 实际输出及结果 | ⚠️ 未执行 |

| 周期 | ipText | 预期 ipValue | 实际 ipValue | 检查内容 | 结果 |
|---|---|---|---|---|---|
| 0 | 1.2.3 | 0 |  | only three segments | 未执行 |
| 1 | 1.2.3.4.5 | 0 |  | five segments | 未执行 |
| 2 | 1.2..4 | 0 |  | empty segment | 未执行 |
| 3 | .1.2.3 | 0 |  | leading period | 未执行 |
| 4 | 1.2.3. | 0 |  | trailing period | 未执行 |
| 5 | 1.2.3.a | 0 |  | non-digit character | 未执行 |
| 6 | 192,168,1,1 | 0 |  | wrong separator | 未执行 |
| 7 |  | 0 |  | empty string | 未执行 |
| 8 | 1234 | 0 |  | no separators at all | 未执行 |
| 9 | 1.2.3.4  | 0 |  | trailing space is not a digit | 未执行 |


## H01 Material Proportioning Process Control（`H01_Proportion`）

- 编译：通过；用例通过 1/6；整题未通过

### TC01 Manual mode: toggle on rising edge

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Manual mode: toggle on rising edge |
| 所属题目 | H01 Material Proportioning Process Control（`H01_Proportion`） |
| 初始状态 | power-up, estop=1 (not triggered), opeMode=0 (manual), all buttons released |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | each device toggles ON on a rising edge, holding the button does not re-toggle, second press turns OFF, devices independent |
| 实际输出及结果 | ✅ 通过 |

| 周期 | estop | opeMode | valveAStart | valveBStart | valveCStart | valveDStart | mixMotorStart | autoStart | processMode | levelSensor | mixMotorComplete | 预期 valveARun | 预期 valveBRun | 预期 valveCRun | 预期 valveDRun | 预期 mixMotorRun | 实际 valveARun | 实际 valveBRun | 实际 valveCRun | 实际 valveDRun | 实际 mixMotorRun | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | all OFF | PASS |
| 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | rising edge of valveAStart -> A ON | PASS |
| 2 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | button held -> no re-toggle, A stays ON | PASS |
| 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | button released -> A stays ON | PASS |
| 4 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | B and mixer toggled ON, A unaffected | PASS |
| 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | hold | PASS |
| 6 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | second press -> A OFF | PASS |
| 7 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | C and D ON | PASS |
| 8 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | buttons released, all stay | PASS |
| 9 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | second press on all -> all OFF | PASS |
| 10 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 100 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | auto inputs have no effect in manual | PASS |

### TC02 Automatic mode, processMode=FALSE (A -> B -> mix -> D)

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Automatic mode, processMode=FALSE (A -> B -> mix -> D) |
| 所属题目 | H01 Material Proportioning Process Control（`H01_Proportion`） |
| 初始状态 | power-up, estop=1, opeMode=1, processMode=0, levelSensor=0 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | autoStart opens A, level 50 switches to B, level 80 closes B and starts mixer (C skipped), mixComplete stops mixer and opens D |
| 实际输出及结果 | ❌ 不通过；周期 4：valveARun 预期 0，实际 True；valveBRun 预期 1，实际 False；周期 6：valveBRun 预期 0，实际 True；mixMotorRun 预期 1，实际 False；周期 7：mixMotorRun 预期 1，实际 False |

| 周期 | estop | opeMode | valveAStart | valveBStart | valveCStart | valveDStart | mixMotorStart | autoStart | processMode | levelSensor | mixMotorComplete | 预期 valveARun | 预期 valveBRun | 预期 valveCRun | 预期 valveDRun | 预期 mixMotorRun | 实际 valveARun | 实际 valveBRun | 实际 valveCRun | 实际 valveDRun | 实际 mixMotorRun | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | auto idle, nothing runs | PASS |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | autoStart -> valve A opens | PASS |
| 2 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 20 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | filling, A stays open after button released | PASS |
| 3 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 49 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | just below 50 -> A still open | PASS |
| 4 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 50 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | level 50 -> A closes, B opens | FAIL |
| 5 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 65 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | filling B | PASS |
| 6 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 80 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | level 80 -> B closes; processMode=0 -> mixer starts, C not opened | FAIL |
| 7 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 80 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | mixing | FAIL |
| 8 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 80 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | mix complete -> mixer OFF, valve D opens, process ends | FAIL |

### TC03 Automatic mode, processMode=TRUE (A -> B -> C -> mix -> D)

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Automatic mode, processMode=TRUE (A -> B -> C -> mix -> D) |
| 所属题目 | H01 Material Proportioning Process Control（`H01_Proportion`） |
| 初始状态 | power-up, estop=1, opeMode=1, processMode=1, levelSensor=0 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | third material through C until level 100, then mixer and D |
| 实际输出及结果 | ❌ 不通过；周期 1：valveARun 预期 0，实际 True；valveBRun 预期 1，实际 False；周期 2：valveBRun 预期 0，实际 True；valveCRun 预期 1，实际 False；周期 4：valveCRun 预期 0，实际 True；mixMotorRun 预期 1，实际 False |

| 周期 | estop | opeMode | valveAStart | valveBStart | valveCStart | valveDStart | mixMotorStart | autoStart | processMode | levelSensor | mixMotorComplete | 预期 valveARun | 预期 valveBRun | 预期 valveCRun | 预期 valveDRun | 预期 mixMotorRun | 实际 valveARun | 实际 valveBRun | 实际 valveCRun | 实际 valveDRun | 实际 mixMotorRun | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | autoStart -> A | PASS |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 50 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 50 -> B | FAIL |
| 2 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 80 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 80 -> B closes, processMode=1 -> C opens, mixer not yet | FAIL |
| 3 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 99 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | below 100 -> C still open | PASS |
| 4 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 100 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 100 -> C closes, mixer starts | FAIL |
| 5 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 100 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | mix complete -> mixer OFF, D opens | FAIL |

### TC04 Emergency stop in automatic mode

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Emergency stop in automatic mode |
| 所属题目 | H01 Material Proportioning Process Control（`H01_Proportion`） |
| 初始状态 | power-up, estop=1, opeMode=1 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | estop=0 stops everything immediately, outputs stay OFF while estop is held, sequence does not resume by itself after release, new autoStart restarts from A |
| 实际输出及结果 | ❌ 不通过；周期 1：valveARun 预期 0，实际 True；valveBRun 预期 1，实际 False；周期 2：valveBRun 预期 0，实际 True；mixMotorRun 预期 1，实际 False |

| 周期 | estop | opeMode | valveAStart | valveBStart | valveCStart | valveDStart | mixMotorStart | autoStart | processMode | levelSensor | mixMotorComplete | 预期 valveARun | 预期 valveBRun | 预期 valveCRun | 预期 valveDRun | 预期 mixMotorRun | 实际 valveARun | 实际 valveBRun | 实际 valveCRun | 实际 valveDRun | 实际 mixMotorRun | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | start | PASS |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 50 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | B phase | FAIL |
| 2 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 80 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | mixer running | FAIL |
| 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 80 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ESTOP -> all OFF immediately | PASS |
| 4 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 80 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | while estop held, nothing can start | PASS |
| 5 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 80 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | estop released -> stays OFF, no automatic resume | PASS |
| 6 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | new autoStart restarts from valve A | PASS |

### TC05 Emergency stop in manual mode

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC05 Emergency stop in manual mode |
| 所属题目 | H01 Material Proportioning Process Control（`H01_Proportion`） |
| 初始状态 | power-up, estop=1, opeMode=0 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | running devices are stopped by estop, buttons ignored during estop, after release devices stay OFF until toggled again |
| 实际输出及结果 | ❌ 不通过；周期 4：valveARun 预期 0，实际 True；mixMotorRun 预期 0，实际 True；周期 5：valveARun 预期 1，实际 False；mixMotorRun 预期 0，实际 True |

| 周期 | estop | opeMode | valveAStart | valveBStart | valveCStart | valveDStart | mixMotorStart | autoStart | processMode | levelSensor | mixMotorComplete | 预期 valveARun | 预期 valveBRun | 预期 valveCRun | 预期 valveDRun | 预期 mixMotorRun | 实际 valveARun | 实际 valveBRun | 实际 valveCRun | 实际 valveDRun | 实际 mixMotorRun | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | A and mixer ON | PASS |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | hold | PASS |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ESTOP -> all OFF | PASS |
| 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | button during estop ignored | PASS |
| 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | estop released -> all remain OFF | FAIL |
| 5 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | toggle works again after release | FAIL |

### TC06 Automatic mode ignores manual buttons; autoStart only starts when idle

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC06 Automatic mode ignores manual buttons; autoStart only starts when idle |
| 所属题目 | H01 Material Proportioning Process Control（`H01_Proportion`） |
| 初始状态 | power-up, estop=1, opeMode=1 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | manual buttons have no effect in auto, pressing autoStart during a running sequence does not restart it |
| 实际输出及结果 | ❌ 不通过；周期 2：valveARun 预期 0，实际 True；valveBRun 预期 1，实际 False；周期 3：valveARun 预期 0，实际 True；valveBRun 预期 1，实际 False |

| 周期 | estop | opeMode | valveAStart | valveBStart | valveCStart | valveDStart | mixMotorStart | autoStart | processMode | levelSensor | mixMotorComplete | 预期 valveARun | 预期 valveBRun | 预期 valveCRun | 预期 valveDRun | 预期 mixMotorRun | 实际 valveARun | 实际 valveBRun | 实际 valveCRun | 实际 valveDRun | 实际 mixMotorRun | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | manual buttons ignored in auto | PASS |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | start | PASS |
| 2 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 50 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | B phase | FAIL |
| 3 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 60 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | autoStart during sequence -> no restart, still B | FAIL |
| 4 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 60 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | manual C button ignored | PASS |


## H02 Flexible Processing Control（`H02_FlexProcess`）

- 编译：通过；用例通过 1/3；整题未通过

### TC01 Simple route 1 -> 3 -> 5

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Simple route 1 -> 3 -> 5 |
| 所属题目 | H02 Flexible Processing Control（`H02_FlexProcess`） |
| 初始状态 | power-up, material at station 1, processSequence = [3,5], processLength = 2 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | start at station 1, move right to the first processing station, continue after completion, stop at station 5 |
| 实际输出及结果 | ✅ 通过 |

| 周期 | processLength | processSequence[1] | processSequence[2] | processSequence[3] | processSequence[4] | processSequence[5] | processSequence[6] | processSequence[7] | processSequence[8] | sensor1 | sensor2 | sensor3 | sensor4 | sensor5 | station1Start | station2Complete | station3Complete | station4Complete | 预期 conveyorLeft | 预期 conveyorRight | 实际 conveyorLeft | 实际 conveyorRight | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 2 | 3 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | material at station 1, start not pressed -> conveyor stopped | PASS |
| 1 | 2 | 3 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | start pressed -> move right toward station 3 | PASS |
| 2 | 2 | 3 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | in transit | PASS |
| 3 | 2 | 3 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | arrived at station 3 -> conveyor stops | PASS |
| 4 | 2 | 3 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | processing, no completion signal yet | PASS |
| 5 | 2 | 3 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | station 3 complete -> move right toward station 5 | PASS |
| 6 | 2 | 3 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | in transit | PASS |
| 7 | 2 | 3 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | arrived at station 5 -> stop, production finished | PASS |

### TC02 Route requiring a leftward move 1 -> 4 -> 2 -> 5

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Route requiring a leftward move 1 -> 4 -> 2 -> 5 |
| 所属题目 | H02 Flexible Processing Control（`H02_FlexProcess`） |
| 初始状态 | power-up, material at station 1, processSequence = [4,2,5], processLength = 3 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | direction decided from the current and next station numbers, left movement |
| 实际输出及结果 | ❌ 不通过；周期 2：conveyorLeft 预期 1，实际 False；conveyorRight 预期 0，实际 True；周期 3：conveyorLeft 预期 1，实际 False；conveyorRight 预期 0，实际 True |

| 周期 | processLength | processSequence[1] | processSequence[2] | processSequence[3] | processSequence[4] | processSequence[5] | processSequence[6] | processSequence[7] | processSequence[8] | sensor1 | sensor2 | sensor3 | sensor4 | sensor5 | station1Start | station2Complete | station3Complete | station4Complete | 预期 conveyorLeft | 预期 conveyorRight | 实际 conveyorLeft | 实际 conveyorRight | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 3 | 4 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | start -> right toward station 4 | PASS |
| 1 | 3 | 4 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | arrived at station 4 | PASS |
| 2 | 3 | 4 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | station 4 complete, next is station 2 -> move LEFT | FAIL |
| 3 | 3 | 4 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | in transit leftwards | FAIL |
| 4 | 3 | 4 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | arrived at station 2 -> stop | PASS |
| 5 | 3 | 4 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | station 2 complete, next is station 5 -> move right | PASS |
| 6 | 3 | 4 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | arrived at station 5 -> stop | PASS |

### TC03 Wrong signals are ignored

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Wrong signals are ignored |
| 所属题目 | H02 Flexible Processing Control（`H02_FlexProcess`） |
| 初始状态 | power-up, processSequence = [2,5], processLength = 2 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | completion signal from a station the product is not at, start without material, conveyor never runs in both directions |
| 实际输出及结果 | ❌ 不通过；周期 0：conveyorRight 预期 0，实际 True；周期 5：conveyorRight 预期 1，实际 False |

| 周期 | processLength | processSequence[1] | processSequence[2] | processSequence[3] | processSequence[4] | processSequence[5] | processSequence[6] | processSequence[7] | processSequence[8] | sensor1 | sensor2 | sensor3 | sensor4 | sensor5 | station1Start | station2Complete | station3Complete | station4Complete | 预期 conveyorLeft | 预期 conveyorRight | 实际 conveyorLeft | 实际 conveyorRight | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 2 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | start without material at station 1 -> nothing | FAIL |
| 1 | 2 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | completion signals before the product arrives are ignored | PASS |
| 2 | 2 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | correct start -> move right | PASS |
| 3 | 2 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | arrived at station 2 | PASS |
| 4 | 2 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | completion from stations 3/4 ignored at station 2 | PASS |
| 5 | 2 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | correct completion -> move right to station 5 | FAIL |


## H03 Recipe Management System（`H03_RecipeMgr`）

- 编译：通过；用例通过 3/3；整题通过

### TC01 Add recipes and reject duplicates

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Add recipes and reject duplicates |
| 所属题目 | H03 Recipe Management System（`H03_RecipeMgr`） |
| 初始状态 | power-up, empty database (all recipeID = 0) |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | add into the lowest free slot, duplicate ID -> 16#8002 |
| 实际输出及结果 | ✅ 通过 |

| 周期 | addRecipe | deleteRecipe | modifyRecipe | queryRecipe | recipeIn.recipeID | recipeIn.ingredientType | recipeIn.ingredientRatio | recipeIn.productionTemperature | 预期 recipeAdded | 预期 error | 预期 status | 实际 recipeAdded | 实际 error | 实际 status | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 101 | 1 | 0.5 | 180.0 | 1 | 0 | 0 | 1 | 0 | 0 | first recipe added | PASS |
| 1 | 0 | 0 | 0 | 0 | 101 | 1 | 0.5 | 180.0 |  | 0 | 0 |  | 0 | 0 | request released | PASS |
| 2 | 1 | 0 | 0 | 0 | 102 | 2 | 0.3 | 200.0 | 1 | 0 | 0 | 1 | 0 | 0 | second recipe added | PASS |
| 3 | 0 | 0 | 0 | 0 | 102 | 2 | 0.3 | 200.0 |  | 0 | 0 |  | 0 | 0 | released | PASS |
| 4 | 1 | 0 | 0 | 0 | 101 | 9 | 0.9 | 90.0 |  | 1 | 32770 |  | 1 | 32770 | duplicate recipe number -> 16#8002 | PASS |

### TC02 Query existing and missing recipes

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Query existing and missing recipes |
| 所属题目 | H03 Recipe Management System（`H03_RecipeMgr`） |
| 初始状态 | database contains 101 and 102 from TC01-like preparation |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | query returns all fields, missing ID -> 16#8001 |
| 实际输出及结果 | ✅ 通过 |

| 周期 | addRecipe | deleteRecipe | modifyRecipe | queryRecipe | recipeIn.recipeID | recipeIn.ingredientType | recipeIn.ingredientRatio | recipeIn.productionTemperature | 预期 recipeAdded | 预期 error | 预期 status | 预期 recipeQueryResult.recipeID | 预期 recipeQueryResult.ingredientType | 预期 recipeQueryResult.ingredientRatio | 预期 recipeQueryResult.productionTemperature | 实际 recipeAdded | 实际 error | 实际 status | 实际 recipeQueryResult.recipeID | 实际 recipeQueryResult.ingredientType | 实际 recipeQueryResult.ingredientRatio | 实际 recipeQueryResult.productionTemperature | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 101 | 1 | 0.5 | 180.0 | 1 |  |  |  |  |  |  | 1 |  |  |  |  |  |  | prepare: add 101 | PASS |
| 1 | 0 | 0 | 0 | 0 | 101 | 1 | 0.5 | 180.0 |  | 0 | 0 |  |  |  |  |  | 0 | 0 |  |  |  |  | released | PASS |
| 2 | 0 | 0 | 0 | 1 | 101 | 0 | 0.0 | 0.0 |  | 0 | 0 | 101 | 1 | 0.5 | 180.0 |  | 0 | 0 | 101 | 1 | 0.5 | 180.0 | query 101 returns the stored recipe | PASS |
| 3 | 0 | 0 | 0 | 0 | 101 | 0 | 0.0 | 0.0 |  | 0 | 0 |  |  |  |  |  | 0 | 0 |  |  |  |  | released | PASS |
| 4 | 0 | 0 | 0 | 1 | 999 | 0 | 0.0 | 0.0 |  | 1 | 32769 |  |  |  |  |  | 1 | 32769 |  |  |  |  | query a missing number -> 16#8001 | PASS |

### TC03 Modify and delete

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Modify and delete |
| 所属题目 | H03 Recipe Management System（`H03_RecipeMgr`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | modify replaces the stored recipe, delete clears the slot, errors 16#8005 and 16#8004 for missing numbers |
| 实际输出及结果 | ✅ 通过 |

| 周期 | addRecipe | deleteRecipe | modifyRecipe | queryRecipe | recipeIn.recipeID | recipeIn.ingredientType | recipeIn.ingredientRatio | recipeIn.productionTemperature | 预期 recipeAdded | 预期 error | 预期 status | 预期 recipeModified | 预期 recipeQueryResult.recipeID | 预期 recipeQueryResult.ingredientType | 预期 recipeQueryResult.ingredientRatio | 预期 recipeQueryResult.productionTemperature | 预期 recipeDeleted | 实际 recipeAdded | 实际 error | 实际 status | 实际 recipeModified | 实际 recipeQueryResult.recipeID | 实际 recipeQueryResult.ingredientType | 实际 recipeQueryResult.ingredientRatio | 实际 recipeQueryResult.productionTemperature | 实际 recipeDeleted | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 101 | 1 | 0.5 | 180.0 | 1 |  |  |  |  |  |  |  |  | 1 |  |  |  |  |  |  |  |  | prepare | PASS |
| 1 | 0 | 0 | 0 | 0 | 101 | 1 | 0.5 | 180.0 |  | 0 | 0 |  |  |  |  |  |  |  | 0 | 0 |  |  |  |  |  |  | released | PASS |
| 2 | 0 | 0 | 1 | 0 | 101 | 7 | 0.8 | 220.0 |  | 0 | 0 | 1 |  |  |  |  |  |  | 0 | 0 | 1 |  |  |  |  |  | modify 101 | PASS |
| 3 | 0 | 0 | 0 | 0 | 101 | 7 | 0.8 | 220.0 |  | 0 | 0 |  |  |  |  |  |  |  | 0 | 0 |  |  |  |  |  |  | released | PASS |
| 4 | 0 | 0 | 0 | 1 | 101 | 0 | 0.0 | 0.0 |  |  |  |  | 101 | 7 | 0.8 | 220.0 |  |  |  |  |  | 101 | 7 | 0.8 | 220.0 |  | query shows the modified values | PASS |
| 5 | 0 | 0 | 0 | 0 | 101 | 0 | 0.0 | 0.0 |  | 0 | 0 |  |  |  |  |  |  |  | 0 | 0 |  |  |  |  |  |  | released | PASS |
| 6 | 0 | 0 | 1 | 0 | 777 | 0 | 0.0 | 0.0 |  | 1 | 32773 |  |  |  |  |  |  |  | 1 | 32773 |  |  |  |  |  |  | modify a missing number -> 16#8005 | PASS |
| 7 | 0 | 0 | 0 | 0 | 777 | 0 | 0.0 | 0.0 |  | 0 | 0 |  |  |  |  |  |  |  | 0 | 0 |  |  |  |  |  |  | released | PASS |
| 8 | 0 | 1 | 0 | 0 | 101 | 0 | 0.0 | 0.0 |  | 0 | 0 |  |  |  |  |  | 1 |  | 0 | 0 |  |  |  |  |  | 1 | delete 101 | PASS |
| 9 | 0 | 0 | 0 | 0 | 101 | 0 | 0.0 | 0.0 |  | 0 | 0 |  |  |  |  |  |  |  | 0 | 0 |  |  |  |  |  |  | released | PASS |
| 10 | 0 | 0 | 0 | 1 | 101 | 0 | 0.0 | 0.0 |  | 1 | 32769 |  |  |  |  |  |  |  | 1 | 32769 |  |  |  |  |  |  | deleted recipe can no longer be queried | PASS |
| 11 | 0 | 0 | 0 | 0 | 101 | 0 | 0.0 | 0.0 |  | 0 | 0 |  |  |  |  |  |  |  | 0 | 0 |  |  |  |  |  |  | released | PASS |
| 12 | 0 | 1 | 0 | 0 | 101 | 0 | 0.0 | 0.0 |  | 1 | 32772 |  |  |  |  |  |  |  | 1 | 32772 |  |  |  |  |  |  | delete a missing number -> 16#8004 | PASS |


## H04 FIFO First-In-First-Out Queue（`H04_FIFO`）

- 编译：**未通过**（用例记为未通过）；用例通过 0/5；整题未通过

- 仿真器无法执行：期望 ':='，实际是 'IF'

### TC01 Basic enqueue and dequeue in FIFO order

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Basic enqueue and dequeue in FIFO order |
| 所属题目 | H04 FIFO First-In-First-Out Queue（`H04_FIFO`） |
| 初始状态 | power-up: queue empty, elementCount 0, capacity 5 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | one operation per rising edge, held signal does not repeat, values come out in insertion order |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'IF' |

| 周期 | enqueue | dequeue | reset | item | 预期 elementCount | 预期 status | 预期 item | 实际 elementCount | 实际 status | 实际 item | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 |  | 0 | 0 |  |  |  |  | power-up: empty | FAIL |
| 1 | 1 | 0 | 0 | 11 | 1 | 0 |  |  |  |  | enqueue 11 | 未执行 |
| 2 | 1 | 0 | 0 | 99 | 1 |  |  |  |  |  | signal held -> no second enqueue | 未执行 |
| 3 | 0 | 0 | 0 | 99 | 1 |  |  |  |  |  | released | 未执行 |
| 4 | 1 | 0 | 0 | 22 | 2 |  |  |  |  |  | enqueue 22 | 未执行 |
| 5 | 0 | 0 | 0 |  | 2 |  |  |  |  |  | released | 未执行 |
| 6 | 0 | 1 | 0 |  | 1 | 0 | 11 |  |  |  | dequeue returns the first value 11 | 未执行 |
| 7 | 0 | 0 | 0 |  | 1 |  |  |  |  |  | released | 未执行 |
| 8 | 0 | 1 | 0 |  | 0 |  | 22 |  |  |  | dequeue returns 22, queue empty | 未执行 |

### TC02 Full queue rejects an enqueue

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Full queue rejects an enqueue |
| 所属题目 | H04 FIFO First-In-First-Out Queue（`H04_FIFO`） |
| 初始状态 | power-up, capacity 8 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | capacity 8 reached, 16#8002 reported, count unchanged, space freed by a dequeue |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'IF' |

| 周期 | enqueue | dequeue | reset | item | 预期 elementCount | 预期 status | 预期 item | 实际 elementCount | 实际 status | 实际 item | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 1 | 0 |  |  |  |  | enqueue 1 | FAIL |
| 1 | 0 | 0 | 0 | 1 | 1 |  |  |  |  |  | release | 未执行 |
| 2 | 1 | 0 | 0 | 2 | 2 | 0 |  |  |  |  | enqueue 2 | 未执行 |
| 3 | 0 | 0 | 0 | 2 | 2 |  |  |  |  |  | release | 未执行 |
| 4 | 1 | 0 | 0 | 3 | 3 | 0 |  |  |  |  | enqueue 3 | 未执行 |
| 5 | 0 | 0 | 0 | 3 | 3 |  |  |  |  |  | release | 未执行 |
| 6 | 1 | 0 | 0 | 4 | 4 | 0 |  |  |  |  | enqueue 4 | 未执行 |
| 7 | 0 | 0 | 0 | 4 | 4 |  |  |  |  |  | release | 未执行 |
| 8 | 1 | 0 | 0 | 5 | 5 | 0 |  |  |  |  | enqueue 5 | 未执行 |
| 9 | 0 | 0 | 0 | 5 | 5 |  |  |  |  |  | release | 未执行 |
| 10 | 1 | 0 | 0 | 6 | 6 | 0 |  |  |  |  | enqueue 6 | 未执行 |
| 11 | 0 | 0 | 0 | 6 | 6 |  |  |  |  |  | release | 未执行 |
| 12 | 1 | 0 | 0 | 7 | 7 | 0 |  |  |  |  | enqueue 7 | 未执行 |
| 13 | 0 | 0 | 0 | 7 | 7 |  |  |  |  |  | release | 未执行 |
| 14 | 1 | 0 | 0 | 8 | 8 | 0 |  |  |  |  | enqueue 8 | 未执行 |
| 15 | 0 | 0 | 0 | 8 | 8 |  |  |  |  |  | release | 未执行 |
| 16 | 1 | 0 | 0 | 99 | 8 | 32770 | 99 |  |  |  | enqueue into a full queue -> 16#8002, unchanged | 未执行 |
| 17 | 0 | 0 | 0 | 99 | 8 |  |  |  |  |  | release | 未执行 |
| 18 | 0 | 1 | 0 |  | 7 | 0 | 1 |  |  |  | dequeue frees a slot, FIFO order returns 1 | 未执行 |
| 19 | 0 | 0 | 0 |  | 7 |  |  |  |  |  | release | 未执行 |
| 20 | 1 | 0 | 0 | 9 | 8 | 0 |  |  |  |  | enqueue succeeds again (wrap-around) | 未执行 |

### TC03 Empty queue rejects a dequeue

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Empty queue rejects a dequeue |
| 所属题目 | H04 FIFO First-In-First-Out Queue（`H04_FIFO`） |
| 初始状态 | power-up, queue empty |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | 16#8001 reported, item unchanged, count stays zero |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'IF' |

| 周期 | enqueue | dequeue | reset | item | 预期 elementCount | 预期 status | 预期 item | 实际 elementCount | 实际 status | 实际 item | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 77 | 0 | 32769 | 77 |  |  |  | dequeue from an empty queue -> 16#8001, item unchanged | FAIL |
| 1 | 0 | 0 | 0 | 77 | 0 |  |  |  |  |  | release | 未执行 |
| 2 | 1 | 0 | 0 | 33 | 1 | 0 |  |  |  |  | enqueue works | 未执行 |
| 3 | 0 | 0 | 0 | 33 | 1 |  |  |  |  |  | release | 未执行 |
| 4 | 0 | 1 | 0 |  | 0 | 0 | 33 |  |  |  | dequeue returns 33 | 未执行 |
| 5 | 0 | 0 | 0 |  | 0 |  |  |  |  |  | release | 未执行 |
| 6 | 0 | 1 | 0 |  | 0 | 32769 |  |  |  |  | empty again -> 16#8001 | 未执行 |

### TC04 Reset has priority and empties the queue

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Reset has priority and empties the queue |
| 所属题目 | H04 FIFO First-In-First-Out Queue（`H04_FIFO`） |
| 初始状态 | power-up |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | reset clears the count, takes priority over enqueue/dequeue, status stays 16#0000 |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'IF' |

| 周期 | enqueue | dequeue | reset | item | 预期 elementCount | 预期 status | 实际 elementCount | 实际 status | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 5 | 1 |  |  |  | enqueue | FAIL |
| 1 | 0 | 0 | 0 | 5 | 1 |  |  |  | release | 未执行 |
| 2 | 1 | 0 | 0 | 6 | 2 |  |  |  | enqueue | 未执行 |
| 3 | 0 | 0 | 0 | 6 | 2 |  |  |  | release | 未执行 |
| 4 | 0 | 0 | 1 |  | 0 | 0 |  |  | reset -> empty, no error | 未执行 |
| 5 | 1 | 0 | 1 | 9 | 0 | 0 |  |  | reset has priority over enqueue | 未执行 |
| 6 | 0 | 0 | 0 |  | 0 |  |  |  | release | 未执行 |
| 7 | 0 | 1 | 0 |  | 0 | 32769 |  |  | queue really is empty | 未执行 |
| 8 | 0 | 0 | 0 |  | 0 |  |  |  | release | 未执行 |
| 9 | 1 | 0 | 0 | 8 | 1 | 0 |  |  | queue usable after reset | 未执行 |

### TC05 Circular wrap-around keeps FIFO order

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC05 Circular wrap-around keeps FIFO order |
| 所属题目 | H04 FIFO First-In-First-Out Queue（`H04_FIFO`） |
| 初始状态 | power-up, capacity 5 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | repeated enqueue/dequeue cycles past the end of the buffer |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'IF' |

| 周期 | enqueue | dequeue | reset | item | 预期 elementCount | 预期 item | 实际 elementCount | 实际 item | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 1 |  |  |  | in 1 | FAIL |
| 1 | 0 | 0 | 0 | 1 | 1 |  |  |  | release | 未执行 |
| 2 | 1 | 0 | 0 | 2 | 2 |  |  |  | in 2 | 未执行 |
| 3 | 0 | 0 | 0 | 2 | 2 |  |  |  | release | 未执行 |
| 4 | 1 | 0 | 0 | 3 | 3 |  |  |  | in 3 | 未执行 |
| 5 | 0 | 0 | 0 | 3 | 3 |  |  |  | release | 未执行 |
| 6 | 0 | 1 | 0 |  | 2 | 1 |  |  | out 1 | 未执行 |
| 7 | 0 | 0 | 0 |  | 2 |  |  |  | release | 未执行 |
| 8 | 0 | 1 | 0 |  | 1 | 2 |  |  | out 2 | 未执行 |
| 9 | 0 | 0 | 0 |  | 1 |  |  |  | release | 未执行 |
| 10 | 1 | 0 | 0 | 4 | 2 |  |  |  | in 4 (wraps) | 未执行 |
| 11 | 0 | 0 | 0 | 4 | 2 |  |  |  | release | 未执行 |
| 12 | 1 | 0 | 0 | 5 | 3 |  |  |  | in 5 | 未执行 |
| 13 | 0 | 0 | 0 | 5 | 3 |  |  |  | release | 未执行 |
| 14 | 0 | 1 | 0 |  | 2 | 3 |  |  | out 3 - order preserved across the wrap | 未执行 |
| 15 | 0 | 0 | 0 |  | 2 |  |  |  | release | 未执行 |
| 16 | 0 | 1 | 0 |  | 1 | 4 |  |  | out 4 | 未执行 |
| 17 | 0 | 0 | 0 |  | 1 |  |  |  | release | 未执行 |
| 18 | 0 | 1 | 0 |  | 0 | 5 |  |  | out 5, queue empty | 未执行 |


## H05 Mechanical Arm Control（`H05_MechArm`）

- 编译：**未通过**（用例记为未通过）；用例通过 0/7；整题未通过

- 仿真器无法执行：控制结构缺少结束标记 ELSE/ELSIF/END_IF

### TC01 Manual mode: each button moves until its limit switch

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Manual mode: each button moves until its limit switch |
| 所属题目 | H05 Mechanical Arm Control（`H05_MechArm`） |
| 初始状态 | power-up, EmergencyStop=1 (inactive), ManualMode=1, arm at home (top-left, released) |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | button pressed & not in position -> move; in position -> no move; release -> stop; all six actions; Start ignored |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 控制结构缺少结束标记 ELSE/ELSIF/END_IF |

| 周期 | ManualMode | SingleStepMode | SingleCycleMode | ContinuousMode | EmergencyStop | Start | DownButton | UpButton | LeftButton | RightButton | GripButton | ReleaseButton | DownLimitSwitch | UpLimitSwitch | LeftLimitSwitch | RightLimitSwitch | GripLimitSwitch | ReleaseLimitSwitch | 预期 MoveDown | 预期 MoveUp | 预期 MoveLeft | 预期 MoveRight | 预期 ActivateGrip | 预期 ActivateRelease | 实际 MoveDown | 实际 MoveUp | 实际 MoveLeft | 实际 MoveRight | 实际 ActivateGrip | 实际 ActivateRelease | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | no button -> no motion | FAIL |
| 1 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | DownButton, not at down limit -> MoveDown | 未执行 |
| 2 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | still moving down (up switch released) | 未执行 |
| 3 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | down limit reached -> stop although button held | 未执行 |
| 4 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | button released | 未执行 |
| 5 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | UpButton -> MoveUp | 未执行 |
| 6 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | button released mid-way -> stop | 未执行 |
| 7 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | UpButton at up limit -> no motion | 未执行 |
| 8 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |  |  |  |  |  |  | RightButton, not at right limit -> MoveRight | 未执行 |
| 9 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | LeftButton at left limit -> no motion | 未执行 |
| 10 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |  |  |  |  |  |  | GripButton, not gripped -> ActivateGrip | 未执行 |
| 11 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | ReleaseButton while already released -> no action | 未执行 |
| 12 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  |  |  | ReleaseButton while gripped -> ActivateRelease | 未执行 |
| 13 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | Start has no effect in manual mode | 未执行 |

### TC02 Single-step mode: one action per Start press

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Single-step mode: one action per Start press |
| 所属题目 | H05 Mechanical Arm Control（`H05_MechArm`） |
| 初始状态 | power-up, SingleStepMode=1, arm at home |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | eight actions each started by Start, each stops at its limit and waits; Start held does not start the next action |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 控制结构缺少结束标记 ELSE/ELSIF/END_IF |

| 周期 | ManualMode | SingleStepMode | SingleCycleMode | ContinuousMode | EmergencyStop | Start | DownButton | UpButton | LeftButton | RightButton | GripButton | ReleaseButton | DownLimitSwitch | UpLimitSwitch | LeftLimitSwitch | RightLimitSwitch | GripLimitSwitch | ReleaseLimitSwitch | 预期 MoveDown | 预期 MoveUp | 预期 MoveLeft | 预期 MoveRight | 预期 ActivateGrip | 预期 ActivateRelease | 实际 MoveDown | 实际 MoveUp | 实际 MoveLeft | 实际 MoveRight | 实际 ActivateGrip | 实际 ActivateRelease | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | Start -> down begins | FAIL |
| 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | down: moving, Start released | 未执行 |
| 2 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | down: in motion | 未执行 |
| 3 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | down limit reached -> stop, wait for Start | 未执行 |
| 4 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |  |  |  |  |  |  | Start -> grip begins | 未执行 |
| 5 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |  |  |  |  |  |  | grip: moving, Start released | 未执行 |
| 6 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |  |  |  |  |  |  | grip: in motion | 未执行 |
| 7 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | grip limit reached -> stop, wait for Start | 未执行 |
| 8 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | Start -> up begins | 未执行 |
| 9 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | up: moving, Start released | 未执行 |
| 10 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | up: in motion | 未执行 |
| 11 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | up limit reached -> stop, wait for Start | 未执行 |
| 12 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |  |  |  |  |  |  | Start -> right begins | 未执行 |
| 13 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |  |  |  |  |  |  | right: moving, Start released | 未执行 |
| 14 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |  |  |  |  |  |  | right: in motion | 未执行 |
| 15 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | right limit reached -> stop, wait for Start | 未执行 |
| 16 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | Start -> down begins | 未执行 |
| 17 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | down: moving, Start released | 未执行 |
| 18 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | down: in motion | 未执行 |
| 19 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | down limit reached -> stop, wait for Start | 未执行 |
| 20 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  |  |  | Start -> release begins | 未执行 |
| 21 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  |  |  | release: moving, Start released | 未执行 |
| 22 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  |  |  | release: in motion | 未执行 |
| 23 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | release limit reached -> stop, wait for Start | 未执行 |
| 24 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | Start -> up begins | 未执行 |
| 25 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | up: moving, Start released | 未执行 |
| 26 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | up: in motion | 未执行 |
| 27 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | up limit reached -> stop, wait for Start | 未执行 |
| 28 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |  |  |  |  |  |  | Start -> left begins | 未执行 |
| 29 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |  |  |  |  |  |  | left: moving, Start released | 未执行 |
| 30 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |  |  |  |  |  |  | left: in motion | 未执行 |
| 31 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | left limit reached -> stop, wait for Start | 未执行 |

### TC03 Single-cycle mode: one Start runs the whole cycle and stops at home

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Single-cycle mode: one Start runs the whole cycle and stops at home |
| 所属题目 | H05 Mechanical Arm Control（`H05_MechArm`） |
| 初始状态 | power-up, SingleCycleMode=1, arm at home |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | automatic chaining of all eight actions, stops at home, waits for Start |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 控制结构缺少结束标记 ELSE/ELSIF/END_IF |

| 周期 | ManualMode | SingleStepMode | SingleCycleMode | ContinuousMode | EmergencyStop | Start | DownButton | UpButton | LeftButton | RightButton | GripButton | ReleaseButton | DownLimitSwitch | UpLimitSwitch | LeftLimitSwitch | RightLimitSwitch | GripLimitSwitch | ReleaseLimitSwitch | 预期 MoveDown | 预期 MoveUp | 预期 MoveLeft | 预期 MoveRight | 预期 ActivateGrip | 预期 ActivateRelease | 实际 MoveDown | 实际 MoveUp | 实际 MoveLeft | 实际 MoveRight | 实际 ActivateGrip | 实际 ActivateRelease | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | Start -> down begins | FAIL |
| 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | down: moving, Start released | 未执行 |
| 2 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | down: in motion | 未执行 |
| 3 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 |  |  |  |  |  |  |  |  |  |  |  | down limit reached -> completed action stops | 未执行 |
| 4 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |  |  |  |  |  |  | next action ActivateGrip is running (same or next cycle) | 未执行 |
| 5 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |  |  |  |  |  |  | grip begins automatically | 未执行 |
| 6 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |  |  |  |  |  |  | grip: in motion | 未执行 |
| 7 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |  |  |  |  | 0 |  |  |  |  |  |  |  | grip limit reached -> completed action stops | 未执行 |
| 8 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | next action MoveUp is running (same or next cycle) | 未执行 |
| 9 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | up begins automatically | 未执行 |
| 10 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | up: in motion | 未执行 |
| 11 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |  | 0 |  |  |  |  |  |  |  |  |  |  | up limit reached -> completed action stops | 未执行 |
| 12 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |  |  |  |  |  |  | next action MoveRight is running (same or next cycle) | 未执行 |
| 13 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |  |  |  |  |  |  | right begins automatically | 未执行 |
| 14 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |  |  |  |  |  |  | right: in motion | 未执行 |
| 15 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 |  |  |  | 0 |  |  |  |  |  |  |  |  | right limit reached -> completed action stops | 未执行 |
| 16 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | next action MoveDown is running (same or next cycle) | 未执行 |
| 17 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | down begins automatically | 未执行 |
| 18 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | down: in motion | 未执行 |
| 19 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  | down limit reached -> completed action stops | 未执行 |
| 20 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  |  |  | next action ActivateRelease is running (same or next cycle) | 未执行 |
| 21 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  |  |  | release begins automatically | 未执行 |
| 22 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  |  |  | release: in motion | 未执行 |
| 23 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 |  |  |  |  |  | 0 |  |  |  |  |  |  | release limit reached -> completed action stops | 未执行 |
| 24 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | next action MoveUp is running (same or next cycle) | 未执行 |
| 25 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | up begins automatically | 未执行 |
| 26 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | up: in motion | 未执行 |
| 27 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 |  | 0 |  |  |  |  |  |  |  |  |  |  | up limit reached -> completed action stops | 未执行 |
| 28 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |  |  |  |  |  |  | next action MoveLeft is running (same or next cycle) | 未执行 |
| 29 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |  |  |  |  |  |  | left begins automatically | 未执行 |
| 30 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |  |  |  |  |  |  | left: in motion | 未执行 |
| 31 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | left limit reached -> cycle end | 未执行 |
| 32 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | back at home: stays stopped (single cycle) | 未执行 |
| 33 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | still stopped without Start | 未执行 |
| 34 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | new Start -> next cycle begins | 未执行 |

### TC04 Continuous mode: cycles repeat without Start

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Continuous mode: cycles repeat without Start |
| 所属题目 | H05 Mechanical Arm Control（`H05_MechArm`） |
| 初始状态 | power-up, ContinuousMode=1, arm at home |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | after the last action the next cycle starts automatically |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 控制结构缺少结束标记 ELSE/ELSIF/END_IF |

| 周期 | ManualMode | SingleStepMode | SingleCycleMode | ContinuousMode | EmergencyStop | Start | DownButton | UpButton | LeftButton | RightButton | GripButton | ReleaseButton | DownLimitSwitch | UpLimitSwitch | LeftLimitSwitch | RightLimitSwitch | GripLimitSwitch | ReleaseLimitSwitch | 预期 MoveDown | 预期 MoveUp | 预期 MoveLeft | 预期 MoveRight | 预期 ActivateGrip | 预期 ActivateRelease | 实际 MoveDown | 实际 MoveUp | 实际 MoveLeft | 实际 MoveRight | 实际 ActivateGrip | 实际 ActivateRelease | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | Start -> down begins | FAIL |
| 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | down: moving, Start released | 未执行 |
| 2 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | down: in motion | 未执行 |
| 3 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 |  |  |  |  |  |  |  |  |  |  |  | down limit reached -> completed action stops | 未执行 |
| 4 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |  |  |  |  |  |  | next action ActivateGrip is running (same or next cycle) | 未执行 |
| 5 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |  |  |  |  |  |  | grip begins automatically | 未执行 |
| 6 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |  |  |  |  |  |  | grip: in motion | 未执行 |
| 7 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |  |  |  |  | 0 |  |  |  |  |  |  |  | grip limit reached -> completed action stops | 未执行 |
| 8 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | next action MoveUp is running (same or next cycle) | 未执行 |
| 9 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | up begins automatically | 未执行 |
| 10 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | up: in motion | 未执行 |
| 11 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |  | 0 |  |  |  |  |  |  |  |  |  |  | up limit reached -> completed action stops | 未执行 |
| 12 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |  |  |  |  |  |  | next action MoveRight is running (same or next cycle) | 未执行 |
| 13 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |  |  |  |  |  |  | right begins automatically | 未执行 |
| 14 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |  |  |  |  |  |  | right: in motion | 未执行 |
| 15 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 |  |  |  | 0 |  |  |  |  |  |  |  |  | right limit reached -> completed action stops | 未执行 |
| 16 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | next action MoveDown is running (same or next cycle) | 未执行 |
| 17 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | down begins automatically | 未执行 |
| 18 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | down: in motion | 未执行 |
| 19 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  | down limit reached -> completed action stops | 未执行 |
| 20 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  |  |  | next action ActivateRelease is running (same or next cycle) | 未执行 |
| 21 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  |  |  | release begins automatically | 未执行 |
| 22 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  |  |  | release: in motion | 未执行 |
| 23 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 |  |  |  |  |  | 0 |  |  |  |  |  |  | release limit reached -> completed action stops | 未执行 |
| 24 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | next action MoveUp is running (same or next cycle) | 未执行 |
| 25 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | up begins automatically | 未执行 |
| 26 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | up: in motion | 未执行 |
| 27 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 |  | 0 |  |  |  |  |  |  |  |  |  |  | up limit reached -> completed action stops | 未执行 |
| 28 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |  |  |  |  |  |  | next action MoveLeft is running (same or next cycle) | 未执行 |
| 29 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |  |  |  |  |  |  | left begins automatically | 未执行 |
| 30 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |  |  |  |  |  |  | left: in motion | 未执行 |
| 31 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |  |  | 0 |  |  |  |  |  |  |  |  |  | left limit reached -> completed action stops | 未执行 |
| 32 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | next action MoveDown is running (same or next cycle) | 未执行 |
| 33 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | second cycle running without Start | 未执行 |

### TC05 Emergency stop in automatic and manual modes

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC05 Emergency stop in automatic and manual modes |
| 所属题目 | H05 Mechanical Arm Control（`H05_MechArm`） |
| 初始状态 | power-up, SingleCycleMode=1, arm at home |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | all outputs OFF immediately, stay OFF while estop active, no automatic resume, manual buttons blocked |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 控制结构缺少结束标记 ELSE/ELSIF/END_IF |

| 周期 | ManualMode | SingleStepMode | SingleCycleMode | ContinuousMode | EmergencyStop | Start | DownButton | UpButton | LeftButton | RightButton | GripButton | ReleaseButton | DownLimitSwitch | UpLimitSwitch | LeftLimitSwitch | RightLimitSwitch | GripLimitSwitch | ReleaseLimitSwitch | 预期 MoveDown | 预期 MoveUp | 预期 MoveLeft | 预期 MoveRight | 预期 ActivateGrip | 预期 ActivateRelease | 实际 MoveDown | 实际 MoveUp | 实际 MoveLeft | 实际 MoveRight | 实际 ActivateGrip | 实际 ActivateRelease | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | start cycle | FAIL |
| 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | moving down | 未执行 |
| 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | ESTOP -> all outputs OFF | 未执行 |
| 3 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | Start during estop ignored | 未执行 |
| 4 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | estop released -> no automatic resume | 未执行 |
| 5 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | manual button during estop -> no motion | 未执行 |
| 6 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | estop released: manual works again | 未执行 |

### TC06 Automatic modes wait for Start; manual buttons ignored

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC06 Automatic modes wait for Start; manual buttons ignored |
| 所属题目 | H05 Mechanical Arm Control（`H05_MechArm`） |
| 初始状态 | power-up, arm at home |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | no motion without Start in single-step/single-cycle/continuous; manual buttons ignored in auto modes |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 控制结构缺少结束标记 ELSE/ELSIF/END_IF |

| 周期 | ManualMode | SingleStepMode | SingleCycleMode | ContinuousMode | EmergencyStop | Start | DownButton | UpButton | LeftButton | RightButton | GripButton | ReleaseButton | DownLimitSwitch | UpLimitSwitch | LeftLimitSwitch | RightLimitSwitch | GripLimitSwitch | ReleaseLimitSwitch | 预期 MoveDown | 预期 MoveUp | 预期 MoveLeft | 预期 MoveRight | 预期 ActivateGrip | 预期 ActivateRelease | 实际 MoveDown | 实际 MoveUp | 实际 MoveLeft | 实际 MoveRight | 实际 ActivateGrip | 实际 ActivateRelease | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | single-step idle | FAIL |
| 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | single-cycle idle, manual button ignored | 未执行 |
| 2 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | continuous idle, manual button ignored | 未执行 |
| 3 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  | Start -> continuous cycle begins | 未执行 |

### TC07 Single-step mode: one Start press performs exactly one action

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC07 Single-step mode: one Start press performs exactly one action |
| 所属题目 | H05 Mechanical Arm Control（`H05_MechArm`） |
| 初始状态 | single-step mode, e-stop released, arm idle at step 0 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | single-step mode is edge-triggered on Start; after an action completes the arm must wait for a new Start edge. This case fails on Part 2's reference implementation (DEFECT-H05-01) |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 控制结构缺少结束标记 ELSE/ELSIF/END_IF |

| 周期 | ManualMode | SingleStepMode | SingleCycleMode | ContinuousMode | EmergencyStop | Start | DownButton | UpButton | LeftButton | RightButton | GripButton | ReleaseButton | DownLimitSwitch | UpLimitSwitch | LeftLimitSwitch | RightLimitSwitch | GripLimitSwitch | ReleaseLimitSwitch | 预期 MoveDown | 预期 ActivateGrip | 预期 MoveUp | 实际 MoveDown | 实际 ActivateGrip | 实际 MoveUp | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  |  | Start edge -> action 1: move down | FAIL |
| 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  |  | Start released, action 1 continues | 未执行 |
| 2 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  | down limit reached: action 1 finished | 未执行 |
| 3 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  | 0 |  |  |  |  | DECISIVE: no new Start edge, so the arm must wait. Action 2 (grip) must not begin | 未执行 |
| 4 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  | 0 |  |  |  |  | still waiting: one Start press, one action | 未执行 |
| 5 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  | 0 |  |  |  |  | still waiting, no unattended progression | 未执行 |
| 6 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  | 1 |  |  |  |  | a fresh Start edge now performs action 2: grip | 未执行 |
| 7 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  | 1 |  |  |  |  | grip continues while Start is held | 未执行 |
| 8 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 |  | 0 | 0 |  |  |  | grip limit reached: action 2 finished, and no new Start edge, so action 3 must not begin | 未执行 |


## H06 Production Control（`H06_Production`）

- 编译：通过；用例通过 1/6；整题未通过

### TC01 Manual jog with interlock

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 Manual jog with interlock |
| 所属题目 | H06 Production Control（`H06_Production`） |
| 初始状态 | power-up, Mode=0 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | forward, reverse, both -> OFF, release -> stop, kick/light OFF in manual |
| 实际输出及结果 | ✅ 通过 |

| 周期 | Mode | ForwardButton | ReverseButton | SensorFeed | SensorWash | SensorWeight | SensorFiring | SensorOutput | washComplete | weightComplete | weight | firingComplete | 预期 MotorForward | 预期 MotorReverse | 预期 kick | 预期 CompletionLight | 实际 MotorForward | 实际 MotorReverse | 实际 kick | 实际 CompletionLight | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | all OFF | PASS |
| 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | forward | PASS |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | release -> stop | PASS |
| 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | reverse | PASS |
| 4 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | interlock: both OFF | PASS |
| 5 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | auto signals ignored in manual, no kick | PASS |

### TC02 Automatic cycle with qualified material (weight 150)

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 Automatic cycle with qualified material (weight 150) |
| 所属题目 | H06 Production Control（`H06_Production`） |
| 初始状态 | power-up, Mode=1, no material |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | all five stations, motor stops at each sensor, firingTemp = 525 for weight 150, light ON/OFF |
| 实际输出及结果 | ❌ 不通过；周期 2：MotorForward 预期 1，实际 False；周期 3：MotorForward 预期 1，实际 False；周期 7：MotorForward 预期 1，实际 False |

| 周期 | Mode | ForwardButton | ReverseButton | SensorFeed | SensorWash | SensorWeight | SensorFiring | SensorOutput | washComplete | weightComplete | weight | firingComplete | 预期 MotorForward | 预期 MotorReverse | 预期 kick | 预期 CompletionLight | 预期 firingTemp | 实际 MotorForward | 实际 MotorReverse | 实际 kick | 实际 CompletionLight | 实际 firingTemp | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | auto idle | PASS |
| 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  | material at feed -> forward (trigger cycle) | PASS |
| 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | motor starts in the following cycle | FAIL |
| 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | moving to wash | FAIL |
| 4 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | at wash -> stop | PASS |
| 5 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | waiting washComplete | PASS |
| 6 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |  | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  | washComplete -> forward (trigger cycle) | PASS |
| 7 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | motor starts in the following cycle | FAIL |
| 8 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | moving to weight | FAIL |
| 9 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | at weight -> stop | PASS |
| 10 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 150 | 0 |  | 0 | 0 | 0 | 525.0 |  | 0 | 0 | 0 | 525.0 | qualified: firingTemp=525, forward, no kick (trigger cycle) | PASS |
| 11 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 150 | 0 | 1 | 0 | 0 | 0 | 525.0 | 0 | 0 | 0 | 0 | 0.0 | motor starts in the following cycle | FAIL |
| 12 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 150 | 0 | 1 | 0 | 0 | 0 | 525.0 | 0 | 0 | 0 | 0 | 0.0 | moving to firing, temp held | FAIL |
| 13 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 150 | 0 | 0 | 0 | 0 | 0 | 525.0 | 0 | 0 | 0 | 0 | 0.0 | at firing -> stop | FAIL |
| 14 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 150 | 1 |  | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  | firingComplete -> forward (trigger cycle) | PASS |
| 15 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 150 | 0 | 1 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | motor starts in the following cycle | FAIL |
| 16 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 150 | 0 | 1 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | moving to output | FAIL |
| 17 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 150 | 0 | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  |  | at output -> stop, light ON (arrival cycle) | PASS |
| 18 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 150 | 0 | 0 | 0 | 0 | 1 |  | 0 | 0 | 0 | 0 |  | completion light on in the following cycle | FAIL |
| 19 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 150 | 0 | 0 | 0 | 0 | 1 |  | 0 | 0 | 0 | 0 |  | light stays ON while product present | FAIL |
| 20 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 150 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | product removed -> light OFF | PASS |
| 21 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  | next material starts a new cycle (trigger cycle) | PASS |
| 22 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | motor starts in the following cycle | FAIL |

### TC03 Weight boundaries and temperature mapping

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 Weight boundaries and temperature mapping |
| 所属题目 | H06 Production Control（`H06_Production`） |
| 初始状态 | power-up, Mode=1 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | weight 100 -> 500, weight 200 -> 550, weight 120 -> 510 (linear), all qualified |
| 实际输出及结果 | ❌ 不通过；周期 1：MotorForward 预期 1，实际 False；周期 4：MotorForward 预期 1，实际 False；周期 7：MotorForward 预期 1，实际 False；firingTemp 预期 500.0，实际 0.0 |

| 周期 | Mode | ForwardButton | ReverseButton | SensorFeed | SensorWash | SensorWeight | SensorFiring | SensorOutput | washComplete | weightComplete | weight | firingComplete | 预期 MotorReverse | 预期 kick | 预期 CompletionLight | 预期 MotorForward | 预期 firingTemp | 实际 MotorReverse | 实际 kick | 实际 CompletionLight | 实际 MotorForward | 实际 firingTemp | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  |  | start (trigger cycle) | PASS |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 0 | 0 | 0 | 0 |  | motor starts in the following cycle | FAIL |
| 2 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | at wash | PASS |
| 3 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  |  | washed (trigger cycle) | PASS |
| 4 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 0 | 0 | 0 | 0 |  | motor starts in the following cycle | FAIL |
| 5 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | at weight | PASS |
| 6 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 100 | 0 | 0 | 0 | 0 |  | 500.0 | 0 | 0 | 0 |  | 500.0 | weight=100 (lower boundary) qualified, temp 500 (trigger cycle) | PASS |
| 7 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 100 | 0 | 0 | 0 | 0 | 1 | 500.0 | 0 | 0 | 0 | 0 | 0.0 | motor starts in the following cycle | FAIL |
| 8 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 100 | 0 | 0 | 0 | 0 | 0 | 500.0 | 0 | 0 | 0 | 0 | 0.0 | at firing | FAIL |
| 9 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 100 | 1 | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  |  | fired (trigger cycle) | PASS |
| 10 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 100 | 0 | 0 | 0 | 0 | 1 |  | 0 | 0 | 0 | 0 |  | motor starts in the following cycle | FAIL |
| 11 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 100 | 0 | 0 | 0 |  | 0 |  | 0 | 0 |  | 0 |  | at output (arrival cycle) | PASS |
| 12 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 100 | 0 | 0 | 0 | 1 | 0 |  | 0 | 0 | 0 | 0 |  | completion light on in the following cycle | FAIL |
| 13 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 100 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | removed | PASS |
| 14 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  |  | second material (trigger cycle) | PASS |
| 15 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 0 | 0 | 0 | 0 |  | motor starts in the following cycle | FAIL |
| 16 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | at wash | PASS |
| 17 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  |  | washed (trigger cycle) | PASS |
| 18 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 0 | 0 | 0 | 0 |  | motor starts in the following cycle | FAIL |
| 19 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | at weight | PASS |
| 20 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 200 | 0 | 0 | 0 | 0 |  | 550.0 | 0 | 0 | 0 |  | 550.0 | weight=200 (upper boundary) qualified, temp 550 (trigger cycle) | PASS |
| 21 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 200 | 0 | 0 | 0 | 0 | 1 | 550.0 | 0 | 0 | 0 | 0 | 0.0 | motor starts in the following cycle | FAIL |
| 22 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 200 | 0 | 0 | 0 | 0 | 0 | 550.0 | 0 | 0 | 0 | 0 | 0.0 | at firing | FAIL |
| 23 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 200 | 1 | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  |  | fired (trigger cycle) | PASS |
| 24 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 200 | 0 | 0 | 0 | 0 | 1 |  | 0 | 0 | 0 | 0 |  | motor starts in the following cycle | FAIL |
| 25 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 200 | 0 | 0 | 0 |  | 0 |  | 0 | 0 |  | 0 |  | at output (arrival cycle) | PASS |
| 26 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 200 | 0 | 0 | 0 | 1 | 0 |  | 0 | 0 | 0 | 0 |  | completion light on in the following cycle | FAIL |
| 27 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 200 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | removed | PASS |
| 28 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  |  | third material (trigger cycle) | PASS |
| 29 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 0 | 0 | 0 | 0 |  | motor starts in the following cycle | FAIL |
| 30 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | at wash | PASS |
| 31 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  |  | washed (trigger cycle) | PASS |
| 32 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 0 | 0 | 0 | 0 |  | motor starts in the following cycle | FAIL |
| 33 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 |  | at weight | PASS |
| 34 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 120 | 0 | 0 | 0 | 0 |  | 510.0 | 0 | 0 | 0 |  | 510.0 | weight=120 -> temp 510 (linear) (trigger cycle) | PASS |
| 35 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 120 | 0 | 0 | 0 | 0 | 1 | 510.0 | 0 | 0 | 0 | 0 | 0.0 | motor starts in the following cycle | FAIL |

### TC04 Unqualified material is rejected

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC04 Unqualified material is rejected |
| 所属题目 | H06 Production Control（`H06_Production`） |
| 初始状态 | power-up, Mode=1 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | weight 99.9 -> kick, no forward; weight 200.1 -> kick; line ready again after rejection |
| 实际输出及结果 | ❌ 不通过；周期 1：MotorForward 预期 1，实际 False；周期 4：MotorForward 预期 1，实际 False；周期 9：MotorForward 预期 1，实际 False |

| 周期 | Mode | ForwardButton | ReverseButton | SensorFeed | SensorWash | SensorWeight | SensorFiring | SensorOutput | washComplete | weightComplete | weight | firingComplete | 预期 MotorReverse | 预期 kick | 预期 CompletionLight | 预期 MotorForward | 实际 MotorReverse | 实际 kick | 实际 CompletionLight | 实际 MotorForward | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 |  | start (trigger cycle) | PASS |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | motor starts in the following cycle | FAIL |
| 2 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | at wash | PASS |
| 3 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 |  | washed (trigger cycle) | PASS |
| 4 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | motor starts in the following cycle | FAIL |
| 5 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | at weight | PASS |
| 6 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 99.9 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | weight 99.9 -> kick, motor stays stopped | PASS |
| 7 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 99.9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | rejected material removed -> kick released, motor stopped | PASS |
| 8 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 |  | line accepts the next material (trigger cycle) | PASS |
| 9 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | motor starts in the following cycle | FAIL |
| 10 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | at wash | PASS |
| 11 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 |  | washed (trigger cycle) | PASS |
| 12 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | motor starts in the following cycle | FAIL |
| 13 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | at weight | PASS |
| 14 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 200.1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | weight 200.1 -> kick | PASS |

### TC05 Signals at the wrong station are ignored

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC05 Signals at the wrong station are ignored |
| 所属题目 | H06 Production Control（`H06_Production`） |
| 初始状态 | power-up, Mode=1 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | washComplete/weightComplete/firingComplete before arrival do nothing; manual buttons ignored in auto |
| 实际输出及结果 | ❌ 不通过；周期 3：MotorForward 预期 1，实际 False；周期 6：MotorForward 预期 1，实际 False |

| 周期 | Mode | ForwardButton | ReverseButton | SensorFeed | SensorWash | SensorWeight | SensorFiring | SensorOutput | washComplete | weightComplete | weight | firingComplete | 预期 MotorForward | 预期 MotorReverse | 预期 kick | 预期 CompletionLight | 实际 MotorForward | 实际 MotorReverse | 实际 kick | 实际 CompletionLight | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 150 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | complete signals without material -> nothing, no kick | PASS |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | manual buttons ignored | PASS |
| 2 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 |  | 0 | 0 | 0 | start (trigger cycle) | PASS |
| 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | motor starts in the following cycle | FAIL |
| 4 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 150 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | at wash: other complete signals ignored, motor stopped | PASS |
| 5 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |  | 0 | 0 | 0 |  | 0 | 0 | 0 | correct signal continues (trigger cycle) | PASS |
| 6 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | motor starts in the following cycle | FAIL |
| 7 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 50 | 0 | 0 |  |  |  | 0 |  |  |  | release the confirm button (edge-triggered) | PASS |
| 8 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 50 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | at weight: no kick until weightComplete | PASS |

### TC06 Mode switch during automatic motion

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC06 Mode switch during automatic motion |
| 所属题目 | H06 Production Control（`H06_Production`） |
| 初始状态 | power-up, Mode=1 |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | switch to manual stops motor; back to auto restarts idle |
| 实际输出及结果 | ❌ 不通过；周期 1：MotorForward 预期 1，实际 False；周期 2：MotorForward 预期 1，实际 False |

| 周期 | Mode | ForwardButton | ReverseButton | SensorFeed | SensorWash | SensorWeight | SensorFiring | SensorOutput | washComplete | weightComplete | weight | firingComplete | 预期 MotorReverse | 预期 kick | 预期 CompletionLight | 预期 MotorForward | 实际 MotorReverse | 实际 kick | 实际 CompletionLight | 实际 MotorForward | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 |  | start (trigger cycle) | PASS |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | motor starts in the following cycle | FAIL |
| 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | moving | FAIL |
| 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Mode=0 -> motor stops | PASS |
| 4 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | manual jog | PASS |
| 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | back to auto, idle | PASS |


## C01 Product Reject and Filtering Station（`FB_C01`）

- 编译：通过；用例通过 0/2；整题未通过

### TC01 accept and reject a part

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 accept and reject a part |
| 所属题目 | C01 Product Reject and Filtering Station（`FB_C01`） |
| 初始状态 | counters zero, batch not full |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | normal accept, defective reject, pusher time-out |
| 实际输出及结果 | ❌ 不通过；周期 4：RejectPusher 预期 0，实际 True |

| 周期 | RunSwitch | PartPresent | DefectSensor | ResetButton | 预期 ConveyorMotor | 预期 AcceptCount | 预期 RejectCount | 预期 BatchFull | 预期 RejectPusher | 实际 ConveyorMotor | 实际 AcceptCount | 实际 RejectCount | 实际 BatchFull | 实际 RejectPusher | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | reset | PASS |
| 1 |  | 1 | 0 | 0 | 1 | 1 | 0 |  | 0 | 1 | 1 | 0 |  | 0 | good part accepted | PASS |
| 2 |  | 0 |  |  |  | 1 | 0 |  | 0 |  | 1 | 0 |  | 0 | part leaves | PASS |
| 3 |  | 1 | 1 |  | 1 | 1 | 1 |  | 1 | 1 | 1 | 1 |  | 1 | defective part rejected | PASS |
| 4（保持 1100 ms） |  | 0 |  |  |  |  | 1 |  | 0 |  |  | 1 |  | 1 | pusher retracted after 1 s | FAIL |

### TC02 batch of five stops the conveyor

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 batch of five stops the conveyor |
| 所属题目 | C01 Product Reject and Filtering Station（`FB_C01`） |
| 初始状态 | counters zero, batch not full |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | five accepted parts, batch full, reset |
| 实际输出及结果 | ❌ 不通过；周期 10：ConveyorMotor 预期 1，实际 False |

| 周期 | RunSwitch | ResetButton | PartPresent | 预期 AcceptCount | 预期 BatchFull | 预期 ConveyorMotor | 预期 RejectCount | 实际 AcceptCount | 实际 BatchFull | 实际 ConveyorMotor | 实际 RejectCount | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 0 | 0 | 1 |  | 0 | 0 | 1 |  | reset | PASS |
| 1 |  | 0 | 1 | 1 |  | 1 |  | 1 |  | 1 |  | part 1 | PASS |
| 2 |  |  | 0 | 1 |  |  |  | 1 |  |  |  | gap | PASS |
| 3 |  |  | 1 | 2 |  |  |  | 2 |  |  |  | part 2 | PASS |
| 4 |  |  | 0 | 2 |  |  |  | 2 |  |  |  | gap | PASS |
| 5 |  |  | 1 | 3 |  |  |  | 3 |  |  |  | part 3 | PASS |
| 6 |  |  | 0 | 3 |  |  |  | 3 |  |  |  | gap | PASS |
| 7 |  |  | 1 | 4 |  |  |  | 4 |  |  |  | part 4 | PASS |
| 8 |  |  | 0 | 4 |  |  |  | 4 |  |  |  | gap | PASS |
| 9 |  |  | 1 | 5 | 1 | 0 |  | 5 | 1 | 0 |  | fifth part fills batch | PASS |
| 10 |  | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | reset starts a new batch | FAIL |


## C02 Two-Hand Safety Press（`FB_C02`）

- 编译：通过；用例通过 1/2；整题未通过

### TC01 two-hand press and release

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 two-hand press and release |
| 所属题目 | C02 Two-Hand Safety Press（`FB_C02`） |
| 初始状态 | no buttons, no part, no fault |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | normal two-hand start, cycle-complete pulse, reset state |
| 实际输出及结果 | ❌ 不通过；周期 2：CycleComplete 预期 1，实际 False |

| 周期 | LeftButton | RightButton | PartPresent | ResetButton | 预期 PressOutput | 预期 CycleComplete | 预期 Fault | 实际 PressOutput | 实际 CycleComplete | 实际 Fault | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | reset | PASS |
| 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | both buttons close the press | PASS |
| 2 | 0 | 1 | 1 |  | 0 | 1 |  | 0 | 0 |  | release one button, cycle complete | FAIL |
| 3 | 0 | 0 | 0 |  | 0 | 0 |  | 0 | 0 |  | cycle pulse ends | PASS |

### TC02 anti-tiedown fault

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 anti-tiedown fault |
| 所属题目 | C02 Two-Hand Safety Press（`FB_C02`） |
| 初始状态 | no fault |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | single button held 500 ms, fault latch, reset, restart |
| 实际输出及结果 | ✅ 通过 |

| 周期 | LeftButton | RightButton | PartPresent | ResetButton | 预期 Fault | 预期 PressOutput | 实际 Fault | 实际 PressOutput | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | reset | PASS |
| 1（保持 600 ms） | 1 | 0 |  | 0 | 1 | 0 | 1 | 0 | one button held alone | PASS |
| 2 | 1 | 1 | 1 |  | 1 | 0 | 1 | 0 | fault blocks the press | PASS |
| 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | reset while released | PASS |
| 4 |  |  |  | 0 | 0 | 0 | 0 | 0 | buttons released | PASS |
| 5 | 1 | 1 | 1 |  | 0 | 1 | 0 | 1 | press can restart | PASS |


## C03 Automatic Barrier Gate（`FB_C03`）

- 编译：通过；用例通过 0/2；整题未通过

### TC01 open button and automatic close

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 open button and automatic close |
| 所属题目 | C03 Automatic Barrier Gate（`FB_C03`） |
| 初始状态 | gate closed, no vehicle, no beam |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | manual open, 3 s close delay, closed state |
| 实际输出及结果 | ❌ 不通过；周期 0：GateClosed 预期 1，实际 False；周期 1：GateOpen 预期 1，实际 False；周期 2：GateOpen 预期 1，实际 False |

| 周期 | VehiclePresent | OpenButton | SafetyBeam | 预期 GateOpen | 预期 GateClosed | 预期 WarningLight | 实际 GateOpen | 实际 GateClosed | 实际 WarningLight | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | initial closed | FAIL |
| 1 |  | 1 |  | 1 | 0 | 0 | 0 | 0 | 0 | manual open | FAIL |
| 2 |  | 0 |  | 1 | 0 |  | 0 | 0 |  | no vehicle, close delay running | FAIL |
| 3（保持 3100 ms） |  |  |  | 0 | 1 |  | 0 | 0 |  | closed after 3 s | FAIL |

### TC02 vehicle and safety beam

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 vehicle and safety beam |
| 所属题目 | C03 Automatic Barrier Gate（`FB_C03`） |
| 初始状态 | gate closed |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | hold open by vehicle, beam warning, reopen while closed |
| 实际输出及结果 | ❌ 不通过；周期 0：GateOpen 预期 1，实际 False；周期 1：GateOpen 预期 1，实际 False |

| 周期 | VehiclePresent | SafetyBeam | 预期 GateOpen | 预期 GateClosed | 预期 WarningLight | 实际 GateOpen | 实际 GateClosed | 实际 WarningLight | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 |  | 1 | 0 |  | 0 | 0 |  | vehicle opens gate | FAIL |
| 1 | 0 |  | 1 | 0 |  | 0 | 0 |  | vehicle leaves, close delay | FAIL |
| 2 |  | 1 | 1 |  | 1 | 1 |  | 1 | beam keeps gate open | PASS |
| 3（保持 3100 ms） |  | 0 | 0 | 1 | 0 | 0 | 1 | 0 | beam clear, close after 3 s | PASS |
| 4 |  | 1 | 1 | 0 | 1 | 1 | 0 | 1 | beam reopens closed gate | PASS |


## C04 Star-Delta Motor Starter（`FB_C04`）

- 编译：**未通过**（用例记为未通过）；用例通过 0/2；整题未通过

- 仿真器无法执行：期望 ':='，实际是 'startRisingEdge'

### TC01 start, transition and stop

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 start, transition and stop |
| 所属题目 | C04 Star-Delta Motor Starter（`FB_C04`） |
| 初始状态 | motor stopped |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | star start, 3 s transition, delta run, stop |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'startRisingEdge' |

| 周期 | StartButton | StopButton | Overload | ResetButton | 预期 MainContactor | 预期 StarContactor | 预期 DeltaContactor | 预期 Running | 实际 MainContactor | 实际 StarContactor | 实际 DeltaContactor | 实际 Running | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  | stopped | FAIL |
| 1 | 1 |  |  |  | 1 | 1 | 0 | 1 |  |  |  |  | star start | 未执行 |
| 2（保持 3100 ms） | 0 |  |  |  | 1 | 0 | 1 | 1 |  |  |  |  | delta after 3 s | 未执行 |
| 3 |  | 1 |  |  | 0 | 0 | 0 | 0 |  |  |  |  | stop | 未执行 |

### TC02 overload latch and reset

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 overload latch and reset |
| 所属题目 | C04 Star-Delta Motor Starter（`FB_C04`） |
| 初始状态 | motor stopped |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | overload during delta, fault latch, reset, restart |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'startRisingEdge' |

| 周期 | StartButton | ResetButton | Overload | 预期 MainContactor | 预期 StarContactor | 预期 DeltaContactor | 预期 Fault | 预期 Running | 实际 MainContactor | 实际 StarContactor | 实际 DeltaContactor | 实际 Fault | 实际 Running | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 |  |  | 1 | 1 |  |  |  |  |  |  |  |  | start | FAIL |
| 1（保持 3100 ms） | 0 |  |  | 1 |  | 1 |  |  |  |  |  |  |  | delta | 未执行 |
| 2 |  |  | 1 | 0 | 0 | 0 | 1 | 0 |  |  |  |  |  | overload trip | 未执行 |
| 3 |  | 1 | 0 |  |  |  | 0 |  |  |  |  |  |  | reset | 未执行 |
| 4 | 1 | 0 |  | 1 | 1 |  |  |  |  |  |  |  |  | restart | 未执行 |


## C05 Car Wash Sequence（`FB_C05`）

- 编译：通过；用例通过 0/2；整题未通过

### TC01 full wash sequence

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 full wash sequence |
| 所属题目 | C05 Car Wash Sequence（`FB_C05`） |
| 初始状态 | idle, vehicle present |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | foam, brush, rinse, dry, cycle complete |
| 实际输出及结果 | ❌ 不通过；周期 1：ConveyorMotor 预期 1，实际 False；FoamValve 预期 1，实际 False；周期 2：FoamValve 预期 0，实际 True；BrushMotor 预期 1，实际 False；周期 3：RinseValve 预期 1，实际 False |

| 周期 | StartButton | EmergencyStop | VehiclePresent | ResetButton | 预期 ConveyorMotor | 预期 CycleComplete | 预期 Fault | 预期 FoamValve | 预期 BrushMotor | 预期 RinseValve | 预期 DryFan | 实际 ConveyorMotor | 实际 CycleComplete | 实际 Fault | 实际 FoamValve | 实际 BrushMotor | 实际 RinseValve | 实际 DryFan | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |  |  |  |  | 0 | 0 | 0 |  |  |  |  | reset | PASS |
| 1 | 1 |  | 1 | 0 | 1 | 0 |  | 1 | 0 |  |  | 0 | 0 |  | 0 | 0 |  |  | foam step | FAIL |
| 2（保持 2100 ms） | 0 |  |  |  | 1 |  |  | 0 | 1 |  |  | 1 |  |  | 1 | 0 |  |  | brush step | FAIL |
| 3（保持 2100 ms） |  |  |  |  | 1 |  |  |  | 0 | 1 |  | 1 |  |  |  | 0 | 0 |  | rinse step | FAIL |
| 4（保持 1100 ms） |  |  |  |  | 1 |  |  |  |  | 0 | 1 | 1 |  |  |  |  | 0 | 0 | dry step | FAIL |
| 5（保持 1100 ms） |  |  |  |  | 0 | 1 |  |  |  |  | 0 | 1 | 0 |  |  |  |  | 0 | cycle complete | FAIL |

### TC02 emergency stop and reset

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 emergency stop and reset |
| 所属题目 | C05 Car Wash Sequence（`FB_C05`） |
| 初始状态 | idle |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | emergency during foam, fault latch, reset, restart |
| 实际输出及结果 | ❌ 不通过；周期 0：ConveyorMotor 预期 1，实际 False；FoamValve 预期 1，实际 False；周期 3：ConveyorMotor 预期 0，实际 True |

| 周期 | StartButton | VehiclePresent | ResetButton | EmergencyStop | 预期 ConveyorMotor | 预期 FoamValve | 预期 Fault | 实际 ConveyorMotor | 实际 FoamValve | 实际 Fault | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 |  |  | 1 | 1 | 0 | 0 | 0 | 0 | cycle starts | FAIL |
| 1 | 0 |  |  | 1 | 0 | 0 | 1 | 0 | 0 | 1 | emergency stop | PASS |
| 2 |  |  |  | 0 | 0 |  | 1 | 0 |  | 1 | fault remains latched | PASS |
| 3 |  |  | 1 |  | 0 |  | 0 | 1 |  | 0 | reset | FAIL |
| 4 | 1 |  | 0 |  | 1 | 1 |  | 1 | 1 |  | restart | PASS |


## C06 Elevator Door Control（`FB_C06`）

- 编译：通过；用例通过 0/3；整题未通过

### TC01 open, close by button, limit stop

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 open, close by button, limit stop |
| 所属题目 | C06 Elevator Door Control（`FB_C06`） |
| 初始状态 | door closed |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | open command, open limit, close command, closed limit |
| 实际输出及结果 | ❌ 不通过；周期 2：DoorMotorOpen 预期 0，实际 True；DoorOpen 预期 1，实际 False；周期 4：DoorMotorClose 预期 0，实际 True；DoorClosed 预期 1，实际 False |

| 周期 | OpenButton | CloseButton | ObstacleSensor | DoorOpenLimit | DoorClosedLimit | ResetButton | 预期 DoorMotorOpen | 预期 DoorMotorClose | 预期 DoorClosed | 预期 DoorOpen | 实际 DoorMotorOpen | 实际 DoorMotorClose | 实际 DoorClosed | 实际 DoorOpen | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | closed | PASS |
| 1 | 1 |  |  |  | 0 |  | 1 | 0 |  |  | 1 | 0 |  |  | opening | PASS |
| 2 | 0 |  |  | 1 |  |  | 0 |  | 0 | 1 | 1 |  | 0 | 0 | open limit | FAIL |
| 3 |  | 1 |  | 1 |  |  | 0 | 1 |  |  | 0 | 1 |  |  | closing | PASS |
| 4 |  | 0 |  | 0 | 1 |  |  | 0 | 1 |  |  | 1 | 0 |  | closed limit | FAIL |

### TC02 obstacle reversal and buzzer

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 obstacle reversal and buzzer |
| 所属题目 | C06 Elevator Door Control（`FB_C06`） |
| 初始状态 | door open |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | closing, obstacle, reopen, buzzer |
| 实际输出及结果 | ❌ 不通过；周期 0：DoorOpen 预期 1，实际 False；周期 1：DoorMotorClose 预期 1，实际 False；周期 2：DoorMotorOpen 预期 1，实际 False |

| 周期 | DoorOpenLimit | DoorClosedLimit | ObstacleSensor | CloseButton | 预期 DoorOpen | 预期 DoorMotorClose | 预期 DoorMotorOpen | 预期 WarningBuzzer | 实际 DoorOpen | 实际 DoorMotorClose | 实际 DoorMotorOpen | 实际 WarningBuzzer | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 |  | 1 | 0 |  |  | 0 | 0 |  |  | open | FAIL |
| 1 |  |  |  | 1 |  | 1 | 0 |  |  | 0 | 0 |  | closing | FAIL |
| 2 | 0 |  | 1 |  |  | 0 | 1 | 1 |  | 0 | 0 | 1 | obstacle reverses | FAIL |
| 3 | 1 |  | 0 | 0 | 1 |  | 0 | 0 | 0 |  | 0 | 0 | open limit reached | FAIL |

### TC03 automatic close after 5 s

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 automatic close after 5 s |
| 所属题目 | C06 Elevator Door Control（`FB_C06`） |
| 初始状态 | door open, path clear |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | open door, no commands, auto close timer |
| 实际输出及结果 | ❌ 不通过；周期 0：DoorMotorClose 预期 1，实际 False |

| 周期 | DoorOpenLimit | DoorClosedLimit | OpenButton | CloseButton | ObstacleSensor | 预期 DoorMotorClose | 预期 DoorMotorOpen | 实际 DoorMotorClose | 实际 DoorMotorOpen | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0（保持 5100 ms） | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | auto close starts after 5 s | FAIL |


## C07 Bottle Height Sorting（`FB_C07`）

- 编译：**未通过**（用例记为未通过）；用例通过 0/2；整题未通过

### TC01 accept and reject bottles

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 accept and reject bottles |
| 所属题目 | C07 Bottle Height Sorting（`FB_C07`） |
| 初始状态 | counters zero, conveyor enabled |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | in-range accept, high reject, gate pulse 500 ms |
| 实际输出及结果 | ❌ 不通过；周期 1：AcceptGate 预期 1，实际 False；周期 3：RejectGate 预期 1，实际 False |

| 周期 | RunSwitch | PartPresent | HeightSensor | ResetButton | 预期 ConveyorMotor | 预期 AcceptCount | 预期 RejectCount | 预期 Fault | 预期 AcceptGate | 预期 RejectGate | 实际 ConveyorMotor | 实际 AcceptCount | 实际 RejectCount | 实际 Fault | 实际 AcceptGate | 实际 RejectGate | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 50.0 | 1 | 1 | 0 | 0 | 0 |  |  | 1 | 0 | 0 | 0 |  |  | reset | PASS |
| 1 |  | 1 | 50.0 | 0 | 1 | 1 |  |  | 1 | 0 | 1 | 1 |  |  | 0 | 0 | accept 50 mm | FAIL |
| 2（保持 600 ms） |  | 0 |  |  |  | 1 |  |  | 0 |  |  | 1 |  |  | 0 |  | accept gate retracts | PASS |
| 3 |  | 1 | 70.0 |  |  |  | 1 |  | 0 | 1 |  |  | 1 |  | 0 | 0 | reject 70 mm | FAIL |
| 4（保持 600 ms） |  | 0 |  |  |  |  | 1 |  |  | 0 |  |  | 1 |  |  | 0 | reject gate retracts | PASS |

### TC02 invalid sensor value

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 invalid sensor value |
| 所属题目 | C07 Bottle Height Sorting（`FB_C07`） |
| 初始状态 | counters zero |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | out-of-range sensor latches fault and inhibits gates |
| 实际输出及结果 | ✅ 通过 |

| 周期 | RunSwitch | PartPresent | HeightSensor | ResetButton | 预期 Fault | 预期 ConveyorMotor | 预期 AcceptGate | 预期 RejectGate | 预期 AcceptCount | 预期 RejectCount | 实际 Fault | 实际 ConveyorMotor | 实际 AcceptGate | 实际 RejectGate | 实际 AcceptCount | 实际 RejectCount | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 50.0 | 1 | 0 | 1 |  |  |  |  | 0 | 1 |  |  |  |  | reset | PASS |
| 1 |  | 1 | 150.0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | invalid height | PASS |
| 2 |  |  | 50.0 | 1 | 0 | 1 |  |  | 0 | 0 | 0 | 1 |  |  | 0 | 0 | reset | PASS |


## C08 Greenhouse Irrigation Zones（`FB_C08`）

- 编译：通过；用例通过 0/3；整题未通过

### TC01 dry, wet, dry zones

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 dry, wet, dry zones |
| 所属题目 | C08 Greenhouse Irrigation Zones（`FB_C08`） |
| 初始状态 | idle, zone 1 and 3 dry |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | zone 1 waters, zone 2 skipped, zone 3 waters, complete |
| 实际输出及结果 | ❌ 不通过；周期 0：Zone1Valve 预期 1，实际 False；Pump 预期 1，实际 False；周期 1：Zone3Valve 预期 1，实际 False；Pump 预期 1，实际 False |

| 周期 | StartButton | StopButton | Zone1Moisture | Zone2Moisture | Zone3Moisture | ResetButton | 预期 Zone1Valve | 预期 Pump | 预期 CycleComplete | 预期 Zone2Valve | 预期 Zone3Valve | 实际 Zone1Valve | 实际 Pump | 实际 CycleComplete | 实际 Zone2Valve | 实际 Zone3Valve | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 20.0 | 50.0 | 20.0 | 1 | 1 | 1 | 0 |  |  | 0 | 0 | 0 |  |  | zone 1 starts | FAIL |
| 1（保持 3100 ms） | 0 |  |  |  |  | 0 | 0 | 1 |  | 0 | 1 | 0 | 0 |  | 0 | 0 | zone 2 skipped, zone 3 starts | FAIL |
| 2（保持 3100 ms） |  |  |  |  |  |  |  | 0 | 1 |  | 0 |  | 0 | 1 |  | 0 | cycle complete | PASS |
| 3 |  |  |  |  |  | 1 |  | 0 | 0 |  |  |  | 0 | 0 |  |  | reset complete flag | PASS |

### TC02 all zones wet

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 all zones wet |
| 所属题目 | C08 Greenhouse Irrigation Zones（`FB_C08`） |
| 初始状态 | idle |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | all zones skipped, immediate completion |
| 实际输出及结果 | ❌ 不通过；周期 0：CycleComplete 预期 1，实际 False |

| 周期 | StartButton | Zone1Moisture | Zone2Moisture | Zone3Moisture | 预期 Zone1Valve | 预期 Zone2Valve | 预期 Zone3Valve | 预期 Pump | 预期 CycleComplete | 实际 Zone1Valve | 实际 Zone2Valve | 实际 Zone3Valve | 实际 Pump | 实际 CycleComplete | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 50.0 | 50.0 | 50.0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | all wet, complete immediately | FAIL |

### TC03 stop aborts irrigation

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 stop aborts irrigation |
| 所属题目 | C08 Greenhouse Irrigation Zones（`FB_C08`） |
| 初始状态 | idle |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | stop during zone 1, outputs off, complete cleared |
| 实际输出及结果 | ❌ 不通过；周期 0：Zone1Valve 预期 1，实际 False；Pump 预期 1，实际 False |

| 周期 | StartButton | Zone1Moisture | StopButton | 预期 Zone1Valve | 预期 Pump | 预期 CycleComplete | 实际 Zone1Valve | 实际 Pump | 实际 CycleComplete | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 20.0 |  | 1 | 1 |  | 0 | 0 |  | zone 1 starts | FAIL |
| 1 | 0 |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | stop aborts | PASS |


## C09 Conveyor Zone Accumulation（`FB_C09`）

- 编译：**未通过**（用例记为未通过）；用例通过 0/3；整题未通过

- 仿真器无法执行：期望 ':='，实际是 'MAX_RUN_TIME'

### TC01 normal accumulation

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 normal accumulation |
| 所属题目 | C09 Conveyor Zone Accumulation（`FB_C09`） |
| 初始状态 | line enabled, empty |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | zone 1 moves, zone 1 full, zone 2 moves |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'MAX_RUN_TIME' |

| 周期 | RunSwitch | Zone1Sensor | Zone2Sensor | Zone3Sensor | ReleaseButton | ResetButton | 预期 Zone1Motor | 预期 Zone2Motor | 预期 Zone1Full | 预期 JamAlarm | 预期 Zone2Full | 预期 Zone3Motor | 预期 Zone3Full | 实际 Zone1Motor | 实际 Zone2Motor | 实际 Zone1Full | 实际 JamAlarm | 实际 Zone2Full | 实际 Zone3Motor | 实际 Zone3Full | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |  | zone 1 moves | FAIL |
| 1 |  |  | 1 |  |  | 0 | 0 | 1 | 1 |  | 0 |  |  |  |  |  |  |  |  |  | zone 1 full, zone 2 moves | 未执行 |
| 2 |  |  |  | 1 |  |  |  | 0 |  |  | 1 | 0 | 1 |  |  |  |  |  |  |  | zone 2 full | 未执行 |

### TC02 jam detection and reset

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 jam detection and reset |
| 所属题目 | C09 Conveyor Zone Accumulation（`FB_C09`） |
| 初始状态 | line enabled |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | blocked zone 1 for 5 s, jam alarm, all motors off, reset |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'MAX_RUN_TIME' |

| 周期 | RunSwitch | Zone1Sensor | Zone2Sensor | Zone3Sensor | ReleaseButton | ResetButton | 预期 Zone1Full | 预期 JamAlarm | 预期 Zone1Motor | 预期 Zone2Motor | 实际 Zone1Full | 实际 JamAlarm | 实际 Zone1Motor | 实际 Zone2Motor | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0（保持 5100 ms） | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |  |  |  |  | zone 1 blocked, jam after 5 s | FAIL |
| 1 |  | 0 | 0 |  |  | 1 |  | 0 | 0 | 0 |  |  |  |  | reset and clear sensors | 未执行 |
| 2 |  | 1 |  |  |  | 0 |  | 0 | 1 |  |  |  |  |  | line restarts | 未执行 |

### TC03 release zone 3

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 release zone 3 |
| 所属题目 | C09 Conveyor Zone Accumulation（`FB_C09`） |
| 初始状态 | line enabled |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | release button runs zone 3, blocked zone 3 jams |
| 实际输出及结果 | ⚠️ 未执行；周期 -：解释器不支持: 期望 ':='，实际是 'MAX_RUN_TIME' |

| 周期 | RunSwitch | Zone3Sensor | ReleaseButton | 预期 Zone3Motor | 预期 Zone3Full | 预期 JamAlarm | 实际 Zone3Motor | 实际 Zone3Full | 实际 JamAlarm | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 1 | 1 | 0 | 0 |  |  |  | release runs zone 3 | FAIL |
| 1（保持 5100 ms） |  |  | 0 | 0 | 1 | 1 |  |  |  | zone 3 blocked, jam after 5 s | 未执行 |


## C10 Boiler Purge and Ignition Sequence（`FB_C10`）

- 编译：通过；用例通过 0/3；整题未通过

### TC01 purge, ignition and normal stop

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 purge, ignition and normal stop |
| 所属题目 | C10 Boiler Purge and Ignition Sequence（`FB_C10`） |
| 初始状态 | burner off |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | 3 s purge, 2 s ignition, flame proven, stop |
| 实际输出及结果 | ❌ 不通过；周期 1：PurgeFan 预期 1，实际 False；周期 2：PurgeFan 预期 0，实际 True；Igniter 预期 1，实际 False；周期 3：FuelValve 预期 1，实际 False；FlameOn 预期 1，实际 False |

| 周期 | StartButton | StopButton | EmergencyStop | FlameSensor | ResetButton | 预期 PurgeFan | 预期 Igniter | 预期 FuelValve | 预期 Lockout | 预期 Fault | 预期 FlameOn | 实际 PurgeFan | 实际 Igniter | 实际 FuelValve | 实际 Lockout | 实际 Fault | 实际 FlameOn | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 | 0 |  | reset | PASS |
| 1 | 1 |  |  |  | 0 | 1 | 0 | 0 |  |  |  | 0 | 0 | 0 |  |  |  | purge starts | FAIL |
| 2（保持 3100 ms） | 0 |  |  |  |  | 0 | 1 | 0 |  |  |  | 1 | 0 | 0 |  |  |  | ignition after purge | FAIL |
| 3 |  |  |  | 1 |  |  | 0 | 1 | 0 |  | 1 |  | 0 | 0 | 0 |  | 0 | flame proven | FAIL |
| 4 |  | 1 |  |  |  | 0 | 0 | 0 |  |  | 0 | 1 | 0 | 0 |  |  | 0 | normal stop | FAIL |

### TC02 failed ignition lockout

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 failed ignition lockout |
| 所属题目 | C10 Boiler Purge and Ignition Sequence（`FB_C10`） |
| 初始状态 | burner off |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | purge, ignition window expires, lockout, reset |
| 实际输出及结果 | ❌ 不通过；周期 0：PurgeFan 预期 1，实际 False；周期 1：Igniter 预期 1，实际 False；PurgeFan 预期 0，实际 True；周期 2：Lockout 预期 1，实际 False |

| 周期 | StartButton | FlameSensor | ResetButton | 预期 PurgeFan | 预期 Igniter | 预期 FuelValve | 预期 Lockout | 预期 Fault | 实际 PurgeFan | 实际 Igniter | 实际 FuelValve | 实际 Lockout | 实际 Fault | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 |  | 1 |  |  |  |  | 0 |  |  |  |  | purge | FAIL |
| 1（保持 3100 ms） | 0 |  |  | 0 | 1 |  |  |  | 1 | 0 |  |  |  | ignition | FAIL |
| 2（保持 2100 ms） |  |  |  |  | 0 | 0 | 1 |  |  | 0 | 0 | 0 |  | no flame, lockout | FAIL |
| 3 |  |  | 1 |  |  |  | 0 | 0 |  |  |  | 0 | 0 | reset lockout | PASS |

### TC03 emergency stop latch

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 emergency stop latch |
| 所属题目 | C10 Boiler Purge and Ignition Sequence（`FB_C10`） |
| 初始状态 | burner off |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | emergency during purge, fault latch, reset |
| 实际输出及结果 | ❌ 不通过；周期 0：PurgeFan 预期 1，实际 False；周期 1：PurgeFan 预期 0，实际 True |

| 周期 | StartButton | ResetButton | EmergencyStop | 预期 PurgeFan | 预期 Fault | 预期 Lockout | 实际 PurgeFan | 实际 Fault | 实际 Lockout | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 |  |  | 1 | 0 |  | 0 | 0 |  | purge | FAIL |
| 1 | 0 |  | 1 | 0 | 1 |  | 1 | 1 |  | emergency stop | FAIL |
| 2 |  |  | 0 | 0 | 1 |  | 0 | 1 |  | fault latched | PASS |
| 3 |  | 1 |  |  | 0 | 0 |  | 0 | 0 | reset | PASS |


## C11 Palletizer Layer Counting（`FB_C11`）

- 编译：通过；用例通过 0/1；整题未通过

### TC01 two layers fill a pallet

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 two layers fill a pallet |
| 所属题目 | C11 Palletizer Layer Counting（`FB_C11`） |
| 初始状态 | counts zero |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | three boxes per layer, layer push pulse, full pallet, reset |
| 实际输出及结果 | ❌ 不通过；周期 0：ConveyorMotor 预期 1，实际 False；周期 1：BoxCount 预期 1，实际 0；周期 3：BoxCount 预期 2，实际 1 |

| 周期 | RunSwitch | BoxPresent | ResetButton | 预期 BoxCount | 预期 LayerCount | 预期 ConveyorMotor | 预期 PalletFull | 预期 LayerPush | 实际 BoxCount | 实际 LayerCount | 实际 ConveyorMotor | 实际 PalletFull | 实际 LayerPush | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 |  | 0 | 0 | 0 | 0 |  | reset | FAIL |
| 1 |  | 1 | 0 | 1 |  | 1 |  |  | 0 |  | 1 |  |  | box 1 | FAIL |
| 2 |  | 0 |  | 1 |  |  |  |  | 1 |  |  |  |  | gap | PASS |
| 3 |  | 1 |  | 2 |  |  |  |  | 1 |  |  |  |  | box 2 | FAIL |
| 4 |  | 0 |  | 2 |  |  |  |  | 2 |  |  |  |  | gap | PASS |
| 5 |  | 1 |  | 0 | 1 | 0 |  | 1 | 2 | 0 | 0 |  | 1 | layer 1 push | FAIL |
| 6（保持 1100 ms） |  | 0 |  |  |  | 1 |  | 0 |  |  | 0 |  | 0 | push retracts | FAIL |
| 7 |  | 1 |  | 1 |  |  |  |  | 0 |  |  |  |  | box 4 | FAIL |
| 8 |  | 0 |  | 1 |  |  |  |  | 1 |  |  |  |  | gap | PASS |
| 9 |  | 1 |  | 2 |  |  |  |  | 1 |  |  |  |  | box 5 | FAIL |
| 10 |  | 0 |  | 2 |  |  |  |  | 2 |  |  |  |  | gap | PASS |
| 11 |  | 1 |  | 0 | 2 | 0 | 1 | 1 | 2 | 1 | 0 | 0 | 1 | layer 2 fills pallet | FAIL |
| 12（保持 1100 ms） |  | 0 |  |  |  | 0 | 1 | 0 |  |  | 0 | 1 | 0 | push retracts, pallet remains full | PASS |
| 13 |  |  | 1 | 0 | 0 | 1 | 0 |  | 0 | 0 | 0 | 0 |  | reset pallet | FAIL |


## C12 Safety Light Curtain Muting（`FB_C12`）

- 编译：通过；用例通过 1/3；整题未通过

### TC01 curtain safety stop and reset

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC01 curtain safety stop and reset |
| 所属题目 | C12 Safety Light Curtain Muting（`FB_C12`） |
| 初始状态 | conveyor enabled, curtain clear |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | curtain blocked, safety stop latch, reset when clear |
| 实际输出及结果 | ✅ 通过 |

| 周期 | RunSwitch | LightCurtain | MutingSensor1 | MutingSensor2 | ResetButton | 预期 ConveyorMotor | 预期 SafetyStop | 预期 Alarm | 预期 MutingActive | 实际 ConveyorMotor | 实际 SafetyStop | 实际 Alarm | 实际 MutingActive | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | reset | PASS |
| 1 |  | 1 |  |  | 0 | 0 | 1 |  | 0 | 0 | 1 |  | 0 | curtain blocks | PASS |
| 2 |  | 0 |  |  |  | 0 | 1 |  |  | 0 | 1 |  |  | stop remains latched | PASS |
| 3 |  |  |  |  | 1 | 1 | 0 |  |  | 1 | 0 |  |  | reset while clear | PASS |

### TC02 valid muting sequence

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC02 valid muting sequence |
| 所属题目 | C12 Safety Light Curtain Muting（`FB_C12`） |
| 初始状态 | conveyor enabled, curtain clear |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | sensor 1 then sensor 2, curtain blocked, conveyor runs |
| 实际输出及结果 | ❌ 不通过；周期 3：MutingActive 预期 0，实际 True；ConveyorMotor 预期 0，实际 True；SafetyStop 预期 1，实际 False |

| 周期 | RunSwitch | MutingSensor1 | MutingSensor2 | LightCurtain | ResetButton | 预期 MutingActive | 预期 ConveyorMotor | 预期 SafetyStop | 预期 Alarm | 实际 MutingActive | 实际 ConveyorMotor | 实际 SafetyStop | 实际 Alarm | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 0 |  | 0 | 1 |  |  | 0 | 1 |  |  | sensor 1 armed | PASS |
| 1 |  |  | 1 | 1 |  | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | valid muting | PASS |
| 2 |  | 1 | 1 | 1 |  | 1 | 1 |  |  | 1 | 1 |  |  | muting holds | PASS |
| 3 |  | 0 | 0 | 1 |  | 0 | 0 | 1 |  | 1 | 1 | 0 |  | muting ends, curtain still blocked | FAIL |
| 4 |  |  |  | 0 | 1 |  | 1 | 0 |  |  | 1 | 0 |  | reset | PASS |

### TC03 wrong sequence and muting timeout

| 项目 | 填写内容 |
|---|---|
| 测试用例名称 | TC03 wrong sequence and muting timeout |
| 所属题目 | C12 Safety Light Curtain Muting（`FB_C12`） |
| 初始状态 | conveyor enabled, curtain clear |
| 输入与步骤 | 见下表，每行为一个扫描周期|
| 预期输出 | 见下表“预期”列 |
| 覆盖内容 | sensor 2 first, alarm; sensor 1 alone 2 s, alarm |
| 实际输出及结果 | ❌ 不通过；周期 0：Alarm 预期 1，实际 False；ConveyorMotor 预期 0，实际 True；周期 2：Alarm 预期 1，实际 False；ConveyorMotor 预期 0，实际 True |

| 周期 | RunSwitch | MutingSensor1 | MutingSensor2 | LightCurtain | ResetButton | 预期 Alarm | 预期 ConveyorMotor | 预期 MutingActive | 实际 Alarm | 实际 ConveyorMotor | 实际 MutingActive | 检查内容 | 结果 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 0 |  | 1 | 0 | 0 | 0 | 1 | 0 | sensor 2 without sensor 1 | FAIL |
| 1 |  |  | 0 |  | 1 | 0 | 1 |  | 0 | 1 |  | reset alarm | PASS |
| 2（保持 2100 ms） |  | 1 |  |  | 0 | 1 | 0 |  | 0 | 1 |  | sensor 1 alone times out | FAIL |
| 3 |  | 0 |  |  | 1 | 0 | 1 |  | 0 | 1 |  | reset timeout | PASS |


