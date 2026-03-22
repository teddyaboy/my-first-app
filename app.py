import streamlit as st
import pandas as pd

# 1. 添加标题
st.title("我的第一个数据应用 🚀")

# 2. 接收用户输入
name = st.text_input("请输入你的名字", "游客")

# 3. 交互式插件：滑杆
age = st.slider("选择你的年龄", 0, 100, 25)

# 4. 展示逻辑
st.write(f"你好 {name}！你今年 {age} 岁了。")

# 5. 展示图表（直接传入 dataframe 即可）
df = pd.DataFrame({"月份": ["Jan", "Feb", "Mar"], "销售额": [10, 20, 15]})
st.line_chart(df, x="月份", y="销售额")