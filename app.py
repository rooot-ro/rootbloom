import streamlit as st
import pandas as pd
import plotly.express as px
from io import BytesIO
import os

# ============ 图片路径 ============
banner_path = "banner_rootbloom_grass.png"
perma_path = "perma_model.png"

# ============ 页面基础全局设置 ============
st.set_page_config(
    page_title="乡土文化浸润，培育品质行为",
    page_icon="🌱",
    layout="wide"
)

# ===================== CSS 样式 =====================
page_style = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f7f1e3;
}
.banner-text-title{
    font-size:34px;
    font-weight:bold;
    text-align:center;
    color:#2c4227;
    padding:24px;
    background:#d8e9d2;
    border-radius:14px;
    margin-bottom:12px;
}
/* 隐藏原生顶部白条 */
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0) !important;
}
.nav-container {
    background-color: rgba(255,255,255,0.85);
    padding:14px 18px;
    border-radius:14px;
    margin-bottom:18px;
    box-shadow:0 2px 8px rgba(0,0,0,0.07);
}
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

# ============ 顶部Banner 容错处理 ============
if os.path.exists(banner_path):
    st.image(banner_path, use_container_width=True)
else:
    st.markdown("<div class='banner-text-title'>乡土文化浸润，培育品质行为</div>", unsafe_allow_html=True)

# ============ 导航栏 ============
st.markdown("<div class='nav-container'>", unsafe_allow_html=True)
page = st.radio(
    "",
    ["首页", "PERMA框架｜品质行为拆解", "AI赋能校本课程开发", "乡土校本课程案例", "品质行为前后对比评估", "学生品质行为成长档案"],
    horizontal=True
)
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<hr style='border:1px solid #b8c9b3'>", unsafe_allow_html=True)

# ====================== 首页 ======================
if page == "首页":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.subheader("乡土文化浸润，培育品质行为")
    st.write("本项目立足乡村小学本土校本文化资源，以PERMA模型作为观测框架，将乡土文化学习与学生品质行为培育融合。借助AI降低教师校本课程开发压力，把德育从说教转变为在地文化体验，追踪、记录学生在乡土实践场景下的品质行为变化，实现文化浸润、行为育人。")

    st.subheader("项目背景")
    st.write("乡村小学德育普遍存在四大现实困境：①德育素材脱离本土文化，缺少扎根乡土的课程载体；②教师日常工作量大，独立开发校本德育课程难度高；③德育评价偏向主观感受，缺少对学生真实品质行为的过程性追踪；④课堂以讲授为主，缺少实践体验，道德认知很难转化为稳定行为习惯。")
    st.write("本项目搭建完整校本德育实施体系，依托PERMA五大维度，聚焦学生在乡土课堂中可观测行为表现；配套网页工具辅助教师备课、采集课堂行为记录，建立学生品质成长档案，直观呈现文化浸润带来的行为改变。")

    st.subheader("项目目标")
    st.write("1. 理论目标：依托PERMA框架，构建乡土文化场景下学生品质行为观测体系，推动德育评价由主观感受转向可观测行为记录。")
    st.write("2. 课程开发目标：产出完整乡土校本课程包，包含教案、课堂任务单、行为观察量表；依托乡土实践落实义务教育核心素养，把本土文化资源转化为育人载体。")
    st.write("3. 工具目标：搭建AI辅助备课模块，支持批量录入课堂行为记录，可视化品质行为成长数据，一键导出学生成长档案。")
    st.write("4. 育人目标：依托家乡本土文化浸润，帮助学生建立乡土认同，在实践中养成友善、专注、协作、自信的品质行为。")
    st.markdown("</div>", unsafe_allow_html=True)

# ====================== PERMA框架｜品质行为拆解 ======================
elif page == "PERMA框架｜品质行为拆解":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    # 图片容错
    if os.path.exists(perma_path):
        st.image(perma_path, use_container_width=True)
    else:
        st.info("📌 PERMA品质行为观测框架示意图（图片暂未上传，不影响全部功能）")

    st.subheader("PERMA框架 —— 乡土课程对应的品质行为观测指标")
    st.write("本项目不做抽象心理测评，每一个维度对应乡土课堂中教师可以直接观察到的学生行为，在研学、手作、文化分享活动现场完成记录。")

    st.subheader("🌞 P 积极情绪｜品质行为：共情感恩，友善待人")
    st.write("观测行为：乡土故事、自然观察活动愿意表达内心感受；感受家乡人文风物之美，心怀感恩；小组活动体谅同伴情绪，友善沟通。")
    st.write("课堂场景：本土风物观察、乡土故事品读，记录学生共情表达、友善互助行为。")

    st.subheader("🎯 E 投入专注｜品质行为：坚持不懈，踏实专注")
    st.write("观测行为：参与乡土手作、标本采集、文化探究时可以持续投入；遇到困难愿意反复尝试，不轻易放弃，养成坚韧踏实习惯。")
    st.write("课堂场景：乡土手工、自然探究，记录专注度、面对挫折时的坚持表现。")

    st.subheader("🤝 R 人际关系｜品质行为：尊重倾听，协作互助")
    st.write("观测行为：小组研学、集体创作时倾听同伴想法，尊重不同意见；主动分工协作，友好化解小组矛盾。")
    st.write("课堂场景：乡土研学、集体创作，观察沟通、分工、包容互助行为。")

    st.subheader("🧭 M 意义认同｜品质行为：热爱乡土，建立文化自信")
    st.write("观测行为：主动了解家乡历史、本土植物民俗；愿意向他人讲述家乡故事，建立乡土归属感与责任意识。")
    st.write("课堂场景：本土文化研学、乡土分享会，记录探究意愿与文化表达行为。")

    st.subheader("🏅 A 成就感知｜品质行为：勇于表达，敢于挑战")
    st.write("观测行为：敢于展示自己的乡土作品，主动分享收获；面对陌生的文化探究任务愿意尝试，实践中收获成就感，建立自信。")
    st.write("课堂场景：乡土成果展示，记录学生主动展示、敢于挑战任务的行为。")

    st.subheader("核心逻辑说明")
    st.write("传统德育评价多依赖主观评语。本项目将德育目标落地到乡土校本课程场景，以可观测的品质行为作为评价依据，采集课程前后两次行为记录，可视化展示学生行为层面成长，佐证乡土文化浸润的育人实效。")
    st.markdown("</div>", unsafe_allow_html=True)

# ====================== AI赋能校本课程开发 ======================
elif page == "AI赋能校本课程开发":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.subheader("🤖 AI校本课程提示词生成器")
    st.write("填写课程基础信息，一键生成完整校本课程教案，配套课堂品质行为观察量表，复制到AI即可使用。")

    col1, col2 = st.columns(2)
    with col1:
        grade_sel = st.selectbox("授课年级", ["三年级","四年级","五年级","六年级"])
        behavior_list = st.multiselect("重点培育品质行为",["P共情感恩","E专注坚持","R协作互助","M乡土认同","A自信表达"],
                                       default=["P共情感恩","M乡土认同"])
    with col2:
        theme = st.text_input("乡土校本课程主题", value="簕杜鹃乡土文化探究")
        lesson_count = st.number_input("总课时", min_value=1, max_value=10, value=2)

    behavior_text = "，".join(behavior_list)
    prompt_text = f"""
请为小学{grade_sel}设计{lesson_count}课时的乡土校本德育课程，课程主题：{theme}。
课程立足本土乡土文化资源，基于PERMA框架，重点培育学生品质行为：{behavior_text}。

输出完整课程方案，包含：
1.课程设计理念：乡土文化浸润，把文化认知转化为学生品质行为，落实义务教育核心素养；
2.核心素养目标（文化自信、健全人格、责任意识、合作探究，写可观察的学生行为目标）；
3.教学重难点；
4.分课时教学设计：教学环节、时长、学生实践活动、教师引导话术；
5.配套课堂品质行为观察量表，对接PERMA行为观测维度；
6.教学实施注意事项与本土化素材建议。

要求：面向乡村小学，突出体验实践，拒绝空洞说教，文本适配校本课程申报材料。
"""
    st.subheader("✅ 生成提示词（直接全选复制）")
    st.code(prompt_text, language="text")
    st.info("💡 将上面全部文字复制粘贴给AI，直接产出完整教案+行为观察量表")

    st.subheader("🎨 AI辅助课堂素材")
    st.write("- AI绘制本土风物插画、乡土主题海报，补充课堂PPT配图；")
    st.write("- 生成情景对话脚本，用于课堂角色扮演；")
    st.write("- 辅助设计课堂任务单、记录表单。")

    st.subheader("⚖️ AI使用原则")
    st.write("教师主导课堂，AI仅作为备课辅助工具；全部AI产出内容需要教师审核、本土化修改，贴合小学生认知，坚守文化育人主线。")
    st.markdown("</div>", unsafe_allow_html=True)

# ====================== 乡土校本课程案例 ======================
elif page == "乡土校本课程案例":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.subheader("📚 乡土校本德育课程示例")
    st.write("全套课程共8课时，面向3‑6年级，以PERMA行为观测为框架，依托河源本土乡土资源开展体验式实践课。每一课聚焦1‑2项品质行为，以学生实地实践活动为主。")

    st.subheader("📝 课程整体流程")
    st.write("乡土情景导入 → 沉浸式文化体验活动 → 小组研讨交流 → 学生创作产出 → 成果展示 + 教师行为观察评价")
    st.write("评价方式：课堂过程性行为观察记录 + 课程前后行为量表 + 学生品质行为成长档案，多维度评估文化浸润带来的行为改变。")

    st.subheader("📂 课程主题示例")
    st.write("**主题1：家乡草木与生命感悟（P共情感恩）**")
    st.write("观察本土植物，感受家乡自然之美，引导学生学会感恩；重点观察共情、感恩表达行为。")

    st.write("**主题2：乡土手作实践（E专注坚持 + R协作互助）**")
    st.write("小组共同完成乡土标本手工，磨炼耐心，学习分工互助；重点观察坚持、协作行为。")

    st.write("**主题3：本土红色与民俗研学（M乡土认同）**")
    st.write("了解家乡历史人物与民俗故事，厚植家国乡土情怀；重点观察探究本土文化、主动表达乡土认同的行为。")

    st.write("**主题4：乡土文化成果展（A自信表达）**")
    st.write("展示学生的乡土创作，分享学习收获；重点观察主动展示、敢于表达的行为。")

    st.subheader("🏫 课堂实施说明")
    st.write("课程走出单纯教室讲授，把校园、乡野、红色旧址变成学习场所。教师在活动过程中，对照PERMA观测表，客观记录学生真实行为，不做主观定性评价。")
    st.markdown("</div>", unsafe_allow_html=True)

# ====================== 品质行为前后对比评估 ======================
elif page == "品质行为前后对比评估":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.subheader("📊 学生品质行为前后对比评估")
    st.write("录入学生课程前、课程后的PERMA五个维度得分，自动生成对比图表，直观看到学生品质行为变化。")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("课程前测得分")
        pre_positive = st.slider("P 积极情绪", 1,5,3)
        pre_engage = st.slider("E 投入专注", 1,5,3)
        pre_relation = st.slider("R 人际关系", 1,5,3)
        pre_meaning = st.slider("M 意义认同", 1,5,3)
        pre_achieve = st.slider("A 成就感知", 1,5,3)
    with col2:
        st.subheader("课程后测得分")
        post_positive = st.slider("P 积极情绪", 1,5,4)
        post_engage = st.slider("E 投入专注", 1,5,4)
        post_relation = st.slider("R 人际关系", 1,5,4)
        post_meaning = st.slider("M 意义认同", 1,5,4)
        post_achieve = st.slider("A 成就感知", 1,5,4)

    import pandas as pd
    data = pd.DataFrame({
        "维度":["积极情绪","投入专注","人际关系","意义认同","成就感知"],
        "课程前":[pre_positive, pre_engage, pre_relation, pre_meaning, pre_achieve],
        "课程后":[post_positive, post_engage, post_relation, post_meaning, post_achieve]
    })
    fig = px.bar(data, x="维度", y=["课程前","课程后"], barmode="group",
                 title="品质行为课程前后对比图", range_y=[0,5])
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ====================== 学生品质行为成长档案 ======================
elif page == "学生品质行为成长档案":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.subheader("📁 学生品质行为成长档案录入与导出")
    st.write("录入学生基础信息与课堂行为记录，一键导出成长档案。")

    name = st.text_input("学生姓名")
    grade = st.text_input("班级")
    note = st.text_area("课堂行为观察记录")

    if st.button("生成成长档案"):
        export_text = f"""
# 学生品质行为成长档案
姓名：{name}
班级：{grade}
观察记录：{note}
"""
        # 导出txt文件
        from io import StringIO
        s = StringIO()
        s.write(export_text)
        st.download_button("下载档案文本", data=s.getvalue(), file_name="学生成长档案.txt")
        st.success("档案已生成，点击按钮下载！")
    st.markdown("</div>", unsafe_allow_html=True)
