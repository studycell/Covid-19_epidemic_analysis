# Covid-19 epidemic data analysis

This project is used to analyze the data of the Covid-19 epidemic, perform data visualization operations on it, and use the SIR prediction model to predict future epidemic data.



##  Data Description

The data obtained in this project is derived from the Covid-19 epidemic crawler.

Some of the API which provides the data have stopped updating in 2020.

| File name             | Data start time  | Data end time    |
| --------------------- | ---------------- | ---------------- |
| foreign.csv           | 2020.1.28        | 2021.8.31        |
| 各洲的数据.csv        | 2020.3.1         | 2020.12.31       |
| japandata.csv         | stopped updating | stopped updating |
| indiandata.csv        | stopped updating | stopped updating |
| chinadailyconfirm.csv | still updating   | still updating   |

## Function Description

**Some functions are temporarily unavailable due to missing data**

**Some functions are not properly named**

**these problems will be solved in the future**

### Get Data

```python
# 处理各洲数据、绘图（所有）
def dealcontinentdata()
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

## Running Results

The running results of the test program are displayed in the "运行结果" folder

SIR model is not shown in this version

## Contributing

As there are many areas that have not been improved in the program, I strongly welcome everyone to improve the program.

For major changes, please open an issue first to discuss what you want to change.

Make sure to update the test as needed.

