import streamlit as st

# 页面设置
st.set_page_config(
    page_title="品牌官网",
    page_icon="⭐",
    layout="centered"
)

# 顶部标题
st.title("品牌名称")
st.markdown("**专业服务 · 值得信赖**")
st.markdown("---")

# 公司简介
st.write("我们专注于提供高品质的服务，致力于为客户创造最大价值。")

# 服务项目
st.subheader("服务项目")

services = [
    {"name": "专业咨询", "desc": "提供专业的行业咨询和解决方案"},
    {"name": "技术支持", "desc": "全面的技术支持和维护服务"},
    {"name": "数据分析", "desc": "深度数据分析和业务洞察"},
    {"name": "定制开发", "desc": "根据需求定制专属解决方案"}
]

for service in services:
    st.write(f"• **{service['name']}** - {service['desc']}")

# 联系方式
st.markdown("---")
st.subheader("联系我们")
st.write("📞 400-123-4567")
st.write("📧 contact@company.com")
st.write("📍 北京市朝阳区xxx街道")

# 底部
st.markdown("---")
st.markdown("<p style='text-align: center; color: #666;'>© 2024 品牌名称 版权所有</p>", unsafe_allow_html=True)
