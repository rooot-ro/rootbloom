import streamlit as st
# from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------- 页面基础全局配置 ----------------------
st.set_page_config(
    page_title="AI赋能校本德育课程开发平台",
    page_icon="🌱",
    layout="wide"
)

# ========== 图片加载【全部注释，云端不读取图片】==========
# banner_img = Image.open("static/banner_rootbloom_grass.png")
# bg_home_img = Image.open("static/bg_home.png")
# bg_subtle_img = Image.open("static/bg_subtle.png")
# perma_img = Image.open("static/perma_model.png")

# 顶部Banner
# st.image(banner_img, use_column_width=True)
st.title("AI赋能校本德育课程开发平台｜PERMA心理积极转化模型")
st.markdown("""
> 本平台面向中小学德育教师，依托PERMA积极心理学模型，结合学校校本特色文化，快速搭建德育课程方案，
> 采集学生心理测评数据，实现课程干预前后心理状态对比，助力学生心理积极转化。
""")
st.divider()

# ========== 【顶部横向标签页导航】 ==========
page_list = [
    "🏠 首页｜项目总介绍",
    "📖 PERMA模型介绍",
    "🏫 校本文化录入",
    "📑 德育课程模板生成",
    "📤 学生基础数据上传",
    "📝 PERMA问卷【前测】",
    "📝 PERMA问卷【后测】",
    "📊 前后测数据对比",
    "ℹ️ 关于本项目"
]
selected_page = st.tabs(page_list)

# ---------------------- 1. 首页｜项目总介绍 ----------------------
with selected_page[0]:
    st.header("🌱 项目简介")
    st.markdown("""
### 项目背景
当前中小学德育工作，经常存在课程模板同质化、难以结合本校特色校本文化、学生心理改变难以量化评估的痛点。
本项目基于PERMA积极心理学模型，打造轻量化德育课程开发工具。

### 平台核心功能
1. 录入学校校本文化，快速生成适配本校的德育课程大纲预览
2. 上传学生基础学情数据，辅助课程内容设计
3. PERMA五维度心理问卷，收集课程干预前、后学生心理数据
4. 自动生成可视化图表，直观展示学生心理积极转化效果

### 适用对象
中小学德育教师、心理老师、校本课程开发团队
""")
    # st.image(bg_home_img, use_column_width=True)

# ---------------------- 2. PERMA积极心理学模型介绍 ----------------------
with selected_page[1]:
    st.header("PERMA积极心理学模型")
    # st.image(perma_img, use_column_width=True)
    st.markdown("""
PERMA是积极心理学的经典模型，包含五大核心维度，用来衡量个体积极心理状态：
- **P 积极情绪（Positive Emotion）**：愉悦、满足、乐观等正向情绪体验
- **E 投入（Engagement）**：全身心投入活动，沉浸其中，忘记时间
- **R 人际关系（Relationships）**：拥有支持性、温暖的师生、同伴关系
- **M 意义（Meaning）**：感受到超越个人的价值、归属感，认同文化与集体
- **A 成就（Accomplishment）**：通过努力完成目标，获得成就感

> 本项目将PERMA模型融入校本德育课程，以课程干预推动学生积极心理转化。
""")

# ----------------------3. 校本文化信息录入 ----------------------
with selected_page[2]:
    st.header("🏫 校本文化信息录入")
    st.markdown("填写学校基础信息与校本文化，作为德育课程设计的基础素材")
    school_name = st.text_input("学校全称")
    school_location = st.text_input("学校所在地")
    school_feature = st.text_area("学校特色 / 校本文化简述")
    school_target = st.text_area("德育育人目标")
    submit_culture = st.button("保存校本文化信息")
    if submit_culture:
        st.success("✅ 校本文化信息已暂存，可前往课程模板页面使用")
        st.session_state["school_name"] = school_name
        st.session_state["school_feature"] = school_feature
        st.session_state["school_target"] = school_target

# ----------------------4. 德育课程模板生成预览 ----------------------
with selected_page[3]:
    st.header("📑 德育课程模板生成预览")
    st.subheader("结合校本文化与PERMA模型，生成德育课程大纲")
    school_name = st.session_state.get("school_name", "")
    school_culture = st.session_state.get("school_feature", "")

    grade = st.selectbox("适用学段", ["小学低段","小学高段","初中"])
    course_hour = st.number_input("课时数量", min_value=1, max_value=10, value=1)
    course_theme = st.text_input("课程主题")

    if st.button("生成课程大纲预览"):
        st.success("✅ 基于PERMA模型生成课程大纲预览")
        st.markdown(f"""
# {school_name}校本德育课程：{course_theme}
适用学段：{grade}｜课时：{course_hour}课时
校本文化背景：{school_culture}

## 课程目标（PERMA五维度）
1. P：引导学生获得积极情绪
2. E：通过校本实践活动提升课堂投入度
3. R：构建良好师生、同伴支持人际关系
4. M：结合校本文化，帮助学生建立价值感与归属感
5. A：设置分层小任务，让学生获得阶段性成就感

## 课程环节
1. 导入：校本文化情境引入
2. 活动体验：小组合作实践
3. 小组分享与反思
4. 课后延伸实践任务
5. 课程评价：PERMA心理前后测评
        """)

# ----------------------5. 学生基础数据上传 ----------------------
with selected_page[4]:
    st.header("📤 上传学生基础情况数据")
    uploaded_file = st.file_uploader("上传学生信息Excel/CSV文件", type=["xlsx","csv"])
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.subheader("上传数据预览")
        st.dataframe(df)
        st.info("💡 说明：学生数据仅用于课程方案参考，不会对外泄露。")
        st.session_state["student_df"] = df

# ----------------------6. PERMA问卷【课程前测】 ----------------------
with selected_page[5]:
    st.header("📝 PERMA心理问卷｜课程前测")
    st.markdown("课程开展之前填写，记录学生初始心理状态")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        p_pre = st.slider("P积极情绪",0,10,5)
    with col2:
        e_pre = st.slider("E投入",0,10,5)
    with col3:
        r_pre = st.slider("R人际关系",0,10,5)
    with col4:
        m_pre = st.slider("M意义",0,10,5)
    with col5:
        a_pre = st.slider("A成就",0,10,5)
    if st.button("保存前测分数"):
        st.session_state["pre"] = [p_pre,e_pre,r_pre,m_pre,a_pre]
        st.success("✅ 前测分数已保存！")

# ----------------------7. PERMA问卷【课程后测】 ----------------------
with selected_page[6]:
    st.header("📝 PERMA心理问卷｜课程后测")
    st.markdown("课程结束后填写，记录干预之后学生心理状态")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        p_post = st.slider("P积极情绪",0,10,6)
    with col2:
        e_post = st.slider("E投入",0,10,6)
    with col3:
        r_post = st.slider("R人际关系",0,10,6)
    with col4:
        m_post = st.slider("M意义",0,10,6)
    with col5:
        a_post = st.slider("A成就",0,10,6)
    if st.button("保存后测分数"):
        st.session_state["post"] = [p_post,e_post,r_post,m_post,a_post]
        st.success("✅ 后测分数已保存！")

# ----------------------8. 前后测数据对比分析 ----------------------
with selected_page[7]:
    st.header("📊 PERMA五维度 前后测对比分析")
    pre_score = st.session_state.get("pre", [5,5,5,5,5])
    post_score = st.session_state.get("post", [6,6,6,6,6])

    labels = ["P积极情绪","E投入","R人际关系","M意义","A成就"]
    fig, ax = plt.subplots(figsize=(10,6))
    x = list(range(len(labels)))
    ax.bar([i-0.2 for i in x], pre_score, width=0.4, label="课程前测")
    ax.bar([i+0.2 for i in x], post_score, width=0.4, label="课程后测")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(0,10)
    ax.legend()
    ax.set_title("PERMA五维度 课程干预前后对比")
    st.pyplot(fig)

# ----------------------9. 关于本项目 ----------------------
with selected_page[8]:
    st.header("ℹ️ 关于本项目")
    st.markdown("""
#### 项目名称
AI赋能校本德育课程开发平台（基于PERMA积极心理模型）

#### 项目简介
本项目面向中小学德育教师，将PERMA积极心理学模型融入校本德育课程开发。
教师录入本校校本文化、学生学情，快速生成德育课程大纲；使用PERMA心理问卷采集前后测数据，可视化展示学生积极心理转化效果。

#### 适用场景
- 学校校本德育课程开发
- 心理健康教育课程干预效果评估
- 教师备课模板工具

#### 项目亮点
✅ 结合校本文化，课程方案不千篇一律
✅ PERMA模型量化心理成长，看得见学生改变
✅ 操作简单，文科教师无需代码基础即可使用
""")
