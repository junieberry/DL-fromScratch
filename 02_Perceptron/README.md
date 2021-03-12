## 2장 퍼셉트론
### 2.1 퍼셉트론이란?
**퍼셉트론**은 다수의 신호를 입력으로 받아 하나의 신호를 출력한다.

![01. 퍼셉트론 - Perceptron](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F99BDCE4D5B98A1022C)

입력 신호가 뉴런에 보내질 때는 각각 고유한 가중치가 곱해지는데, 이때 뉴런에서 보내온 신호의 총합이 정해진 한계를 넘어설 때만 1을 출력한다.

**가중치**는 각 입력 신호가 결과에 미치는 영향력을 의미한다.

### 2.2 단순한 논리게이트

#### 2.2.1 AND 게이트
  
| $x_1$  |$x_2$|$y$|
|--|--|--|
|  0|0  |0
|0|1|0|
|1|0|0|
|1|1|1

#### 2.2.2 NAND 게이트와 OR 게이트

NAND 게이트는 Not AND를 의미한다.

| $x_1$  |$x_2$|$y$|
|--|--|--|
|  0|0  |1
|0|1|1|
|1|0|1|
|1|1|0

### 2.4 퍼셉트론의 한계
#### 2.4.1 XOR 게이트
XOR 게이트는 배타적 논리합이라는 논리 회로이다.
| $x_1$  |$x_2$|$y$|
|--|--|--|
|  0|0  |0
|0|1|1|
|1|0|1|
|1|1|0

이때 XOR 게이트는 AND, NAND, OR 과는 달리 하나의 퍼셉트론으로 구현할 수 없다.

### 2.5 다층 퍼셉트론

이처럼 단층 퍼셉트론으로는 비선형 영역을 분리할 수 없다. 이를 해결하기 위해 퍼셉트론의 층을 쌓아 **다층 퍼셉트론**으로 구현한다.

![NPN Transistor XOR Gate Circuit | Sully Station Technologies](https://lh3.googleusercontent.com/proxy/Sds2vbRqDDPFUgb2Szlkl2Xcjj4GP6w0wxIOLo0ZizCXzUvA-lKcgwCS3vz2n-nw-vOfeaGHnIM1gD-6nppSQusxcrqQIl_InGc9LQ)



> Written with [StackEdit](https://stackedit.io/).
