import streamlit as st
import pandas as pd
import plotly.express as px
from io import BytesIO

# ============ 图片路径 ============
banner_path = "banner_rootbloom_grass.png"
perma_path = "perma_model.png"

# ============ 页面基础全局设置 ============
st.set_page_config(
    page_title="RootBloom｜乡土文化浸润，培育品质行为",
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
    ["首页", "PERMA框架｜品质行为拆解", "AI赋能校本课程开发", "乡土校本课程案例", "品质行为前后对比评估", "学生品质行为成长档案"],
    horizontal=True
)
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<hr style='border:1px solid #b8c9b3;'>", unsafe_allow_html=True)

# ====================== 首页 ======================
if page == "首页":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.subheader("RootBloom｜乡土文化浸润，培育品质行为")
    st.write("本项目立足乡村小学本土校本文化资源，以PERMA模型作为观测框架，将乡土文化学习与学生品质行为培育融合。借助AI降低教师校本课程开发压力，把德育从说教转变为在地文化体验，**追踪、记录学生在乡土实践场景下的品质行为变化**，实现文化浸润、行为育人。")

    st.subheader("项目背景")
    st.write("乡村小学德育普遍存在四大现实难题：①德育素材脱离本土文化，缺少扎根乡土的课程载体；②教师工作量大，独立开发校本德育课程难度高；③德育评价偏主观感受，缺少对**学生真实品质行为**的过程性追踪；④课堂形式以讲授为主，学生缺少实践体验，难以将道德认知转化为稳定行为。")
    st.write("本项目搭建完整校本德育实施体系，依托PERMA五大维度，聚焦学生在乡土课堂中的可观测行为，配套网页工具辅助教师备课、采集课堂行为记录、建立学生品质成长档案，直观呈现文化浸润带来的行为改变。")

    st.subheader("项目目标")
    st.write("1. 理论目标：依托PERMA积极心理学框架，构建**乡土文化场景下的学生品质行为观测体系**，实现德育评价从主观感受转向可观测行为记录。")
    st.write("2. 课程开发目标：开发一套完整乡土校本课程包，包含教案、课堂任务单、行为观察量表，将本土文化资源转化为育人载体。")
    st.write("3. 工具目标：搭建AI辅助备课网页工具，帮助乡村教师快速生成校本课程方案；支持批量录入学生课堂行为记录，可视化展示品质行为成长，一键导出成长档案。")
    st.write("4. 育人目标：依托家乡本土文化浸润，引导学生建立乡土认同，在实践活动中养成友善、专注、合作、自信的良好品质行为。")
    st.markdown("</div>", unsafe_allow_html=True)

# ====================== PERMA框架｜品质行为拆解页面 ======================
elif page == "PERMA框架｜品质行为拆解":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.image(perma_path, use_container_width=True)

    st.subheader("PERMA框架 —— 乡土课程对应的品质行为观测指标")
    st.write("本项目不做抽象心理测试，**每一项维度都对应乡土课堂里可以直接观察到的学生行为**，教师在研学、手作、文化分享等活动中记录表现：")

    st.subheader("🌞 P 积极情绪｜品质行为：共情感恩，友善待人")
    st.write("观测行为：在乡土故事、自然观察活动中，愿意表达感受；能够体会家乡自然与人文之美，懂得感恩；在小组活动中体谅同伴情绪、友善沟通。")
    st.write("课堂场景：本土风物观察、乡土故事品读；教师记录学生情绪表达、共情、友善互助的行为。")

    st.subheader("🎯 E 投入专注｜品质行为：坚持不懈，踏实专注")
    st.write("观测行为：参与乡土手作、标本采集、文化探究任务时，能够持续投入；遇到困难愿意反复尝试，不轻易放弃，磨炼踏实坚韧的行为习惯。")
    st.write("课堂场景：乡土手工、自然探究项目；教师记录学生任务专注度、面对挫折的坚持行为。")

    st.subheader("🤝 R 人际关系｜品质行为：尊重倾听，协作互助")
    st.write("观测行为：小组研学与集体创作时，愿意倾听同伴观点，尊重不同想法；主动分工、互帮互助，友好解决小组内的小矛盾。")
    st.write("课堂场景：乡土研学、集体共创作品；教师观察小组沟通、分工协作、包容互助行为。")

    st.subheader("🧭 M 意义认同｜品质行为：热爱乡土，建立文化自信")
    st.write("观测行为：愿意主动了解家乡历史、本土植物与民俗；愿意向他人讲述家乡故事，珍视本土文化，建立乡土归属感与责任意识。")
    st.write("课堂场景：本土文化研学、乡土文化分享会；教师记录学生对本土文化的探究意愿与表达行为。")

    st.subheader("🏅 A 成就自信｜品质行为：勇于表达，敢于挑战")
    st.write("观测行为：愿意展示自己的乡土作品，主动分享学习收获；面对陌生的文化探究任务敢于尝试，在实践中获得成就感，建立自信。")
    st.write("课堂场景：学生乡土成果展；教师记录学生展示、主动挑战任务的行为表现。")

    st.subheader("核心逻辑说明")
    st.write("传统德育评价偏向主观评语。本项目把德育目标落地到乡土校本课程场景，**以可观察的品质行为作为评价依据**，采集课程前后的行为表现记录，可视化呈现学生行为层面的成长变化，证明乡土文化浸润的育人实效。")
    st.markdown("</div>", unsafe_allow_html=True)

# ====================== AI赋能校本课程开发【提示词生成器】 ======================
elif page == "AI赋能校本课程开发":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.subheader("🤖 AI校本课程提示词生成器")
    st.write("填写课程基础信息，网页自动生成专业提示词，一键复制，粘贴到豆包即可生成完整校本课程教案，配套**课堂品质行为观察量表**。")

    col1, col2 = st.columns(2)
    with col1:
        grade_sel = st.selectbox("授课年级", ["三年级","四年级","五年级","六年级"])
        perma_dim = st.multiselect("重点培育品质行为维度（可多选）",["P共情感恩","E专注坚持","R协作互助","M乡土认同","A自信表达"], default=["P共情感恩","M乡土认同"])
    with col2:
        theme_input = st.text_input("乡土校本课程主题", value="簕杜鹃乡土文化探究")
        lesson_num = st.number_input("总课时数量", min_value=1,max_value=10,value=2)

    dim_text = ', '.join(perma_dim)
    prompt = f"""
请为小学{grade_sel}设计{lesson_num}课时的乡土校本德育课程，课程主题：{theme_input}。
课程设计依托本土乡土文化资源，以PERMA框架为基础，重点培育学生以下品质行为：{dim_text}。

要求输出完整课程大纲，包含：
1.课程设计理念：乡土文化浸润，将文化认知转化为学生品质行为
2.三维教学目标（情感态度、认知、行为目标，重点写可观察学生行为目标）
3.教学重点与教学难点
4.分课时教学设计，每节课写清楚教学环节、时长分配、学生实践活动、教师引导话术
5.配套课堂品质行为观察量表，用于课后记录学生行为表现，对接PERMA行为观测维度
6.课堂实施注意事项与本土化素材建议

要求：面向乡村小学，体验式实践课程，拒绝纯说教，内容详实，适合校本课程申报。
"""
    st.subheader("✅ 生成的AI提示词（复制全部文本，粘贴到豆包）")
    st.code(prompt, language="text")
    st.info("💡 使用方法：全选复制上面这段文字，直接发给豆包，就能生成定制化校本课程+配套行为观察量表！")

    st.subheader("🎨 2. AI生成课堂可视化素材")
    st.write("- AI绘制本土风物插画、乡土文化主题海报，制作PPT配图，解决乡村学校美术素材不足的痛点。")
    st.write("- 自动生成课堂情景对话脚本，用于德育角色扮演活动，降低教师写脚本的工作量。")

    st.subheader("💬 3. AI课堂互动引导，启发文化思考")
    st.write("- 课堂上AI作为虚拟伙伴，引导学生分享家乡见闻，帮助内向学生表达自己对乡土文化的感受。")
    st.write("- 针对学生发言，给出温和正向引导，启发学生思考感恩、合作、乡土责任等品质行为。")

    st.subheader("⚖️ AI使用伦理原则")
    st.write("教师主导课堂，AI仅作为辅助备课工具；所有AI产出内容，教师必须审核、本地化修改，保证内容贴合小学生认知水平，坚守文化育人主线。")
    st.markdown("</div>", unsafe_allow_html=True)

# ====================== 乡土校本课程案例 ======================
elif page == "乡土校本课程案例":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.subheader("📚 乡土校本德育课程完整案例")
    st.write("整套课程一共8课时，面向小学3-6年级，以PERMA行为观测框架为核心，依托河源本土乡土文化设计体验式实践课。每一节课聚焦1~2项品质行为，以学生在地实践活动为主。")

    st.subheader("📝 课程整体设计框架")
    st.write("课程固定结构：乡土情景导入 → 沉浸式文化体验活动 → 小组分享研讨 → 学生作品创作 → 成果展示与行为观察评价。")
    st.write("评价方式：课堂过程性行为观察记录 + 课程前后行为量表 + 学生品质成长档案，多维度评估文化浸润带来的行为改变。")

    st.subheader("🗂️ 课程主题示例")
    st.write("**主题1：家乡草木与生命感悟（P共情感恩）** 观察本土植物，感受自然之美，学会感恩；AI生成植物小故事、课堂插图。重点观察学生共情、表达感恩的行为。")
    st.write("**主题2：乡土手作实践（E专注坚持 + R协作互助）** 小组合作制作乡土标本，磨炼耐心，学习互助协作。重点观察学生坚持、分工互助行为。")
    st.write("**主题3：本土历史故事研学（M乡土认同）** 学习地方先辈事迹，了解家乡历史，厚植家国情怀。重点观察学生探究本土文化、表达乡土认同的行为。")
    st.write("**主题4：我的家乡成果展（A自信表达）** 学生展示自己的乡土作品，分享收获，建立自信，获得成就感。重点观察学生主动展示、敢于表达的行为。")

    st.subheader("🏫 课堂实施流程")
    st.write("乡村教师使用本网页工具，利用提示词快速交给AI生成教案、行为观察量表；课堂组织学生乡土体验活动，重点观察并记录学生品质行为；课程结束录入行为评分，生成可视化对比图表，归档学生品质行为成长档案。")
    st.markdown("</div>", unsafe_allow_html=True)

# ====================== 品质行为前后对比评估 ======================
elif page == "品质行为前后对比评估":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.subheader("📊 学生品质行为｜课程前、课后行为表现对比")
    st.write("填入课程开展前、课程结束后，学生各项品质行为的平均分（满分10分，依据课堂观察打分），网页自动生成对比柱状图，直观展示学生行为成长变化。")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("课程前：行为表现得分（满分10）")
        pre_P = st.number_input("P 共情感恩", min_value=0.0, max_value=10.0, value=4.2, step=0.1)
        pre_E = st.number_input("E 专注坚持", min_value=0.0, max_value=10.0, value=3.8, step=0.1)
        pre_R = st.number_input("R 协作互助", min_value=0.0, max_value=10.0, value=4.0, step=0.1)
        pre_M = st.number_input("M 乡土认同", min_value=0.0, max_value=10.0, value=3.5, step=0.1)
        pre_A = st.number_input("A 自信表达", min_value=0.0, max_value=10.0, value=3.6, step=0.1)

    with col2:
        st.subheader("课程后：行为表现得分（满分10）")
        post_P = st.number_input("P 共情感恩", min_value=0.0, max_value=10.0, value=7.1, step=0.1)
        post_E = st.number_input("E 专注坚持", min_value=0.0, max_value=10.0, value=6.8, step=0.1)
        post_R = st.number_input("R 协作互助", min_value=0.0, max_value=10.0, value=7.3, step=0.1)
        post_M = st.number_input("M 乡土认同", min_value=0.0, max_value=10.0, value=7.5, step=0.1)
        post_A = st.number_input("A 自信表达", min_value=0.0, max_value=10.0, value=6.9, step=0.1)

    data = pd.DataFrame({
        "品质行为维度": ["共情感恩P", "专注坚持E", "协作互助R", "乡土认同M", "自信表达A"] * 2,
        "行为得分": [pre_P, pre_E, pre_R, pre_M, pre_A, post_P, post_E, post_R, post_M, post_A],
        "阶段": ["课程前","课程前","课程前","课程前","课程前","课程后","课程后","课程后","课程后","课程后"]
    })
    fig = px.bar(data, x="品质行为维度", y="行为得分", color="阶段", barmode="group",
                 range_y=[0,10], title="乡土校本课程实施｜学生品质行为前后对比")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ====================== 学生品质行为成长档案（批量导入+自动评语+一键导出） ======================
elif page == "学生品质行为成长档案":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.subheader("📒 学生品质行为成长档案记录系统")
    st.write("教师基于乡土课堂观察，记录学生品质行为表现。支持两种录入方式：①单个学生手动录入；②全班表格批量上传，自动生成**围绕乡土课程行为表现**的个性化评语，一键导出全班档案。")

    # 自动生成评语函数：全部改成品质行为描述，绑定校本乡土课程
    def generate_comment(p,e,r,m,a):
        score_list = [("共情感恩",p),("专注坚持",e),("协作互助",r),("乡土认同",m),("自信表达",a)]
        strong = []
        weak = []
        for name, s in score_list:
            if s >=7:
                strong.append(name)
            if s <=4:
                weak.append(name)
        comment_text = ""
        if len(strong) > 0:
            comment_text += f"优势行为：{','.join(strong)}。在乡土校本课程实践中，该生在以上方面表现突出，能够在本土文化探究活动中展现良好行为品质。"
        if len(weak) >0:
            comment_text += f"待提升行为：{','.join(weak)}。后续乡土课程中可以针对性引导，持续锻炼该生的相关行为习惯。"
        if not strong and not weak:
            comment_text = "各项品质行为表现均衡稳定，继续在乡土文化实践活动中持续成长，加深对家乡文化的理解。"
        return comment_text

    # 初始化会话存储
    if "student_df" not in st.session_state:
        st.session_state.student_df = pd.DataFrame(columns=["姓名","班级","共情感恩","专注坚持","协作互助","乡土认同","自信表达","个性化行为评语"])

    tab1, tab2 = st.tabs(["📥 批量上传全班表格","✍️ 手动新增单个学生"])

    with tab1:
        st.subheader("上传全班Excel/CSV行为记录表")
        st.write("表格表头必须包含：姓名,班级,共情感恩,专注坚持,协作互助,乡土认同,自信表达")
        upload_file = st.file_uploader("上传文件", type=["xlsx","csv"])
        if upload_file is not None:
            try:
                if upload_file.name.endswith(".csv"):
                    df_raw = pd.read_csv(upload_file)
                else:
                    df_raw = pd.read_excel(upload_file)
                # 自动生成行为评语
                df_raw["个性化行为评语"] = df_raw.apply(lambda row: generate_comment(row["共情感恩"],row["专注坚持"],row["协作互助"],row["乡土认同"],row["自信表达"]), axis=1)
                st.session_state.student_df = df_raw
                st.success("✅ 文件上传成功！已自动生成每位学生的品质行为评语")
                st.dataframe(df_raw, use_container_width=True)
            except Exception as err:
                st.error(f"读取文件失败，请检查表头是否正确：{err}")

    with tab2:
        st.subheader("手动录入单个学生课堂行为记录")
        colA, colB = st.columns(2)
        with colA:
            s_name = st.text_input("学生姓名")
            s_class = st.text_input("班级（例：301）")
            s_p = st.slider("共情感恩",0.0,10.0,5.0,0.1)
            s_e = st.slider("专注坚持",0.0,10.0,5.0,0.1)
        with colB:
            s_r = st.slider("协作互助",0.0,10.0,5.0,0.1)
            s_m = st.slider("乡土认同",0.0,10.0,5.0,0.1)
            s_a = st.slider("自信表达",0.0,10.0,5.0,0.1)
        if st.button("添加到全班成长档案"):
            new_comment = generate_comment(s_p,s_e,s_r,s_m,s_a)
            new_row = pd.DataFrame({
                "姓名":[s_name],
                "班级":[s_class],
                "共情感恩":[s_p],
                "专注坚持":[s_e],
                "协作互助":[s_r],
                "乡土认同":[s_m],
                "自信表达":[s_a],
                "个性化行为评语":[new_comment]
            })
            st.session_state.student_df = pd.concat([st.session_state.student_df, new_row], ignore_index=True)
            st.success("✅ 学生行为档案已添加")

    st.divider()
    st.subheader("全班品质行为档案预览 & 一键导出")
    st.dataframe(st.session_state.student_df, use_container_width=True)

    # 导出Excel
    def export_excel(df):
        out = BytesIO()
        with pd.ExcelWriter(out, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="学生品质行为成长档案")
        return out.getvalue()

    if not st.session_state.student_df.empty:
        excel_data = export_excel(st.session_state.student_df)
        st.download_button(
            label="📥 一键下载全班品质行为档案Excel",
            data=excel_data,
            file_name="学生品质行为成长档案.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    st.markdown("</div>", unsafe_allow_html=True)
