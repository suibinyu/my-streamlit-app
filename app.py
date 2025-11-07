import streamlit as st

# 页面设置
st.set_page_config(
    page_title="品牌官网",
    page_icon="⭐",
    layout="centered"
)

# 自定义样式
st.markdown("""
<style>
    .main {
        padding: 1rem;
    }
    .header {
        text-align: center;
        padding: 2rem 0;
    }
    .service-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .contact-info {
        text-align: center;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# 顶部标题
st.markdown('<div class="header">', unsafe_allow_html=True)
st.title("品牌名称")
st.markdown("**专业服务 · 值得信赖**")
st.markdown('</div>', unsafe_allow_html=True)

# 公司简介
st.header("关于我们")
st.write("我们专注于提供高品质的服务，致力于为客户创造最大价值。")

# 服务项目
st.header("我们的服务")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    st.subheader("专业咨询")
    st.write("提供专业的行业咨询和解决方案")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    st.subheader("技术支持")
    st.write("全面的技术支持和维护服务")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    st.subheader("数据分析")
    st.write("深度数据分析和业务洞察")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    st.subheader("定制开发")
    st.write("根据需求定制专属解决方案")
    st.markdown('</div>', unsafe_allow_html=True)

# 联系方式
st.header("联系我们")

st.markdown('<div class="contact-info">', unsafe_allow_html=True)
st.write("📞 400-123-4567")
st.write("📧 contact@company.com")
st.write("📍 北京市朝阳区xxx街道")
st.markdown('</div>', unsafe_allow_html=True)

# 底部
st.markdown("---")
st.markdown("<p style='text-align: center; color: #666;'>© 2024 品牌名称 版权所有</p>", unsafe_allow_html=True)
