import streamlit as st
import pandas as pd
import numpy as np

# 设置页面配置
st.set_page_config(
    page_title="我的微信公众号应用",
    page_icon="🚀",
    layout="wide"
)

# 应用标题
st.title("🚀 欢迎使用我们的微信公众号应用")
st.markdown("---")

# 侧边栏
with st.sidebar:
    st.header("导航菜单")
    menu_option = st.selectbox(
        "选择功能",
        ["首页", "产品展示", "服务介绍", "联系我们"]
    )

# 根据选择显示不同内容
if menu_option == "首页":
    st.header("公司简介")
    st.write("我们是一家专业的科技公司，致力于为客户提供最优质的服务。")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("我们的优势")
        st.write("• 专业团队")
        st.write("• 多年经验")
        st.write("• 客户至上")
    
    with col2:
        st.subheader("核心价值")
        st.write("• 创新")
        st.write("• 诚信")
        st.write("• 卓越")

elif menu_option == "产品展示":
    st.header("产品展示")
    
    # 示例数据
    products = {
        "产品名称": ["产品A", "产品B", "产品C", "产品D"],
        "价格": [299, 399, 499, 599],
        "评分": [4.5, 4.2, 4.8, 4.0]
    }
    
    df = pd.DataFrame(products)
    st.dataframe(df, use_container_width=True)
    
    # 图表展示
    st.subheader("产品评分图表")
    st.bar_chart(df.set_index("产品名称")["评分"])

elif menu_option == "服务介绍":
    st.header("我们的服务")
    
    services = st.columns(3)
    
    with services[0]:
        st.info("**专业咨询**")
        st.write("提供专业的行业咨询和解决方案")
    
    with services[1]:
        st.success("**技术支持**")
        st.write("全面的技术支持和维护服务")
    
    with services[2]:
        st.warning("**定制开发**")
        st.write("根据需求定制专属解决方案")

elif menu_option == "联系我们":
    st.header("联系我们")
    
    with st.form("contact_form"):
        st.subheader("留言咨询")
        name = st.text_input("姓名")
        email = st.text_input("邮箱")
        message = st.text_area("留言内容")
        
        submitted = st.form_submit_button("提交")
        if submitted:
            if name and email and message:
                st.success("感谢您的留言！我们会尽快回复。")
            else:
                st.error("请填写所有必填字段")

# 页脚
st.markdown("---")
st.markdown("© 2024 我的公司 - 版权所有")