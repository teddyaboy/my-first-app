import matplotlib

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. 页面基本配置
st.set_page_config(page_title="数据分析仪表盘", layout="wide")

# 2. 侧边栏设置
st.sidebar.header("配置选项")
chart_color = st.sidebar.color_picker("选择图表颜色", "#00f900")
data_points = st.sidebar.slider("选择数据点数量", 10, 100, 50)
show_raw_data = st.sidebar.checkbox("显示原始数据表")

# 3. 主界面标题
st.title("📊 交互式数据可视化")
st.markdown(f"当前显示 **{data_points}** 个随机生成的数据点。")

# 4. 生成随机数据
df = pd.DataFrame({
    'x': np.arange(data_points),
    'y': np.random.randn(data_points).cumsum()
})

# 5. 使用 Matplotlib 绘图
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df['x'], df['y'], color=chart_color, marker='o', linestyle='-')
ax.set_title("随机累积走势图")
ax.set_xlabel("时间/索引")
ax.set_ylabel("数值")
ax.grid(True, alpha=0.3)

# 6. 在 Streamlit 中显示图表
st.pyplot(fig)

# 7. 根据侧边栏选项显示数据表
if show_raw_data:
    st.subheader("原始数据预览")
    st.dataframe(df, use_container_width=True)

# 8. 添加一个简单的交互反馈
if st.button("庆祝一下！"):
    st.balloons()
