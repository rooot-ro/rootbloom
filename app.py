import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import base64

# ========== 工具函数：图片转base64，用于网页背景图 ==========
def img_to_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ========== 页面全局基础配置 ==========
st.set_page_config(
    page_title="PERMA德育课程开发平台",
    page_icon="🌱",
    layout="wide"
)

# ========== 加载图片资源，请确认static文件夹内文件名和下面完全对应 ==========
banner_img = Image.open("static/banner_rootbloom_grass.png")
bg_home_b64 = img_to_base64("static/bg_home.png")
bg_subtle_b64 = img_to_base64("static/bg_subtle.png")
perma_img = Image.open("static/perma_model.png")

# ========== 侧边导航菜单 ==========
menu = st.sidebar.radio(
    "📋 功能导航栏",
    [
        "首页介绍｜PERMA模型",
        "教师课程大纲生成",
        "学生问卷录入",
        "前后测对比图表"
    ]
)

# ========== 页面背景CSS ==========
if menu == "首页介绍｜PERMA模型":
    page_css = f"""
    <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bg_home_b64}");
            background-size: cover;
            background-attachment: fixed;
        }}
        .block-container {{
            background-color: rgba(255,255,255,0.82);
            padding: 2rem;
            border-radius:12px;
        }}
    </style>
    """
else:
    page_css = f"""
    <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bg_subtle_b64}");
            background-size: cover;
            background-attachment: fixed;
        }}
        .block-container {{
            background-color: rgba(255,255,255,0.85);
            padding: 2rem;
            border-radius:12px;
        }}
    </style>
    """
st.markdown(page_css, unsafe_allow_html=True)

# ========== 顶部Banner横幅（已修复参数 use_container_width） ==========
st.image(banner_img, use_container_width=True)

# ===================== 板块1：首页介绍｜PERMA模型 =====================
if menu == "首页介绍｜PERMA模型":
    st.header("🌱 AI赋能校本德育课程开发平台")
    st.subheader("理论基础：PERMA积极心理学模型")

    st.markdown("""
PERMA模型用于追踪学生德育课程中心理积极转化，包含五大维度：
- **P（Positive Emotions）积极情绪**：正向愉悦感、自豪感
- **E（Engagement）投入**：沉浸式参与课程与实践活动
- **R（Relationships）人际关系**：同伴互助、良好的校园联结
- **M（Meaning）意义感**：理解校本文化，建立自我价值认同
- **A（Accomplishment）成就**：完成任务，获得成长成就感
    """)

    st.image(perma_img, caption="PERMA积极心理学模型示意图", use_container_width=True)

    st.info("""
💡 项目简介
面向中小学德育教师：教师填写校本文化、学生学情信息，平台基于PERMA框架生成标准化德育课程大纲；录入学生PERMA问卷前后测数据，自动生成可视化对比图表，直观观察学生心理积极转化效果。
    """)

# ===================== 板块2：教师课程大纲生成 =====================
elif menu == "教师课程大纲生成":
    st.header("📑 校本德育课程大纲生成模板")
    st.write("请填写学校校本文化、学生学情，平台自动生成PERMA框架下的课程大纲预览")

    school_name = st.text_input("🏫 学校名称")
    school_culture = st.text_area("🎋 校本文化简述（例：竹子文化、簕杜鹃红色文化）")
    student_condition = st.text_area("👧👦 班级学生学情描述")
    course_theme = st.text_input("📖 本次德育课程主题")

    if st.button("生成PERMA德育课程大纲"):
        st.success("✅ 大纲生成完成，下方预览")
        st.subheader("【PERMA框架 · 校本德育课程方案】")
        outline_content = f"""
# 《{course_theme}》德育课程方案
> 依托校本文化：{school_culture}
> 面向学情：{student_condition}

## 一、课程目标（PERMA五维目标）
1. P积极情绪：引导学生感受本土校本文化，产生文化自信与愉悦感
2. E投入：以项目式学习，让学生深度参与文化探究实践
3. R人际关系：小组合作探究，培养沟通协作、互助包容的品质
4. M意义感：读懂校本文化内涵，建立个人价值与校园文化的联结
5. A成就：完成课程实践作品，收获成长，获得正向成就感

## 二、课程实施流程
1. 课程导入：校本文化故事、校园场景引入主题
2. 探究学习：小组项目式任务，自主调研文化内容
3. 实践活动：校园文化主题实践、手工/宣讲/研学等活动
4. 反思记录：学生撰写感悟、课堂分享
5. 课程评价：PERMA五维度问卷前测+后测，评估心理成长

## 三、评价方式
课程开展前发放PERMA问卷【前测】→开展德育课程→课程结束发放【后测】，对比学生积极心理转化效果。
        """
        st.markdown(outline_content)
        st.download_button(
            label="📥 导出大纲为文本文件",
            data=outline_content,
            file_name=f"{school_name}_PERMA德育课程大纲.txt",
            mime="text/plain"
        )

# ===================== 板块3：学生问卷录入 =====================
elif menu == "学生问卷录入":
    st.header("📝 PERMA学生问卷数据录入面板")
    st.write("录入同一批学生课程【前测】、【后测】五个维度得分，保存数据用于图表对比")

    col_left, col_right = st.columns(2)
    with col_left:
        st.subheader("📌 课程前测得分（上课之前）")
        p_pre = st.number_input("P 积极情绪", min_value=0, max_value=10, value=5)
        e_pre = st.number_input("E 投入", min_value=0, max_value=10, value=5)
        r_pre = st.number_input("R 人际关系", min_value=0, max_value=10, value=5)
        m_pre = st.number_input("M 意义感", min_value=0, max_value=10, value=5)
        a_pre = st.number_input("A 成就", min_value=0, max_value=10, value=5)

    with col_right:
        st.subheader("📌 课程后测得分（课程结束后）")
        p_post = st.number_input("P 积极情绪", min_value=0, max_value=10, value=5)
        e_post = st.number_input("E 投入", min_value=0, max_value=10, value=5)
        r_post = st.number_input("R 人际关系", min_value=0, max_value=10, value=5)
        m_post = st.number_input("M 意义感", min_value=0, max_value=10, value=5)
        a_post = st.number_input("A 成就", min_value=0, max_value=10, value=5)

    survey_df = pd.DataFrame({
        "PERMA维度": ["P积极情绪", "E投入", "R人际关系", "M意义感", "A成就"],
        "前测得分": [p_pre, e_pre, r_pre, m_pre, a_pre],
        "后测得分": [p_post, e_post, r_post, m_post, a_post]
    })
    st.session_state["survey_data"] = survey_df

    st.subheader("📋 录入数据预览表")
    st.dataframe(survey_df, use_container_width=True)
    st.success("✅ 数据已临时保存，可前往【前后测对比图表】页面绘图")

# ===================== 板块4：前后测对比图表 =====================
elif menu == "前后测对比图表":
    st.header("📊 PERMA五维度 前后测心理转化对比图")
    st.write("读取问卷录入数据，自动生成柱状对比图，观察学生心理成长变化")

    if "survey_data" in st.session_state:
        chart_df = st.session_state["survey_data"]
        fig, ax = plt.subplots(figsize=(11, 5.5))
        x_axis = list(range(len(chart_df["PERMA维度"])))
        bar_width = 0.35

        bar1 = ax.bar([i - bar_width/2 for i in x_axis], chart_df["前测得分"], bar_width, label="课程前测", color="#73b873")
        bar2 = ax.bar([i + bar_width/2 for i in x_axis], chart_df["后测得分"], bar_width, label="课程后测", color="#2d7d46")

        ax.set_xticks(x_axis)
        ax.set_xticklabels(chart_df["PERMA维度"])
        ax.set_ylabel("得分（0~10分）")
        ax.set_title("PERMA模型｜德育课程前后测得分对比", fontsize=14)
        ax.legend()
        ax.set_ylim(0, 10)

        for bar in bar1:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.1, f"{height}", ha="center")
        for bar in bar2:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.1, f"{height}", ha="center")

        st.pyplot(fig)
        st.info("📖图表解读：后测分数高于前测，代表学生在该维度出现积极心理转化，德育干预有效果。")
    else:
        st.warning("⚠️ 暂无问卷数据！请先切换到【学生问卷录入】页面填写数据。")
