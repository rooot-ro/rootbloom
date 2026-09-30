import streamlit as st
import pandas as pd
import plotly.express as px
from io import BytesIO

# ============ 图片路径 ============
banner_path = "banner_rootbloom_grass.jpg"
perma_path = "perma_model.jpg"

# ============ 页面基础全局设置 ============
st.set_page_config(
    page_title="从文化符号到品质行为",
    page_icon="🌱",
    layout="wide"
)

# ===================== CSS 样式【顶部固定Banner + 内容卡片浅绿色】 =====================
page_style = """
<style>
/* 整个网页背景：奶油米底色 */
[data-testid="stAppViewContainer"] {
    background-color: #f7f1e3;
}

/* 顶部Banner容器 */
.banner-container {
    width: 100%;
    margin-bottom: 12px;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
}

/* 隐藏原生顶部白条 */
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0) !important;
}

/* 导航栏盒子 */
.nav-container {
    background-color: rgba(255,255,255,0.85);
    padding:14px 18px;
    border-radius:14px;
    margin-bottom:18px;
    box-shadow:0 2px 8px rgba(0,0,0,0.07);
}

/* 内容卡片浅绿色 */
.content-card {
    background-color:#e8f1e4;
    padding:26px;
    border-radius:14px;
    margin-bottom:20px;
    box-shadow:0 3px 10px rgba(0,0,0,0.06);
}
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# ============ 顶部Banner ============
st.markdown("<div class='banner-container'>", unsafe_allow_html=True)
st.image(banner_path, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# ============ 导航栏 ============
st.markdown("<div class='nav-container'>", unsafe_allow_html=True)
page = st.radio(
    "",
    ["首页", "PERMA模型与德育拆分", "AI赋能德育课程", "校本课程案例", "效果评估&成长图表", "学生成长档案记录"],
    horizontal=True
)
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<hr style='border:1px solid #b8c9b3;'>", unsafe_allow_html=True)

# ====================== 首页 ======================
if page == "首页":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.subheader("从文化符号到品质行为｜AI赋能乡村小学乡土德育校本课程项目")
    st.write("本项目面向乡村小学，以PERMA积极心理学模型搭建德育评价框架，结合地方乡土资源，借助AI工具减轻一线教师校本课程开发负担，打造低成本、可迁移、体验式德育课程。项目将传统说教德育转化为实践体验式课堂，把积极心理品质培育融入本土文化学习。")

    st.subheader("项目背景")
    st.write("乡村小学德育普遍存在四大现实难题：①德育内容城市化，缺少贴合本地乡土资源的课程素材；②教师教学任务繁重，独立开发校本德育课程工作量巨大；③德育评价偏向主观描述，缺少可量化、可视化的学生成长追踪工具；④课堂形式以讲授为主，学生参与感弱，德育内化效果不足。")
    st.write("本项目构建一套完整的乡土德育实施体系，依托PERMA五大维度观测学生成长，配套网页工具辅助教师备课、收集前后测数据、建立学生德育成长档案。")

    st.subheader("项目目标")
    st.write("1. 理论目标：将PERMA积极心理模型与小学德育目标深度融合，建立乡土化德育评价框架，实现德育效果可观测、可评估。")
    st.write("2. 课程开发目标：开发一套完整乡土德育校本课程包，包含教案、PPT课件、学生任务单、课堂评价量表。")
    st.write("3. 工具目标：搭建AI辅助备课网页工具，帮助乡村教师快速生成备课提示词，简化德育评价的数据统计，支持批量导入学生档案、一键导出全班记录。")
    st.write("4. 育人目标：引导学生认识家乡文化，培育积极情绪、合作能力、乡土认同感，塑造健全人格，厚植家国情怀。")
    st.markdown("</div>", unsafe_allow_html=True)

# ====================== PERMA模型与德育拆分页面 ======================
elif page == "PERMA模型与德育拆分":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.image(perma_path, use_container_width=True)

    st.subheader("PERMA积极心理模型 —— 德育目标拆解")
    st.write("本项目把PERMA五大核心维度，一一对应小学德育育人目标，把抽象德育概念拆解为课堂可落地、课后可观察评价的成长指标：")

    st.subheader("🌞 P 积极情绪 Positive Emotion｜德育目标：涵养共情、感恩与仁爱之心")
    st.write("育人内涵：引导学生感知自然之美、乡土温情，学会体察他人情绪，拥有感恩、友善、温暖的正向情绪品质。")
    st.write("课堂落地形式：乡土故事品读、家乡自然观察、情绪分享会；课堂评价重点观察学生是否愿意表达感受、共情同伴。")

    st.subheader("🎯 E 投入 Engagement｜德育目标：培养专注、坚持与抗挫品格")
    st.write("育人内涵：学生全身心投入实践任务，在遇到困难时愿意坚持尝试，磨炼耐心、毅力，塑造踏实专注的做事品格。")
    st.write("课堂落地形式：乡土手工、自然探究项目；评价指标：任务专注时长、遇到挫折时的坚持行为。")

    st.subheader("🤝 R 人际关系 Relationships｜德育目标：学会尊重、倾听与团队协作")
    st.write("育人内涵：学会尊重差异、倾听同伴，掌握友善沟通方式，在小组活动中互助包容，建立良好同伴关系。")
    st.write("课堂落地形式：小组研学、集体共创作品；评价重点：小组分工、互助行为、沟通表达。")

    st.subheader("🧭 M 意义 Meaning｜德育目标：建立乡土认同，厚植家国责任感")
    st.write("育人内涵：认识家乡历史、文化与自然，建立文化自信，理解个人与家乡的联结，树立责任意识。")
    st.write("课堂落地形式：地方文化研学、本土民俗探究；评价：学生对本土文化的理解、身份认同感。")

    st.subheader("🏅 A 成就 Accomplishment｜德育目标：塑造自信、勇于挑战的进取精神")
    st.write("育人内涵：学生在课堂实践中获得成就感，敢于展示自我，建立正向自我认知，愿意主动挑战新任务。")
    st.write("课堂落地形式：学生成果展、作品分享；评价：敢于展示、自我肯定、完成任务后的成就感表达。")

    st.subheader("核心逻辑说明")
    st.write("传统德育难以量化评估，本项目用PERMA五个维度作为观测指标，每一节德育课都绑定至少1个维度，课程前后通过问卷采集数据，可视化呈现学生德育成长变化，让德育成果看得见。")
    st.markdown("</div>", unsafe_allow_html=True)

# ====================== AI赋能德育课程【提示词生成器】 ======================
elif page == "AI赋能德育课程":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.subheader("🤖 AI备课提示词生成器")
    st.write("填写课程基础信息，网页自动生成专业提示词，一键复制，粘贴到豆包即可生成针对性完整课程大纲、教案。")

    col1, col2 = st.columns(2)
    with col1:
        grade_sel = st.selectbox("授课年级", ["三年级","四年级","五年级","六年级"])
        perma_dim = st.multiselect("PERMA德育维度（可多选）",["P积极情绪","E投入专注","R人际关系","M意义认同","A成就自信"], default=["P积极情绪","M意义认同"])
    with col2:
        theme_input = st.text_input("乡土课程主题", value="地方乡土文化主题")
        lesson_num = st.number_input("总课时数量", min_value=1,max_value=10,value=2)

    dim_text = ', '.join(perma_dim)
    prompt = f"""
请为小学{grade_sel}设计{lesson_num}课时的乡土德育校本课程，课程主题：{theme_input}。
课程设计必须以PERMA积极心理模型为核心，重点培育以下维度：{dim_text}。

要求输出完整课程大纲，包含：
1.课程设计理念
2.三维教学目标（情感态度、认知、行为）
3.教学重点与教学难点
4.分课时教学设计，每节课写清楚教学环节、时长分配、学生活动、教师引导话术
5.课程评价方案（过程性评价+课后问卷评价，对接PERMA指标）
6.课堂实施注意事项与本土化素材建议

要求：面向乡村小学，体验式德育，拒绝纯说教，内容详实，适合校本课程申报。
"""
    st.subheader("✅ 生成的AI提示词（复制全部文本，粘贴到豆包）")
    st.code(prompt, language="text")
    st.info("💡 使用方法：全选复制上面这段文字，直接发给豆包，就能生成定制化、有深度的课程大纲！")

    st.subheader("🎨 2. AI生成课堂可视化素材")
    st.write("- AI绘制乡土插画、德育主题海报，制作PPT配图，解决乡村学校美术素材不足的痛点。")
    st.write("- 自动生成课堂情景对话脚本，用于德育角色扮演活动，降低教师写脚本的工作量。")

    st.subheader("💬 3. AI课堂互动引导，辅助德育表达")
    st.write("- 课堂上AI作为虚拟伙伴，引导学生分享内心感受，帮助内向学生表达情绪、想法。")
    st.write("- 针对学生发言，给出温和正向引导，启发学生思考感恩、友善、责任等德育主题。")

    st.subheader("⚖️ AI使用伦理原则")
    st.write("教师主导课堂，AI仅作为辅助备课工具；所有AI产出内容，教师必须审核、本地化修改，保证内容贴合小学生认知水平，坚守德育育人主线。")
    st.markdown("</div>", unsafe_allow_html=True)

# ====================== 校本课程案例 ======================
elif page == "校本课程案例":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.subheader("📚 校本德育课程完整案例")
    st.write("整套课程一共8课时，面向小学3-6年级，以PERMA模型作为德育框架，全部围绕地方乡土文化设计体验式德育课。每一节课绑定1~2个PERMA成长维度，以学生实践活动为主。")

    st.subheader("📝 课程整体设计框架")
    st.write("课程固定结构：乡土情景导入 → 沉浸式体验活动 → 小组分享研讨 → 学生作品创作 → 成果展示评价。")
    st.write("评价方式：过程性课堂观察记录 + PERMA前后测问卷 + 学生成长档案，多维度评估德育效果。")

    st.subheader("🗂️ 课程主题示例")
    st.write("**主题1：家乡草木与生命感悟（P积极情绪）** 观察本土植物，感受自然之美，学会感恩；AI生成植物小故事、课堂插图。")
    st.write("**主题2：乡土手作实践（E投入 + R人际关系）** 小组合作制作乡土标本，磨炼耐心，学习互助协作。")
    st.write("**主题3：本土历史故事研学（M意义认同）** 学习地方先辈事迹，了解家乡历史，厚植家国情怀。")
    st.write("**主题4：我的家乡成果展（A成就自信）** 学生展示自己的作品，分享收获，建立自信，获得成就感。")

    st.subheader("🏫 课堂实施流程")
    st.write("乡村教师使用本网页工具，利用提示词快速交给AI生成教案、课件素材；课堂组织学生体验活动，重点观察学生情绪、合作表现，记录德育成长；课程结束收集问卷，录入系统生成成长图表，归档学生成长档案。")
    st.markdown("</div>", unsafe_allow_html=True)

# ====================== 效果评估&成长图表 ======================
elif page == "效果评估&成长图表":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.subheader("📊 PERMA模型｜课程前后测 学生德育心理品质可视化评估")
    st.write("输入课程前测、后测平均分，网页自动生成对比柱状图，直观展示学生五个维度的成长提升。")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("课程前测得分（满分10分）")
        pre_P = st.number_input("P 积极情绪", min_value=0.0, max_value=10.0, value=4.2, step=0.1)
        pre_E = st.number_input("E 投入专注", min_value=0.0, max_value=10.0, value=3.8, step=0.1)
        pre_R = st.number_input("R 人际关系", min_value=0.0, max_value=10.0, value=4.0, step=0.1)
        pre_M = st.number_input("M 意义认同", min_value=0.0, max_value=10.0, value=3.5, step=0.1)
        pre_A = st.number_input("A 成就自信", min_value=0.0, max_value=10.0, value=3.6, step=0.1)

    with col2:
        st.subheader("课程后测得分（满分10分）")
        post_P = st.number_input("P 积极情绪", min_value=0.0, max_value=10.0, value=7.1, step=0.1)
        post_E = st.number_input("E 投入专注", min_value=0.0, max_value=10.0, value=6.8, step=0.1)
        post_R = st.number_input("R 人际关系", min_value=0.0, max_value=10.0, value=7.3, step=0.1)
        post_M = st.number_input("M 意义认同", min_value=0.0, max_value=10.0, value=7.5, step=0.1)
        post_A = st.number_input("A 成就自信", min_value=0.0, max_value=10.0, value=6.9, step=0.1)

    data = pd.DataFrame({
        "PERMA维度": ["积极情绪P", "投入专注E", "人际关系R", "意义认同M", "成就自信A"] * 2,
        "分数": [pre_P, pre_E, pre_R, pre_M, pre_A, post_P, post_E, post_R, post_M, post_A],
        "测试阶段": ["前测","前测","前测","前测","前测","后测","后测","后测","后测","后测"]
    })
    fig = px.bar(data, x="PERMA维度", y="分数", color="测试阶段", barmode="group",
                 range_y=[0,10], title="学生德育心理品质：课程前测 VS 后测对比")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ====================== 学生成长档案记录（批量导入+自动评语+一键导出） ======================
elif page == "学生成长档案记录":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.subheader("📒 学生德育成长档案记录系统")
    st.write("两种录入方式：①单学生手动录入；②全班Excel文档批量上传，自动生成个性化评语，一键导出全班档案")

    # 自动生成评语函数
    def generate_comment(p,e,r,m,a):
        score_list = [("积极情绪",p),("投入专注",e),("人际关系",r),("意义认同",m),("成就自信",a)]
        strong = []
        weak = []
        for name, s in score_list:
            if s >=7:
                strong.append(name)
            if s <=4:
                weak.append(name)
        comment_text = ""
        if len(strong) > 0:
            comment_text += f"优势维度：{','.join(strong)}。该生在这些方面表现突出，能够在乡土课程中展现良好素养。"
        if len(weak) >0:
            comment_text += f"待提升维度：{','.join(weak)}。后续课程可以针对性引导，帮助学生逐步成长。"
        if not strong and not weak:
            comment_text = "各维度表现均衡稳定，继续保持，在乡土文化实践中持续锻炼品质。"
        return comment_text

    # 初始化会话存储
    if "student_df" not in st.session_state:
        st.session_state.student_df = pd.DataFrame(columns=["姓名","班级","积极情绪","投入","人际关系","意义认同","成就","个性化评语"])

    tab1, tab2 = st.tabs(["📥 批量上传全班表格","✍️ 手动新增单个学生"])

    with tab1:
        st.subheader("上传全班Excel/CSV表格")
        st.write("表格表头必须包含：姓名,班级,积极情绪,投入,人际关系,意义认同,成就")
        upload_file = st.file_uploader("上传文件", type=["xlsx","csv"])
        if upload_file is not None:
            try:
                if upload_file.name.endswith(".csv"):
                    df_raw = pd.read_csv(upload_file)
                else:
                    df_raw = pd.read_excel(upload_file)
                # 自动生成评语
                df_raw["个性化评语"] = df_raw.apply(lambda row: generate_comment(row["积极情绪"],row["投入"],row["人际关系"],row["意义认同"],row["成就"]), axis=1)
                st.session_state.student_df = df_raw
                st.success("✅ 文件上传成功！已自动生成每位学生个性化评语")
                st.dataframe(df_raw, use_container_width=True)
            except Exception as err:
                st.error(f"读取文件失败，请检查表头是否正确：{err}")

    with tab2:
        st.subheader("手动录入单个学生信息")
        colA, colB = st.columns(2)
        with colA:
            s_name = st.text_input("学生姓名")
            s_class = st.text_input("班级（例：301）")
            s_p = st.slider("积极情绪",0.0,10.0,5.0,0.1)
            s_e = st.slider("投入",0.0,10.0,5.0,0.1)
        with colB:
            s_r = st.slider("人际关系",0.0,10.0,5.0,0.1)
            s_m = st.slider("意义认同",0.0,10.0,5.0,0.1)
            s_a = st.slider("成就",0.0,10.0,5.0,0.1)
        if st.button("添加到全班档案"):
            new_comment = generate_comment(s_p,s_e,s_r,s_m,s_a)
            new_row = pd.DataFrame({
                "姓名":[s_name],
                "班级":[s_class],
                "积极情绪":[s_p],
                "投入":[s_e],
                "人际关系":[s_r],
                "意义认同":[s_m],
                "成就":[s_a],
                "个性化评语":[new_comment]
            })
            st.session_state.student_df = pd.concat([st.session_state.student_df, new_row], ignore_index=True)
            st.success("✅ 学生档案已添加")

    st.divider()
    st.subheader("全班档案预览 & 一键导出")
    st.dataframe(st.session_state.student_df, use_container_width=True)

    # 导出Excel
    def export_excel(df):
        out = BytesIO()
        with pd.ExcelWriter(out, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="学生成长档案")
        return out.getvalue()

    excel_data = export_excel(st.session_state.student_df)
    st.download_button(
        label="📥 一键下载全班成长档案Excel",
        data=excel_data,
        file_name="学生德育成长档案.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    st.markdown("</div>", unsafe_allow_html=True)