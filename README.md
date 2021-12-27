#新型冠状病毒疫情数据分析 

本项目用于对新冠疫情进行数据分析，对其进行数据可视化操作，并使用SIR预测模型对未来的疫情数据进行预测。



## 数据说明

本项目所获得的数据是由新型冠状病毒疫情爬虫所得。

其中部分API数据已于2020年停止更新。

| 文件名                | 数据开始时间 | 数据结束时间 |
| --------------------- | ------------ | ------------ |
| foreign.csv           | 2020.1.28    | 2021.8.31    |
| 各洲的数据.csv        | 2020.3.1     | 2020.12.31   |
| japandata.csv         | 停止更新     | 停止更新     |
| indiandata.csv        | 停止更新     | 停止更新     |
| chinadailyconfirm.csv | 仍在更新     | 仍在更新     |

## 函数功能说明

**部分函数由于数据缺失暂时无法使用**

**部分函数命名不规范**

**这些问题将在未来解决**

****

### 获取数据

```python
# 获取部分国家数据
def crawlsomecountry()
```

```python
# 获取各大洲数据
def crawleverycontinent()
```

```python
# 获取中国每日数据
def CrawlChinadata()
```

```python
# 获取日本数据
def crawljapan()
```

```python
# 获取印度数据
def crawlindian()
```

```python
# 排名
def crawl5()
```

### 数据处理及可视化

```python
# 处理各洲数据、绘图（所有）
def dealcontinentdata()
```

```python
# 处理各洲数据、绘图（三月份）
def dealcontinentdatathree()
```

```python
# 联合国五大国绘图（所有）
def dealwithfivecountry()
```

```python
# 联合国五大国绘图（三月）
def dealwithfivecountrythree()
```

```python
# 亚洲地区处理
def dealwithAsian()
```

```python
# 世界当日数据
def run4()
```

```python
# 死亡率全球(除中国)
def dealwithdeadrate()
```

```python
# 死亡率五常
def dealwithdeadratefivecountry()
```

```python
# 治愈率降序全球（除中国）
def dealwithhealrate()
```

```python
# 治愈率降序五常
def dealwithhealratefivecountry()
```

```python
# 中国城市每日新增
def chinacity()
```

```python
# 浙江省城市关系
def chinacities()
```

## 运行结果 

测试程序的运行结果在“运行结果”文件夹中显示

SIR模型在这一版本中不展示



## 贡献代码

由于程序存在很多没有改进的地方，极力欢迎各位对程序进行改进。 

对于重大更改，请先打开一个issue，讨论想要更改的内容。

1.Fork本项目，点击右上角的Fork按键即可。

2.上传文件到已有文件夹：打开对应文件夹，点击Download按钮旁的upload，上传你的文件。

3.上传文件到新文件夹：打开任意文件夹，点击Download按钮旁的upload，把浏览器地址栏中文件夹名称改为你想要新建的文件夹名称，然后回车，上传你的文件。

4. 提交 PR：上传完文件到个人仓库之后，点击 Pull Request 即可。请留意一下项目的文件组织。

5. 也可以直接附加在 Issue 中，由维护者进行添加。

 请确保根据需要更新测试。 





